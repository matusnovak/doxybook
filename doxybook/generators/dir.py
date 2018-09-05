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

def generate_dir(index_path: str, output_path: str, node: Node, cache: Cache) -> dict:
    output_file = os.path.join(output_path, node.refid + '.md')
    print('Generating ' + output_file)
    document = MdDocument()

    # Add title
    title = node.name + ' Directory Reference'
    document.append(MdHeader(1, [Text(title)]))

    # Load XML
    xml_root = xml.etree.ElementTree.parse(os.path.join(index_path, node.refid + '.xml')).getroot()
    if xml_root is None:
        IndexError('Root xml not found!')
    compounddef = xml_root.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')

    document.append(MdHeader(2, [Text('Files')]))

    lst = MdList([])
    keywords = []

    for innerdir in compounddef.findall('innerdir'):
        lst.append(MdParagraph([MdBold([MdLink([Text(innerdir.text + '/')], innerdir.get('refid') + '.md')])]))
        keywords.append(innerdir.text)
    for innerfile in compounddef.findall('innerfile'):
        lst.append(MdParagraph([MdBold([MdLink([Text(innerfile.text)], innerfile.get('refid') + '.md')])]))
        keywords.append(innerfile.text)
    document.append(lst)

    if not config.noindex:
        document.set_keywords(keywords)
    document.set_title(title)

    # Save
    with open(output_file, 'w') as f:
        document.render(MdRenderer(f))