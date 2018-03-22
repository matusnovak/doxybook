import os
import re
import xml.etree.ElementTree
from typing import List

from doxybook.markdown import Md, MdDocument, MdCode, MdCodeBlock, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.generators.paragraph import generateParagraph, convertXmlPara

def generatePages(indexDir: str, outputDir: str, node: Node, cache: Cache) -> dict:
    outputFile = os.path.join(outputDir, 'pages.md')
    print('Generating ' + outputFile)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text('Related Pages')]))

    document.append(MdParagraph([Text('Here is a list of all related documentation pages:')]))
    
    lst = MdList([])

    modules = {}

    # List through all groups
    for child in node.members:
        if child.kind == Kind.PAGE:
            path = os.path.join(indexDir, child.refid + '.xml')
            xmlRoot = xml.etree.ElementTree.parse(path).getroot()
            compounddef = xmlRoot.find('compounddef')
            if compounddef is not None:
                briefdescription = compounddef.find('briefdescription')
                briefdescriptionParas = []
                if briefdescription is not None:
                    briefdescriptionParas = compounddef.find('briefdescription').findall('para')
                p = MdParagraph([])

                name = compounddef.find('title').text
                refid = compounddef.get('id')
                p.append(MdBold([MdLink([Text(name)], refid + '.md')]))

                modules[refid] = name

                p.append(Text(' '))
                for para in briefdescriptionParas:
                    p.extend(convertXmlPara(para, cache))
                lst.append(p)

    document.append(lst)

    # Save
    with open(outputFile, 'w') as f:
        document.render(MdRenderer(f))

    return modules