import os
import re
import xml.etree.ElementTree
from typing import List

from doxybook.markdown import Md, MdDocument, MdCode, MdCodeBlock, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.generators.paragraph import generateParagraph, convertXmlPara

def generateDir(indexDir: str, outputDir: str, node: Node, cache: Cache) -> dict:
    outputFile = os.path.join(outputDir, node.refid + '.md')
    print('Generating ' + outputFile)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text(node.name + ' Directory Reference')]))

    # Load XML
    xmlRoot = xml.etree.ElementTree.parse(os.path.join(indexDir, node.refid + '.xml')).getroot()
    if xmlRoot is None:
        IndexError('Root xml not found!')
    compounddef = xmlRoot.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')

    document.append(MdHeader(2, [Text('Files')]))

    lst = MdList([])
    for innerdir in compounddef.findall('innerdir'):
        lst.append(MdParagraph([MdBold([MdLink([Text(innerdir.text + '/')], innerdir.get('refid') + '.md')])]))
    for innerfile in compounddef.findall('innerfile'):
        lst.append(MdParagraph([MdBold([MdLink([Text(innerfile.text)], innerfile.get('refid') + '.md')])]))
    document.append(lst)

    # Save
    with open(outputFile, 'w') as f:
        document.render(MdRenderer(f))