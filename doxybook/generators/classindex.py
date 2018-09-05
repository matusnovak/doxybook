import os

from doxybook.markdown import MdDocument, MdLink, MdBold, MdHeader, MdList, MdParagraph, MdRenderer, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.config import config

# Generate disctionary based on the first letter of the node
def recursive_dictionary(node: Node, dictionary: dict):
    if node.kind == Kind.CLASS or node.kind == Kind.STRUCT:
        key = node.name.upper()[0]
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(node)
    for child in node.members:
        recursive_dictionary(child, dictionary)

def generate_class_index(path: str, root: Node):
    output_file = os.path.join(path, 'classes.md')
    print('Generating ' + output_file)
    document = MdDocument()
    keywords = []

    # Add title
    document.append(MdHeader(1, [Text('Class Index')]))

    # Sort
    dictionary = {}
    recursive_dictionary(root, dictionary)

    for key in list(sorted(dictionary.keys())):
        document.append(MdHeader(2, [Text(key)]))

        mdl = MdList([])
        for member in dictionary[key]:
            p = MdParagraph([])
            full_name = member.get_full_name(False)
            keywords.append(full_name)
            p.append(MdLink([MdBold([Text(full_name)])], member.url))

            namespace = member.get_namespace()
            if namespace is not None:
                p.append(Text(' ('))
                p.append(MdLink([MdBold([Text(namespace.get_full_name(False))])], namespace.url))
                p.append(Text(')'))
            mdl.append(p)

        document.append(mdl)
        document.append(Br())

    if not config.noindex:
        document.set_keywords(keywords)
    document.set_title('Class Index')

    # Save
    with open(output_file, 'w') as f:
        document.render(MdRenderer(f))
