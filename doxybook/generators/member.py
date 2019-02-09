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

SECTION_DEFS = {
    'public-type': 'Public Types',
    'protected-type': 'Protected Types',
    'public-func': 'Public Functions',
    'protected-func': 'Protected Functions',
    'public-attrib': 'Public Attributes',
    'protected-attrib': 'Protected Attributes',
    'friend': 'Friends',
    'public-static-type': 'Public Static Types',
    'protected-static-type': 'Protected Static Types',
    'public-static-func': 'Public Static Functions',
    'protected-static-func': 'Protected Static Functions',
    'public-static-attrib': 'Public Static Attributes',
    'protected-static-attrib': 'Protected Static Attributes',
    'enum': 'Enums',
    'typedef': 'Typedefs',
    'var': 'Variables',
    'func': 'Functions',
    'union': 'Unions',
    'related': 'Related',
    'define': 'Defines',
    'interface': 'Interfaces'
}

def generate_brief_row(memberdef: xml.etree.ElementTree.Element, cache: Cache, reimplemented: List[str], ignore: List[str]) -> list:
    typ = MdTableCell([])
    refid = memberdef.get('id')

    if refid in ignore:
        raise Exception('ignored')

    node = cache.get(refid)
    refid_prefix = refid[:-35]
    if refid_prefix.startswith('group_'):
        refid_prefix = refid[:-36]
    name = MdTableCell([MdLink([MdBold([Text(node.name)])], refid_prefix + '.md#' + node.get_anchor_hash())])

    kind = memberdef.get('kind')

    if kind == 'enum':
        typ.append(Text('enum'))
        name.append(Text(' { '))

        is_first = True
        for enumvalue in memberdef.findall('enumvalue'):
            if not is_first:
                name.append(Text(', '))
            is_first = False
            name.append(MdBold([Text(enumvalue.find('name').text)]))
            initializer = enumvalue.find('initializer')
            if initializer is not None:
                name.append(Text(' ' + initializer.text))
        name.append(Text(' } '))

    else:
        if memberdef.get('static') == 'yes':
            typ.append(Text('static '))

        virt = memberdef.get('virt')
        if virt == 'virtual' or virt == 'pure-virtual':
            typ.append(Text('virtual '))

        if kind == 'typedef':
            typ.append(Text('typedef '))

        if kind == 'define':
            typ.append(Text('define '))

        typ.extend(convert_xml_para(memberdef.find('type'), cache))
        
        if kind == 'function':
            name.append(Text(' ('))
            params = memberdef.findall('param')
            argsstring = memberdef.find('argsstring').text
            reimplements = memberdef.find('reimplements')
            if reimplements is not None:
                reimplemented.append(reimplements.get('refid'))

            is_first = True
            for param in params:
                if not is_first:
                    name.append(Text(', '))
                is_first = False

                name.extend(convert_xml_para(param.find('type'), cache))
                n = param.find('declname')
                if n is not None:
                    name.append(Text(' ' + n.text))

                d = param.find('defval')
                if d is not None:
                    name.append(Text(' = '))
                    name.extend(convert_xml_para(d, cache))
            name.append(Text(') ')) 

            # Is deleted?
            if re.search('\\)\\s*=\\s*delete', argsstring):
                name.append(Text('= delete '))

            # Is default?
            if re.search('\\)\\s*=\\s*default', argsstring):
                name.append(Text('= default '))

            # Is noexcept
            if re.search('\\).*noexcept', argsstring):
                name.append(Text('noexcept '))

            # Is override
            if re.search('\\).*override', argsstring):
                name.append(Text('override '))

            # Is const?
            if memberdef.get('const') == 'yes':
                name.append(Text('const '))

            # Is pure?
            if virt == 'pure-virtual':
                name.append(Text('= 0'))

    briefdescription = memberdef.find('briefdescription').findall('para')
    if len(briefdescription) > 0:
        name.append(Text('<br>'))
        for para in briefdescription:
            name.extend(convert_xml_para(para, cache))

    return [typ, name]

def get_text_only(p: xml.etree.ElementTree.Element) -> str:
    ret = ''
    if p is None:
        return ret
    if p.text:
        ret = ret + p.text
    for item in p.getchildren():
        ret = ret + get_text_only(item)
        if item.tail:
            ret = ret + item.tail
    return ret

