import os
import re
import xml.etree.ElementTree
from typing import List

from doxybook.markdown import Md, MdDocument, MdCode, MdCodeBlock, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.generators.paragraph import generateParagraph, convertXmlPara

def findPlace(directory: dict, tokens: List[str], refid: str):
    if len(tokens) == 1:
        directory[tokens[0]] = {'#': refid}
        return directory[tokens[0]]
    elif len(tokens) == 0:
        raise Exception('This should never happen')
    else:
        if tokens[0] not in directory:
            directory[tokens[0]] = {}
        return findPlace(directory[tokens[0]], tokens[1:], refid)

def generateListRecursive(directory: dict):
    lst = MdList([])
    for key,value in directory.items():
        if key == '#':
            continue
        if isinstance(value, dict):
            lst.append(MdParagraph([
                MdBold([MdLink([Text(key + '/')], value['#'] + '.md')]),
                generateListRecursive(value)
            ]))
        else:
            lst.append(MdParagraph([MdBold([MdLink([Text(key)], value + '.md')])]))
    return lst

def generateFiles(indexDir: str, outputDir: str, node: Node, cache: Cache) -> dict:
    outputFile = os.path.join(outputDir, 'files.md')
    print('Generating ' + outputFile)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text('File List')]))
    document.append(MdParagraph([Text('Here is a list of all documented files with brief descriptions:')]))

    directory = {}

    # List through all directories
    for child in node.members:
        if child.kind == Kind.DIR:
            tokens = child.name.split('/')
            found = findPlace(directory, tokens, child.refid)
            
            # Load XML
            xmlRoot = xml.etree.ElementTree.parse(os.path.join(indexDir, child.refid + '.xml')).getroot()
            if xmlRoot is None:
                IndexError('Root xml not found!')
            compounddef = xmlRoot.find('compounddef')
            if compounddef is None:
                IndexError('compounddef not found in xml!')

            for innerfile in compounddef.findall('innerfile'):
                found[innerfile.text] = innerfile.get('refid')
    
    lst = generateListRecursive(directory)
    document.append(lst)

    # Save
    with open(outputFile, 'w') as f:
        document.render(MdRenderer(f))

    return directory