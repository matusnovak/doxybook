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

def find_place(directory: dict, tokens: List[str], refid: str):
    if len(tokens) == 1:
        directory[tokens[0]] = {'#': refid}
        return directory[tokens[0]]
    elif len(tokens) == 0:
        raise Exception('Tokens were empty! This should never happen, please contact the owner!')
    else:
        if tokens[0] not in directory:
            directory[tokens[0]] = {}
        return find_place(directory[tokens[0]], tokens[1:], refid)

def generate_list_recursive(directory: dict, keywords: List[str]):
    lst = MdList([])
    for key,value in directory.items():
        if key == '#':
            continue
        if isinstance(value, dict):
            lst.append(MdParagraph([
                MdBold([MdLink([Text(key + '/')], value['#'] + '.md')]),
                generate_list_recursive(value, keywords)
            ]))
            keywords.append(key)
        else:
            lst.append(MdParagraph([MdBold([MdLink([Text(key)], value + '.md')])]))
            keywords.append(key)
    return lst

def generate_files(index_path: str, output_path: str, node: Node, cache: Cache) -> dict:
    output_file = os.path.join(output_path, 'files.md')
    print('Generating ' + output_file)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text('File List')]))
    document.append(MdParagraph([Text('Here is a list of all documented files with brief descriptions:')]))

    directory = {}
    keywords = []

    # List through all directories
    for child in node.members:
        if child.kind == Kind.DIR:
            tokens = child.name.split('/')
            found = find_place(directory, tokens, child.refid)
            
            # Load XML
            xml_root = xml.etree.ElementTree.parse(os.path.join(index_path, child.refid + '.xml')).getroot()
            if xml_root is None:
                IndexError('Root xml not found!')
            compounddef = xml_root.find('compounddef')
            if compounddef is None:
                IndexError('compounddef not found in xml!')

            for innerfile in compounddef.findall('innerfile'):
                found[innerfile.text] = innerfile.get('refid')
    
    lst = generate_list_recursive(directory, keywords)
    document.append(lst)

    if not config.noindex:
        document.set_keywords(keywords)
    document.set_title('Files')

    # Save
    with open(output_file, 'w') as f:
        document.render(MdRenderer(f))

    return directory