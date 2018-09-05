import os

from doxybook.markdown import MdDocument, MdLink, MdBold, MdHeader, MdList, MdParagraph, MdParagraph, MdRenderer, Text
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.config import config

# Construct a tree of all parents (classes, structs, etc...)
def recursive_hierarchy(node: Node, mdl: MdList, keywords: list):
    for child in node.members:
        if child.kind.is_parent():
            p = MdParagraph([])
            p.append(Text(child.get_kind_str() + ' '))
            keywords.append(child.name)
            p.append(MdLink([MdBold([Text(child.name)])], child.url))
            sublist = MdList([])
            recursive_hierarchy(child, sublist, keywords)
            p.append(sublist)
            mdl.append(p)

def generate_annotated(path: str, root: Node):
    output_file = os.path.join(path, 'annotated.md')
    print('Generating ' + output_file)
    document = MdDocument()
    keywords = []

    # Add title
    document.append(MdHeader(1, [Text('Class List')]))

    # Add description
    document.append(MdParagraph([Text('Here are the classes, structs, unions and interfaces with brief descriptions:')]))

    # Recursively add all members
    mdl = MdList([])
    recursive_hierarchy(root, mdl, keywords)
    document.append(mdl)

    if not config.noindex:
        document.set_keywords(keywords)
    document.set_title('Annotated')

    # Save
    with open(output_file, 'w+') as f:
        document.render(MdRenderer(f))