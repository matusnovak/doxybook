import os

from doxybook.markdown import MdDocument, MdLink, MdBold, MdHeader, MdList, MdParagraph, MdRenderer, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.config import config
from doxybook.utils import lookahead

# Generate disctionary based on the first letter of the node
def recursive_dictionary(kind: Kind, node: Node, dictionary: dict):
    if node.kind == kind:
        key = node.name.upper()[0]
        if key not in dictionary:
            dictionary[key] = []
        if node.parent is not None and node.parent.kind.is_parent() and not node.parent.kind == Kind.NAMESPACE:
            dictionary[key].append(node)
    for child in node.members:
        recursive_dictionary(kind, child, dictionary)

def generate_variable_index(path: str, root: Node):
    generate(path, root, Kind.VARIABLE, 'variables', 'Variable Index', 'Here is a list of all variables with links to the class documentation for each member:')

def generate_function_index(path: str, root: Node):
    generate(path, root, Kind.FUNCTION, 'functions', 'Function Index', 'Here is a list of all functions with links to the class documentation for each member:')

def generate_enum_index(path: str, root: Node):
    generate(path, root, Kind.ENUM, 'enumerations', 'Enumeration Index', 'Here is a list of all enumerations with links to the class documentation for each member:')

def generate(path: str, root: Node, kind: Kind, filename: str, title: str, subtitle: str):
    output_file = os.path.join(path, filename + '.md')
    print('Generating ' + output_file)
    document = MdDocument()
    keywords = []

    # Add title
    document.append(MdHeader(1, [Text(title)]))
    document.append(MdParagraph([Text(subtitle)]))

    # Sort
    dictionary = {}
    recursive_dictionary(kind, root, dictionary)

    for key in list(sorted(dictionary.keys())):
        document.append(MdHeader(2, [Text(key)]))

        mdl = MdList([])

        # Remove overloads and sort into columns of classes
        class_dictionary = {}
        for member in dictionary[key]:
            if member.name not in class_dictionary:
                class_dictionary[member.name] = []

            if len(class_dictionary[member.name]) > 0:
                if class_dictionary[member.name][-1].parent == member.parent:
                    continue
            class_dictionary[member.name].append(member)

        for dict_key in list(sorted(class_dictionary.keys())):
            p = MdParagraph([])
            first = class_dictionary[dict_key][-1]

            full_name = first.get_full_name(False)
            keywords.append(full_name)
            p.append(MdBold([Text(first.name)]))

            p.append(Text(' ('))
            for member, has_next in lookahead(class_dictionary[dict_key]):
                parent = member.parent
                p.append(MdLink([MdBold([Text(parent.get_full_name(True))])], parent.url + '#' + member.get_anchor_hash()))
                if has_next:
                    p.append(Text(', '))
            p.append(Text(')'))

            mdl.append(p)

        document.append(mdl)
        document.append(Br())

    if not config.noindex:
        document.set_keywords(keywords)
    document.set_title(title)

    # Save
    with open(output_file, 'w') as f:
        document.render(MdRenderer(f))

