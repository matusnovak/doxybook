import os

from doxybook.markdown import MdDocument, MdLink, MdBold, MdHeader, MdList, MdParagraph, MdRenderer, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind

def recursiveDictionary(node: Node, dictionary: dict):
    if node.kind == Kind.CLASS or node.kind == Kind.STRUCT:
        key = node.name.upper()[0]
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(node)
    for child in node.members:
        recursiveDictionary(child, dictionary)

def generateClassIndex(outputDir: str, root: Node, noindex: bool):
    outputFile = os.path.join(outputDir, 'classes.md')
    print('Generating ' + outputFile)
    document = MdDocument()
    keywords = []

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
            fullName = member.getFullName(False)
            keywords.append(fullName)
            p.append(MdLink([MdBold([Text(fullName)])], member.url))

            namespace = member.getNamespace()
            if namespace is not None:
                p.append(Text(' ('))
                p.append(MdLink([MdBold([Text(namespace.getFullName(False))])], namespace.url))
                p.append(Text(')'))
            mdl.append(p)

        document.append(mdl)
        document.append(Br())

    if not noindex:
        document.setKeywords(keywords)

    # Save
    with open(outputFile, 'w') as f:
        document.render(MdRenderer(f))
