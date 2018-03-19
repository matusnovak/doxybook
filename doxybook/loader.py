import os
import xml.etree.ElementTree

from doxybook.node import Node
from doxybook.kind import Kind, isKindLanguage
from doxybook.utils import tokenize
from doxybook.cache import Cache

def parseRoot(root: xml.etree.ElementTree):
    parent = Node('root', 'root', Kind.ROOT)
    for compound in root.iter('compound'):
        child = Node(compound.find('name').text, compound.get('refid'), Kind(compound.get('kind')))
        parent.addMember(child)
        print('node', parent.name, 'has', len(parent.members), 'members')
        for member in compound.findall('member'):
            subchild = Node(member.find('name').text, member.get('refid'), Kind(member.get('kind')))
            child.addMember(subchild)
    return parent

def reparseChildren(child: Node, root: Node, output: Node):
    tokens = tokenize(child.name, '::')
    if len(tokens) < 1:
        return
    
    i = 0
    while i < len(tokens):
        outFound = output.findMember(tokens[i])
        if outFound == None:
            addedNode = Node(tokens[i], None, Kind('variable'))
            output.addMember(addedNode)
            output = addedNode
        else:
            output = outFound

        i += 1

    output.kind = child.kind
    output.refid = child.refid
    return output

def reparseRoot(rootNode: Node, newRoot: Node):
    while len(rootNode.members) > 0:
        child = rootNode.members[0]
        if isKindLanguage(child.kind):
            newChild = reparseChildren(child, rootNode, newRoot)
            lastEnum = None
            for subchild in child.members:
                if subchild.kind == Kind.ENUMVALUE:
                    lastEnum.addMember(subchild)
                    continue
                else:
                    newChild.addMember(subchild)

                if subchild.kind == Kind.ENUM:
                    lastEnum = subchild
        rootNode.members.pop(0)

def finalize(cache: Cache, node: Node):
    node.finalize()
    cache.add(node.refid, node)
    for child in node.members:
        finalize(cache, child)

def debug(node: Node, indent: str = ''):
    print(indent, 'Node name:', node.name, 'refid:', node.refid)
    for member in node.members:
        debug(member, indent + '  |-')

def loadRoot(cache: Cache, dirPath: str) -> Node:
    print("XML index from: " + dirPath)
    e = xml.etree.ElementTree.parse(os.path.join(dirPath, 'index.xml')).getroot()
    
    outNode = Node('root', 'root', Kind.ROOT)
    
    rootNode = parseRoot(e)
    reparseRoot(rootNode, outNode)
    finalize(cache, outNode)
    
    debug(outNode)
    return outNode
    