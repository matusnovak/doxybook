import os

from doxybook.markdown import MdDocument, MdLink, MdHeader, MdList, MdParagraph, MdParagraph, MdRenderer, Text
from doxybook.node import Node
from doxybook.kind import Kind

def recursiveHierarchy(node: Node, mdl: MdList):
    for child in node.members:
        if child.kind is Kind.NAMESPACE or child.kind is Kind.CLASS or child.kind is Kind.STRUCT:
            p = MdParagraph([])
            p.append(Text(child.getKindStr() + ' '))
            p.append(MdLink([Text(child.name)], child.url))
            sublist = MdList([])
            recursiveHierarchy(child, sublist)
            p.append(sublist)
            mdl.append(p)

def generateHierarchy(outputDir: str, root: Node):
    outputFile = os.path.join(outputDir, 'hierarchy.md')
    print('Generating ' + outputFile)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text('Class Hierarchy')]))

    # Add description
    document.append(MdParagraph([Text('This inheritance list is sorted roughly, but not completely, alphabetically:')]))

    # Recursively add all members
    mdl = MdList([])
    recursiveHierarchy(root, mdl)
    document.append(mdl)

    # Save
    os.makedirs(outputDir, exist_ok=True)
    with open(outputFile, 'w+') as f:
        document.render(MdRenderer(f))