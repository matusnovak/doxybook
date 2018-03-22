import os
import re
import xml.etree.ElementTree
from typing import List

from doxybook.markdown import Md, MdDocument, MdCode, MdCodeBlock, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.generators.paragraph import generateParagraph, convertXmlPara

def generateFile(indexDir: str, outputDir: str, node: Node, cache: Cache) -> dict:
    outputFile = os.path.join(outputDir, node.refid + '_source.md')
    print('Generating ' + outputFile)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text(node.name + ' File Reference')]))

    # Load XML
    xmlRoot = xml.etree.ElementTree.parse(os.path.join(indexDir, node.refid + '.xml')).getroot()
    if xmlRoot is None:
        IndexError('Root xml not found!')
    compounddef = xmlRoot.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')  

    document.append(MdParagraph([MdBold([MdLink([Text('Go to the documentation of this file.')], node.refid + '.md')])]))  

    location = compounddef.find('location')
    if location is not None:
        document.append(MdParagraph([Text('Source: '), MdCode([Text(location.get('file'))])]))

    programlisting = compounddef.find('programlisting')
    if programlisting is None:
        return

    document.append(MdParagraph(convertXmlPara(compounddef, cache)))

    # Save
    with open(outputFile, 'w') as f:
        document.render(MdRenderer(f))