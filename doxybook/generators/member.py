import os
import xml.etree.ElementTree

from doxybook.markdown import Md, MdDocument, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.generators.paragraph import generateParagraph, convertXmlPara

SECTION_DEFS = {
    'public-type': 'Public Types',
    'protected-type': 'Protected Types',
    'private-type': 'Private Types',
    'public-func': 'Public Functions',
    'protected-func': 'Protected Functions',
    'private-func': 'Private Functions',
    'public-attrib': 'Public Attributes',
    'protected-attrib': 'Protected Attributes',
    'private-attrib': 'Private Attributes',
    'friend': 'Friends',
    'public-static-type': 'Public Static Types',
    'protected-static-type': 'Protected Static Types',
    'private-static-type': 'Private Static Types',
    'public-static-func': 'Public Static Functions',
    'protected-static-func': 'Protected Static Functions',
    'private-static-func': 'Private Static Functions',
    'public-static-attrib': 'Public Static Attributes',
    'protected-static-attrib': 'Protected Static Attributes',
    'private-static-attrib': 'Private Static Attributes',
    'enum': 'Enums',
    'typedef': 'Typedefs',
    'var': 'Variables',
    'func': 'Functions',
    'union': 'Unions',
    'related': 'Related'
}

def generateBriefRow(memberdef: xml.etree.ElementTree.Element, cache: Cache) -> list:
    typ = MdTableCell([])
    name = MdTableCell([MdLink([MdBold([Text(memberdef.find('name').text)])], '#' + memberdef.get('id')[-34:])])

    kind = memberdef.get('kind')

    if kind == 'enum':
        typ.append(Text('enum'))
        name.append(Text(' { '))
        for enumvalue in memberdef.findall('enumvalue'):
            name.append(MdBold([Text(enumvalue.find('name').text)]))
            name.append(Text(', '))
        name.append(Text(' } '))
    else:
        if memberdef.get('static') == 'yes':
            typ.append(Text('static '))
        typ.extend(convertXmlPara(memberdef.find('type'), cache))

        
        if kind == 'function':
            name.append(Text(' ('))
            params = memberdef.findall('param')

            isFirst = True
            for param in params:
                if not isFirst:
                    name.append(Text(', '))
                isFirst = False

                name.extend(convertXmlPara(param.find('type'), cache))
                n = param.find('declname')
                if n is not None:
                    name.append(Text(' ' + n.text))

                d = param.find('defval')
                if d is not None:
                    name.append(Text(' = '))
                    name.extend(convertXmlPara(d, cache))
            name.append(Text(')')) 

    return [typ, name]

def generateMember(indexDir: str, outputDir: str, node: Node, cache: Cache):
    outputFile = os.path.join(outputDir, node.url)
    print('Generating ' + outputFile)
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [Text(node.name + ' ' + node.kind.value + ' Reference')]))

    # Load XML
    xmlRoot = xml.etree.ElementTree.parse(os.path.join(indexDir, node.refid + '.xml')).getroot()
    if xmlRoot is None:
        IndexError('Root xml not found!')
    compounddef = xmlRoot.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')

    # Add brief description
    document.extend(generateParagraph(compounddef.find('briefdescription').findall('para'), cache))

    # Sections
    sectiondefs = compounddef.findall('sectiondef')
    for sectiondef in sectiondefs:
        document.append(MdHeader(2, [Text(SECTION_DEFS[sectiondef.get('kind')])]))

        table = MdTable()
        header = MdTableRow([
            Text('Type'),
            Text('Name')
        ])
        table.append(header)

        for memberdef in sectiondef.findall('memberdef'):
            row = MdTableRow(generateBriefRow(memberdef, cache))
            table.append(row)

        document.append(table)

    # Add detailed description
    document.append(MdHeader(2, [Text('Detailed Description')]))
    document.extend(generateParagraph(compounddef.find('detaileddescription').findall('para'), cache))

    location = compounddef.find('location')
    if location is not None:
        document.append(MdLine())
        document.append(MdParagraph([
            Text('The documentation for this class was generated from the following file: '), 
            MdLink([Text(location.get('file'))], 'file.md')
        ]))

    # Save
    os.makedirs(outputDir, exist_ok=True)
    with open(outputFile, 'w+') as f:
        document.render(MdRenderer(f))

