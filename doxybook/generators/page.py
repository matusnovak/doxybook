import os
import re
import xml.etree.ElementTree
from typing import List

from doxybook.markdown import Md, MdDocument, MdCode, MdCodeBlock, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.generators.paragraph import generateParagraph, convertXmlPara

def generatePage(indexDir: str, outputDir: str, refid: str, cache: Cache):
    outputFile = os.path.join(outputDir, refid + '.md')
    print('Generating ' + outputFile)
    document = MdDocument()

    # Load XML
    xmlRoot = xml.etree.ElementTree.parse(os.path.join(indexDir, refid + '.xml')).getroot()
    if xmlRoot is None:
        IndexError('Root xml not found!')
    compounddef = xmlRoot.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')

    title = compounddef.find('title').text

    # Add title
    document.append(MdHeader(1, [Text(title)]))

    document.append(MdParagraph(convertXmlPara(compounddef.find('detaileddescription'), cache)))
    
    # Save
    with open(outputFile, 'w+') as f:
        document.render(MdRenderer(f))

    return title