def make_function_code(compoundname: str, memberdef: xml.etree.ElementTree.Element, is_friend: bool) -> List[str]:
    code = []
    params = memberdef.findall('param')
    argsstring = memberdef.find('argsstring').text
    typ = ''.join(memberdef.find('type').itertext())
    if len(typ) > 0:
        typ += ' '

    prefix = ''
    if memberdef.get('static') == 'yes':
        prefix += 'static '

    if memberdef.get('virt') == 'virtual' or memberdef.get('virt') == 'pure-virtual':
        prefix += 'virtual '

    if memberdef.get('explicit') == 'yes':
        prefix += 'explicit '

    extra = ''

    if memberdef.get('const') == 'yes':
        extra += ' const'

    # Is deleted?
    if argsstring and re.search('\\)\\s*=\\s*delete', argsstring):
        extra += ' = delete'

    # Is default?
    if argsstring and re.search('\\)\\s*=\\s*default', argsstring):
        extra += ' = default'

    # Is noexcept
    if argsstring and re.search('\\).*noexcept', argsstring):
        extra += ' noexcept'

    if memberdef.get('virt') == 'pure-virtual':
        extra += ' = 0'

    name_prefix = ''
    if not name_prefix:
        name_prefix = compoundname + '::'
    if len(params) > 0:
        code.append(prefix + typ + name_prefix + memberdef.find('name').text + ' (')
    else:
        code.append(prefix + typ + name_prefix + memberdef.find('name').text + ' ()' + extra)

    param_index = 0
    for param in params:
        declname = param.find('declname')
        if declname is not None:
            declname = declname.text
        else:
            declname = ''
        defval = param.find('defval')
        if defval is not None:
            defval = ' = ' + get_text_only(defval)
        else:
            defval = ''
        param_index = param_index + 1
        if param_index is not len(params):
            code.append('    ' + get_text_only(param.find('type')) + ' ' + declname + defval + ',')
        else:
            code.append('    ' + get_text_only(param.find('type')) + ' ' + declname + defval)

    if len(params) > 0:
        code.append(')' + extra)

    return code

def find_inherited_classes_recursively(inheritance_compounddefs:List[xml.etree.ElementTree.Element], index_path: str, inheritance_refids: List[str]):
    for refid in inheritance_refids:
        compounddef = xml.etree.ElementTree.parse(os.path.join(index_path, refid + '.xml')).getroot().find('compounddef')
        inheritance_compounddefs.append(compounddef)

        additional_refids:List[str] = []
        for basecompoundref in compounddef.findall('basecompoundref'):
            refid = basecompoundref.get('refid')
            if refid is not None:
                additional_refids.append(basecompoundref.get('refid'))

        find_inherited_classes_recursively(inheritance_compounddefs, index_path, additional_refids)

def make_section(sectiondef: xml.etree.ElementTree.Element, cache: Cache, reimplemented: List[str], ignore: List[str]):
    table = MdTable()
    header = MdTableRow([
        Text('Type'),
        Text('Name')
    ])
    table.append(header)

    member_added = False

    for memberdef in sectiondef.findall('memberdef'):
        try:
            row = MdTableRow(generate_brief_row(memberdef, cache, reimplemented, ignore))
            table.append(row)
            member_added = True
        except:
            pass

    if member_added:
        return table
    return None

def generate_breadcrubs(node: Node):
    ret = []

    breadcrubs = []
    parent = node.parent
    while parent != None:
        #ret.append(MdLink([Text(parent.name)], parent.generate_url()))
        #ret.append(Text(' > '))
        breadcrubs.append(parent)
        parent = parent.parent

    is_first = True
    for parent in reversed(breadcrubs):
        if parent.kind == Kind.ROOT:
            ret.append(MdLink([MdBold([Text('Class List')])], 'annotated.md'))
        else:
            ret.append(MdLink([MdBold([Text(parent.name)])], parent.generate_url()))
        ret.append(Text(' '))
        if is_first:
            is_first = False
            ret.append(MdBold([Text('>')]))
        else:
            ret.append(MdBold([Text('::')]))
        ret.append(Text(' '))

    ret.append(MdLink([MdBold([Text(node.name)])], node.generate_url()))
    ret.append(Br())
    return MdParagraph(ret)

