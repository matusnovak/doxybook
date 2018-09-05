import os
import re
import xml.etree.ElementTree
from typing import List

from doxybook.markdown import Md, MdDocument, MdCode, MdCodeBlock, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.config import config
from doxybook.generators.paragraph import generate_paragraph, convert_xml_para

def generate_page(index_path: str, output_path: str, refid: str, cache: Cache):
    output_file = os.path.join(output_path, refid + '.md')
    print('Generating ' + output_file)
    document = MdDocument()

    # Load XML
    xml_root = xml.etree.ElementTree.parse(os.path.join(index_path, refid + '.xml')).getroot()
    if xml_root is None:
        IndexError('Root xml not found!')
    compounddef = xml_root.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')

    title = compounddef.find('title').text

    # Add title
    document.append(MdHeader(1, [Text(title)]))

    document.append(MdParagraph(convert_xml_para(compounddef.find('detaileddescription'), cache)))

    document.set_title(title)
    
    # Save
    with open(output_file, 'w+') as f:
        document.render(MdRenderer(f))

    return title