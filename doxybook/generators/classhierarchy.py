import os

from doxybook.markdown import MdDocument, MdText, MdLink, MdHeader, MdList, MdParagraph, MdParagraph, MdRenderer
from doxybook.node import Node
from doxybook.kind import Kind

def recursiveHierarchy(node: Node, mdl: MdList):
    for child in node.members:
        if child.kind is Kind.NAMESPACE or child.kind is Kind.CLASS or child.kind is Kind.STRUCT:
            p = MdParagraph([])
            p.append(MdText(child.getKindStr() + ' '))
            p.append(MdLink(child.name, child.url))
            sublist = MdList([])
            recursiveHierarchy(child, sublist)
            p.append(sublist)
            mdl.append(p)

def generate(outputDir: str, root: Node):
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [MdText('Class Hierarchy')]))

    # Add description
    document.append(MdParagraph([MdText('This inheritance list is sorted roughly, but not completely, alphabetically:')]))

    # Recursively add all members
    mdl = MdList([])
    recursiveHierarchy(root, mdl)
    document.append(mdl)

    # Save
    os.makedirs(outputDir, exist_ok=True)
    with open(os.path.join(outputDir, 'hierarchy.md'), 'w+') as f:
        document.render(MdRenderer(f))