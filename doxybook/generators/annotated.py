import os
import xml.etree.ElementTree

from doxybook.markdown import MdDocument, MdLink, MdBold, MdHeader, MdList, MdParagraph, MdParagraph, MdRenderer, Text
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.config import config
from doxybook.cache import Cache
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

# Construct a tree of all parents (classes, structs, etc...)
def recursive_hierarchy(index_path: str, node: Node, mdl: MdList, keywords: list, cache: Cache):
    for child in node.members:
        if child.kind.is_parent():
            p = MdParagraph([])
            p.append(MdBold([Text(child.get_kind_str())]))
            p.append(Text(' '))
            keywords.append(child.name)
            p.append(MdLink([MdBold([Text(child.name)])], child.url))

            brief = get_brief_description(index_path, child.refid, cache)
            p.extend(brief)

            sublist = MdList([])
            recursive_hierarchy(index_path, child, sublist, keywords, cache)
            p.append(sublist)
            mdl.append(p)

def generate_annotated(index_path: str, output_path: str, root: Node, cache: Cache):
    output_file = os.path.join(output_path, 'annotated.md')
    print('Generating ' + output_file)
    document = MdDocument()
    keywords = []

    # Add title
    document.append(MdHeader(1, [Text('Class List')]))

    # Add description
    document.append(MdParagraph([Text('Here are the classes, structs, unions and interfaces with brief descriptions:')]))

    # Recursively add all members
    mdl = MdList([])
    recursive_hierarchy(index_path, root, mdl, keywords, cache)
    document.append(mdl)

    if not config.noindex:
        document.set_keywords(keywords)
    document.set_title('Annotated')

    # Save
    with open(output_file, 'w+') as f:
        document.render(MdRenderer(f))