def generate_member(index_path: str, output_path: str, refid: str, cache: Cache):
    output_file = os.path.join(output_path, refid + '.md')
    print('Generating ' + output_file)
    document = MdDocument()
    keywords = []
    node = cache.get(refid)

    # Load XML
    xml_root = xml.etree.ElementTree.parse(os.path.join(index_path, refid + '.xml')).getroot()
    if xml_root is None:
        IndexError('Root xml not found!')
    compounddef = xml_root.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')

    compoundname = compounddef.find('compoundname').text
    keywords.append(compoundname)

    # Add title
    title = compounddef.get('kind') + ' ' + compoundname
    document.append(MdHeader(1, [Text(title)]))

    if node.kind.is_parent():
        document.append(generate_breadcrubs(node))

    if compounddef.get('kind') == 'file':
        document.append(MdParagraph([MdBold([MdLink([Text('Go to the source code of this file.')], refid + '_source.md')])]))  
        document.append(MdParagraph([Text('\n')]))

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

    # Add inheriance
    inheritance_refids:List[str] = []
    basecompoundrefs = compounddef.findall('basecompoundref')
    if len(basecompoundrefs) > 0:
        document.append(Br())
        document.append(Text('Inherits the following classes: '))
        is_first = True
        for basecompoundref in basecompoundrefs:
            refid = basecompoundref.get('refid')

            if not is_first:
                document.append(Text(', '))
            is_first = False

            if refid is not None:
                document.append(MdBold([MdLink([Text(basecompoundref.text)], basecompoundref.get('refid') + '.md')]))
                inheritance_refids.append(basecompoundref.get('refid'))
            else:
                document.append(MdBold([Text(basecompoundref.text)]))
        document.append(Br())

    # Add derivations
    derivedcompoundrefs = compounddef.findall('derivedcompoundref')
    if len(derivedcompoundrefs) > 0:
        document.append(Br())
        document.append(Text('Inherited by the following classes: '))
        is_first = True
        for derivedcompoundref in derivedcompoundrefs:
            refid = derivedcompoundref.get('refid')

            if not is_first:
                document.append(Text(', '))
            is_first = False

            if refid is not None:
                document.append(MdBold([MdLink([Text(derivedcompoundref.text)], derivedcompoundref.get('refid') + '.md')]))
            else:
                document.append(MdBold([Text(derivedcompoundref.text)]))
        document.append(Br())

    # Find all inherited classes
    inheritance_compounddefs:List[xml.etree.ElementTree.Element] = []
    find_inherited_classes_recursively(inheritance_compounddefs, index_path, inheritance_refids)

    # Add inner groups
    innergroups = compounddef.findall('innergroup')
    if len(innergroups) > 0:
        document.append(MdHeader(2, [Text('Modules')]))

        lst = MdList([])

        for innergroup in innergroups:
            refid = innergroup.get('refid')
            innergroup_root = xml.etree.ElementTree.parse(os.path.join(index_path, refid + '.xml')).getroot()
            compound = innergroup_root.find('compounddef')
            name = compound.find('title').text

            briefdescription_paras = compound.find('briefdescription').findall('para')

            link = MdLink([MdBold([Text(name)])], refid + '.md')
            link_with_brief = MdParagraph([link, Text(' ')])
            link_with_brief.extend(generate_paragraph(briefdescription_paras, cache))
            
            lst.append(link_with_brief)

        document.append(lst)
        document.append(Br())

    # Add inner files
    innerfiles = compounddef.findall('innerfile')
    if len(innerfiles) > 0:
        document.append(MdHeader(2, [Text('Files')]))

        table = MdTable()
        header = MdTableRow([
            Text('Type'),
            Text('Name')
        ])
        table.append(header)

        for innerfile in innerfiles:
            refid = innerfile.get('refid')
            name = innerfile.text

            name_cell = MdTableCell([MdLink([MdBold([Text(name)])], refid + '.md')])
            
            try:
                innerfile_root = xml.etree.ElementTree.parse(os.path.join(index_path, refid + '.xml')).getroot()
                compound = innerfile_root.find('compounddef')                
                briefdescription = compound.find('briefdescription').findall('para')
                if len(briefdescription) > 0:
                    name_cell.append(Text(' '))
                    for para in briefdescription:
                        name_cell.extend(convert_xml_para(para, cache))
            except Exception as e:
                pass

            row = MdTableRow([
                Text('file'),
                name_cell
            ])
            table.append(row)

        document.append(table)

    # Add inner classes
    innerclasses = compounddef.findall('innerclass')
    if len(innerclasses) > 0:
        document.append(MdHeader(2, [Text('Classes')]))

        table = MdTable()
        header = MdTableRow([
            Text('Type'),
            Text('Name')
        ])
        table.append(header)

        for innerclass in innerclasses:
            typ = 'class'
            refid = innerclass.get('refid')
            if refid.startswith('struct'):
                typ = 'struct'

            if innerclass.text.startswith(compoundname):
                name = innerclass.text[len(compoundname)+2:]
            else:
                name = innerclass.text
            keywords.append(name)

            name_cell = MdTableCell([MdLink([MdBold([Text(name)])], refid + '.md')])
            
            try:
                innerfile_root = xml.etree.ElementTree.parse(os.path.join(index_path, refid + '.xml')).getroot()
                compound = innerfile_root.find('compounddef')                
                briefdescription = compound.find('briefdescription').findall('para')
                if len(briefdescription) > 0:
                    name_cell.append(Text('<br>'))
                    for para in briefdescription:
                        name_cell.extend(convert_xml_para(para, cache))
            except Exception as e:
                pass

            row = MdTableRow([
                Text(typ),
                name_cell
            ])
            table.append(row)

        document.append(table)

    # We will record which sections to skip
    skip_sections = {}

    # We will also record which functions have been overwritten
    reimplemented = []

    # Add sections
    sectiondefs = compounddef.findall('sectiondef')
    for sectiondef in sectiondefs:
        section_kind = sectiondef.get('kind')

        if section_kind.startswith('private'):
            continue

        document.append(MdHeader(2, [Text(SECTION_DEFS[section_kind])]))

        table = make_section(sectiondef, cache, reimplemented, [])
        document.append(table)

        for memberdef in sectiondef.findall('memberdef'):
            name = memberdef.find('name')
            if name is not None and name.text is not None:
                keywords.append(name.text)

        # Find inherited stuff
        for inheritance_compounddefs in inheritance_compounddefs:
            inherited_sectiondefs = inheritance_compounddefs.findall('sectiondef')
            refid = inheritance_compounddefs.get('id')
            for sec in inherited_sectiondefs:
                if sec.get('kind') == skip_sections:
                    inherited_name = inheritance_compounddefs.find('compoundname').text

                    tmp = []
                    table = make_section(sec, cache, tmp, reimplemented)
                    if table is not None:
                        document.append(MdHeader(4, [Text(SECTION_DEFS[skip_sections] + ' inherited from '), MdLink([Text(inherited_name)], refid + '.md')]))
                        document.append(table)
                    reimplemented.extend(tmp)

                    for memberdef in sec.findall('memberdef'):
                        name = memberdef.find('name')
                        if name is not None and name.text is not None:
                            keywords.append(name.text)

                    if not refid in skip_sections:
                        skip_sections[refid] = [skip_sections]
                    else:
                        skip_sections[refid].append(skip_sections)

    missing_sections = {}

    # Calculate if we need to create "Additional Inherited Members" section
    for inheritance_compounddef in inheritance_compounddefs:
        refid = inheritance_compounddef.get('id')
        inherited_sectiondefs = inheritance_compounddef.findall('sectiondef')
        for sec in inherited_sectiondefs:
            section_kind = sec.get('kind')
            
            if not section_kind or section_kind.startswith('private') or section_kind not in SECTION_DEFS:
                continue

            if refid in skip_sections:
                if not section_kind in skip_sections[refid]:
                    if not refid in missing_sections:
                        missing_sections[refid] = [section_kind]
                    else:
                        missing_sections[refid].append(section_kind)
            else:
                if not refid in missing_sections:
                    missing_sections[refid] = [section_kind]
                else:
                    missing_sections[refid].append(section_kind)

    if missing_sections:
        document.append(MdHeader(2, [Text('Additional Inherited Members')]))
        for inheritance_compounddef in inheritance_compounddefs:
            refid = inheritance_compounddef.get('id')
            if refid in missing_sections:
                inherited_sectiondefs = inheritance_compounddef.findall('sectiondef')
                for sec in inherited_sectiondefs:
                    section_kind = sec.get('kind')

                    if not section_kind or section_kind.startswith('private') or section_kind not in SECTION_DEFS:
                        continue

                    if section_kind in missing_sections[refid]:
                        inherited_name = inheritance_compounddef.find('compoundname').text

                        tmp = []
                        table = make_section(sec, cache, tmp, reimplemented)
                        if table is not None:
                            document.append(MdHeader(4, [Text(SECTION_DEFS[section_kind] + ' inherited from '), MdLink([Text(inherited_name)], refid + '.md')]))
                            document.append(table)
                        reimplemented.extend(tmp)

    # Add detailed description
    if len(detaileddescription_paras) > 0:
        document.append(MdHeader(2, [Text('Detailed Description')]))
        document.extend(generate_paragraph(compounddef.find('detaileddescription').findall('para'), cache))

    # Add detailed sections
    sectiondefs = compounddef.findall('sectiondef')
    for sectiondef in sectiondefs:
        section_kind = sectiondef.get('kind')
        if section_kind.startswith('private'):
            continue
            
        document.append(MdHeader(2, [Text(SECTION_DEFS[section_kind] + ' Documentation')]))

        memberdefs = sectiondef.findall('memberdef')

        for memberdef in memberdefs:
            kind = memberdef.get('kind')
            refid = memberdef.get('id')
            node = None
            try:
                node = cache.get(refid)
            except:
                pass
            name = memberdef.find('name').text
            
            if config.target == 'gitbook':
                if node is not None and node.overloaded:
                    document.append(MdHeader(3, [Text(kind + ' <a id=\"' + refid[-34:] + '\" href=\"#' + refid[-34:] + '\">' + name + ' (' + str(node.overload_num) + '/' + str(node.overload_total) + ')</a>')]))
                else:
                    document.append(MdHeader(3, [Text(kind + ' <a id=\"' + refid[-34:] + '\" href=\"#' + refid[-34:] + '\">' + name + '</a>')]))
            else:
                if node is not None and node.overloaded:
                    document.append(MdHeader(3, [Text(kind + ' ' + name + ' (' + str(node.overload_num) + '/' + str(node.overload_total) + ')')]))
                else:
                    document.append(MdHeader(3, [Text(kind + ' ' + name)]))

            code = []
            if kind == 'function':
                code.extend(make_function_code(compoundname, memberdef, False))

            elif kind == 'friend':
                argsstring = memberdef.find('argsstring')
                if argsstring is not None and argsstring.text is not None and len(argsstring.text) > 0:
                    code.extend(make_function_code(compoundname, memberdef, True))
                else:
                    code.append(memberdef.find('definition').text + ';')

            elif kind == 'enum':
                code.append('enum ' + compoundname + '::' + memberdef.find('name').text + ' {')
                for enumvalue in memberdef.findall('enumvalue'):
                    value = enumvalue.find('name').text
                    initializer = enumvalue.find('initializer')
                    if initializer is not None:
                        value += ' ' + initializer.text
                    code.append('    ' + value + ',')
                code.append('};')

            elif kind == 'define':
                initializer = memberdef.find('initializer')
                if initializer is not None:
                    code.append(memberdef.get('kind') + ' ' + memberdef.find('name').text + ' ' + initializer.text + ';')
                else:
                    code.append(memberdef.get('kind') + ' ' + memberdef.find('name').text + ';')

            else:
                definition = memberdef.find('definition')
                if definition is None:
                    code.append(memberdef.get('kind') + ' ' + memberdef.find('name').text + ';')
                else:
                    code.append(definition.text + ';')

            document.append(MdCodeBlock(code))

            # Add descriptions
            inbodydescription_paras = memberdef.find('inbodydescription').findall('para')
            detaileddescription_paras = memberdef.find('detaileddescription').findall('para')
            briefdescription_paras = memberdef.find('briefdescription').findall('para')
            document.extend(generate_paragraph(briefdescription_paras, cache))
            document.append(Text('\n'))
            document.extend(generate_paragraph(detaileddescription_paras, cache))
            document.append(Text('\n'))
            for para in inbodydescription_paras:
                document.extend(generate_paragraph([para], cache))
                document.append(Text('\n'))

            # Add overrides
            reimplements = memberdef.find('reimplements')
            if reimplements is not None:
                try:
                    found = cache.get(reimplements.get('refid'))
                    document.append(MdParagraph([Text('Implements '), MdBold([MdLink([Text(found.get_full_name())], found.url)])]))
                    document.append(Br())
                except:
                    pass
    # Add location
    location = compounddef.find('location')
    if location is not None:
        document.append(Text('\n'))
        document.append(MdLine())
        document.append(MdParagraph([
            Text('The documentation for this class was generated from the following file: '), 
            MdCode([Text(location.get('file'))])
        ]))

    # Save
    if not config.noindex:
        document.set_keywords(keywords)
    document.set_title(title)

    with open(output_file, 'w+') as f:
        document.render(MdRenderer(f))

