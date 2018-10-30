import os
import xml.etree.ElementTree
from itertools import filterfalse

from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.utils import tokenize
from doxybook.cache import Cache
from doxybook.config import config

def parse_root(root: xml.etree.ElementTree):
    parent = Node('root', 'root', Kind.ROOT)
    for compound in root.iter('compound'):
        child = Node(compound.find('name').text, compound.get('refid'), Kind(compound.get('kind')))
        parent.add_member(child)
        for member in compound.findall('member'):
            subchild = Node(member.find('name').text, member.get('refid'), Kind(member.get('kind')))
            child.add_member(subchild)
    return parent

def reparse_children(child: Node, root: Node, output: Node):
    tokens = tokenize(child.name, '::')
    if len(tokens) < 1:
        return
    
    i = 0
    while i < len(tokens):
        out_found = output.find_member(tokens[i])
        if out_found == None:
            added_node = Node(tokens[i], None, Kind('variable'))
            output.add_member(added_node)
            output = added_node
        else:
            output = out_found

        i += 1

    output.kind = child.kind
    output.refid = child.refid
    return output

def reparse_root(root_node: Node, new_root: Node):
    while len(root_node.members) > 0:
        child = root_node.members[0]
        if child.kind.is_language():
            new_child = reparse_children(child, root_node, new_root)
            last_enum = None
            for subchild in child.members:
                if subchild.kind == Kind.ENUMVALUE:
                    last_enum.add_member(subchild)
                    continue
                else:
                    new_child.add_member(subchild)

                if subchild.kind == Kind.ENUM:
                    last_enum = subchild
        else:
            new_root.add_member(child)
        root_node.members.pop(0)

def check_for_overloads(child: Node):
    if child.kind.is_parent() or child.kind == Kind.ROOT:
        overload_num = {}
        name_dict = {}
        for subchild in child.members:
            if subchild.name not in name_dict:
                name_dict[subchild.name] = 0
                overload_num[subchild.name] = 1
            name_dict[subchild.name] += 1
        
        for subchild in child.members:
            if name_dict[subchild.name] > 1:
                subchild.overloaded = True
                subchild.overload_num = overload_num[subchild.name]
                subchild.overload_total = name_dict[subchild.name]
                overload_num[subchild.name] += 1

        for subchild in child.members:
            check_for_overloads(subchild)

def check_innergroups(path: str, root: Node, group: Node):
    remov_from_root = []
    e = xml.etree.ElementTree.parse(os.path.join(path, group.refid + '.xml')).getroot()
    compounddef = e.find('compounddef')
    for innergroup in compounddef.findall('innergroup'):
        innergroup_refid = innergroup.get('refid')
        found: Node = None
        for mem in root.members:
            if mem.kind == Kind.GROUP and mem.refid == innergroup_refid:
                found = mem
                break
        group.add_member(found)
        remov_from_root.append(found)
    return remov_from_root

def parse_groups(path: str, root: Node):
    remov_from_root = []
    for child in root.members:
        if child.kind == Kind.GROUP:
            remov_from_root.extend(check_innergroups(path, root, child))
    
    root.members[:] = filterfalse(lambda x: x in remov_from_root, root.members)

def finalize(cache: Cache, node: Node):
    node.finalize()
    cache.add(node.refid, node)
    node.members = sorted(node.members, key=lambda k : k.name) 
    for child in node.members:
        finalize(cache, child)

def debug_node(node: Node, indent: str = ''):
    if node.overloaded:
        print(indent, 'Node name:', node.name, '(' + str(node.overload_num) + '/' + str(node.overload_total) + ')', 'refid:', node.refid)
    else:
        print(indent, 'Node name:', node.name, 'refid:', node.refid, 'kind:', node.kind.value)
    for member in node.members:
        debug_node(member, indent + '  |-')

def load_root(cache: Cache, path: str) -> Node:
    print("XML index from: " + path)
    e = xml.etree.ElementTree.parse(os.path.join(path, 'index.xml')).getroot()
    
    out_node = Node('Global', 'root', Kind.ROOT)
    
    root_node = parse_root(e)
    reparse_root(root_node, out_node)
    parse_groups(path, out_node)
    check_for_overloads(out_node)
    finalize(cache, out_node)
    
    if config.debug:
        debug_node(out_node)
    return out_node
    