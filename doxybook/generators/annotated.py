import os

from doxybook.markdown import MdDocument, MdLink, MdBold, MdHeader, MdList, MdParagraph, MdParagraph, MdRenderer, Text
from doxybook.node import Node
from doxybook.kind import Kind

def recursiveHierarchy(node: Node, mdl: MdList):
    for child in node.members:
        if child.kind is Kind.NAMESPACE or child.kind is Kind.CLASS or child.kind is Kind.STRUCT:
            p = MdParagraph([])
            p.append(Text(child.getKindStr() + ' '))
            p.append(MdLink([MdBold([Text(child.name)])], child.url))
            sublist = MdList([])
            recursiveHierarchy(child, sublist)
            p.append(sublist)
            mdl.append(p)

def generateAnnotated(outputDir: str, root: Node):
    outputFile = os.path.join(outputDir, 'annotated.md')
    print('Generating ' + outputFile)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text('Class List')]))

    # Add description
    document.append(MdParagraph([Text('Here are the classes, structs, unions and interfaces with brief descriptions:')]))

    # Recursively add all members
    mdl = MdList([])
    recursiveHierarchy(root, mdl)
    document.append(mdl)

    # Save
    with open(outputFile, 'w+') as f:
        document.render(MdRenderer(f))