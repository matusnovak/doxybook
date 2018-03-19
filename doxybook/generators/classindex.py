import os

from doxybook.markdown import MdDocument, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, Text
from doxybook.node import Node
from doxybook.kind import Kind

def recursiveDictionary(node: Node, dictionary: dict):
    if node.kind == Kind.CLASS or node.kind == Kind.STRUCT:
        key = node.name[0]
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(node)
    for child in node.members:
        recursiveDictionary(child, dictionary)

def generateClassIndex(outputDir: str, root: Node):
    outputFile = os.path.join(outputDir, 'classes.md')
    print('Generating ' + outputFile)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text('Class Index')]))

    # Sort
    dictionary = {}
    recursiveDictionary(root, dictionary)

    for key in list(sorted(dictionary.keys())):
        document.append(MdHeader(2, [Text(key)]))

        mdl = MdList([])
        for member in dictionary[key]:
            p = MdParagraph([])
            p.append(MdLink([Text(member.getFullName(False))], member.url))

            namespace = member.getNamespace()
            if namespace is not None:
                p.append(Text(' ('))
                p.append(MdLink([Text(namespace.getFullName(False))], namespace.url))
                p.append(Text(')'))
            mdl.append(p)

        document.append(mdl)

    # Save
    os.makedirs(outputDir, exist_ok=True)
    with open(outputFile, 'w+') as f:
        document.render(MdRenderer(f))
