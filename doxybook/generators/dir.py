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

def get_brief_description(index_path: str, refid: str, cache: Cache) -> str:
    brief = []
    try:
        root = xml.etree.ElementTree.parse(os.path.join(index_path, refid + '.xml')).getroot()
        compound = root.find('compounddef')                
        briefdescription = compound.find('briefdescription').findall('para')
        if len(briefdescription) > 0:
            brief.append(Text(' '))
            for para in briefdescription:
                brief.extend(convert_xml_para(para, cache))
    except Exception as e:
        pass
    return brief

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

    # Add brief description
    detaileddescription_paras = compounddef.find('detaileddescription').findall('para')
    briefdescription_paras = compounddef.find('briefdescription').findall('para')

    if len(briefdescription_paras) > 0:
        p = MdParagraph([])
        for para in briefdescription_paras:
            p.extend(convert_xml_para(para, cache))
        if len(detaileddescription_paras) > 0:
            p.append(MdLink([Text('More...')], '#detailed-description'))
        document.append(p)
        document.append(Text('\n'))

    document.append(MdHeader(2, [Text('Files')]))

    lst = MdList([])
    keywords = []

    for innerdir in compounddef.findall('innerdir'):
        refid = innerdir.get('refid')
        brief = get_brief_description(index_path, refid, cache)

        link_with_brief = [MdLink([MdBold([Text(innerdir.text + '/')])], refid + '.md')]
        link_with_brief.extend(brief)

        lst.append(MdParagraph(link_with_brief))
        keywords.append(innerdir.text)

    for innerfile in compounddef.findall('innerfile'):
        refid = innerfile.get('refid')
        brief = get_brief_description(index_path, refid, cache)

        link_with_brief = [MdLink([MdBold([Text(innerfile.text)])], refid + '.md')]
        link_with_brief.extend(brief)

        lst.append(MdParagraph(link_with_brief))
        keywords.append(innerfile.text)

    document.append(lst)
    document.append(Text('\n'))

    # Add detailed description
    if len(detaileddescription_paras) > 0:
        document.append(MdHeader(2, [Text('Detailed Description')]))
        document.extend(generate_paragraph(compounddef.find('detaileddescription').findall('para'), cache))

    if not config.noindex:
        document.set_keywords(keywords)
    document.set_title(title)

    # Save
    with open(output_file, 'w') as f:
        document.render(MdRenderer(f))