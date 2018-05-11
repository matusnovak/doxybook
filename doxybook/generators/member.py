import os
import re
import xml.etree.ElementTree
from typing import List

from doxybook.markdown import Md, MdDocument, MdCode, MdCodeBlock, MdBold, MdItalic, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine, MdTable, MdTableRow, MdTableCell, Text, Br
from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.cache import Cache
from doxybook.generators.paragraph import generateParagraph, convertXmlPara

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
    'define': 'Defines'
}

def generateBriefRow(memberdef: xml.etree.ElementTree.Element, cache: Cache, reimplemented: List[str], ignore: List[str]) -> list:
    typ = MdTableCell([])
    refid = memberdef.get('id')

    if refid in ignore:
        raise Exception('ignored')

    name = MdTableCell([MdLink([MdBold([Text(memberdef.find('name').text)])], refid[:-35] + '.md#' + refid[-34:])])

    kind = memberdef.get('kind')

    if kind == 'enum':
        typ.append(Text('enum'))
        name.append(Text(' { '))

        isFirst = True
        for enumvalue in memberdef.findall('enumvalue'):
            if not isFirst:
                name.append(Text(', '))
            isFirst = False
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

        typ.extend(convertXmlPara(memberdef.find('type'), cache))
        
        if kind == 'function':
            name.append(Text(' ('))
            params = memberdef.findall('param')
            argsstring = memberdef.find('argsstring').text
            reimplements = memberdef.find('reimplements')
            if reimplements is not None:
                reimplemented.append(reimplements.get('refid'))

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
            name.extend(convertXmlPara(para, cache))

    return [typ, name]

def getTextOnly(p: xml.etree.ElementTree.Element) -> str:
    ret = ''
    if p is None:
        return ret
    if p.text:
        ret = ret + p.text
    for item in p.getchildren():
        ret = ret + getTextOnly(item)
        if item.tail:
            ret = ret + item.tail
    return ret

def makeFunctionCode(compoundname: str, memberdef: xml.etree.ElementTree.Element, isFriend: bool) -> List[str]:
    code = []
    params = memberdef.findall('param')
    argsstring = memberdef.find('argsstring').text
    typ = getTextOnly(memberdef.find('type'))
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

    namePrefix = ''
    if not isFriend:
        namePrefix = compoundname + '::'
    if len(params) > 0:
        code.append(prefix + typ + namePrefix + memberdef.find('name').text + ' (')
    else:
        code.append(prefix + typ + namePrefix + memberdef.find('name').text + ' ()' + extra)

    paramIndex = 0
    for param in params:
        declname = param.find('declname')
        if declname is not None:
            declname = declname.text
        else:
            declname = ''
        defval = param.find('defval')
        if defval is not None:
            defval = ' = ' + getTextOnly(defval)
        else:
            defval = ''
        paramIndex = paramIndex + 1
        if paramIndex is not len(params):
            code.append('    ' + getTextOnly(param.find('type')) + ' ' + declname + defval + ',')
        else:
            code.append('    ' + getTextOnly(param.find('type')) + ' ' + declname + defval)

    if len(params) > 0:
        code.append(')' + extra)

    return code

def findInheritedClassesRecursively(inheritanceCompounddefs:List[xml.etree.ElementTree.Element], indexDir: str, inheritanceRefids: List[str]):
    for refid in inheritanceRefids:
        compounddef = xml.etree.ElementTree.parse(os.path.join(indexDir, refid + '.xml')).getroot().find('compounddef')
        inheritanceCompounddefs.append(compounddef)

        additionalRefids:List[str] = []
        for basecompoundref in compounddef.findall('basecompoundref'):
            refid = basecompoundref.get('refid')
            if refid is not None:
                additionalRefids.append(basecompoundref.get('refid'))

        findInheritedClassesRecursively(inheritanceCompounddefs, indexDir, additionalRefids)

def makeSection(sectiondef: xml.etree.ElementTree.Element, cache: Cache, reimplemented: List[str], ignore: List[str]):
    table = MdTable()
    header = MdTableRow([
        Text('Type'),
        Text('Name')
    ])
    table.append(header)

    memberAdded = False

    for memberdef in sectiondef.findall('memberdef'):
        try:
            row = MdTableRow(generateBriefRow(memberdef, cache, reimplemented, ignore))
            table.append(row)
            memberAdded = True
        except:
            pass

    if memberAdded:
        return table
    return None

def generateMember(indexDir: str, outputDir: str, refid: str, cache: Cache, noindex: bool):
    outputFile = os.path.join(outputDir, refid + '.md')
    print('Generating ' + outputFile)
    document = MdDocument()
    keywords = []

    # Load XML
    xmlRoot = xml.etree.ElementTree.parse(os.path.join(indexDir, refid + '.xml')).getroot()
    if xmlRoot is None:
        IndexError('Root xml not found!')
    compounddef = xmlRoot.find('compounddef')
    if compounddef is None:
        IndexError('compounddef not found in xml!')

    compoundname = compounddef.find('compoundname').text
    keywords.append(compoundname)

    # Add title
    document.append(MdHeader(1, [Text(compounddef.get('kind') + ' ' + compoundname)]))

    if compounddef.get('kind') == 'file':
        document.append(MdParagraph([MdBold([MdLink([Text('Go to the source code of this file.')], refid + '_source.md')])]))  

    # Add brief description
    detaileddescriptionParas = compounddef.find('detaileddescription').findall('para')
    briefdescriptionParas = compounddef.find('briefdescription').findall('para')

    if len(briefdescriptionParas) > 0:
        p = MdParagraph([])
        for para in briefdescriptionParas:
            p.extend(convertXmlPara(para, cache))
        if len(detaileddescriptionParas) > 0:
            p.append(MdLink([Text('More...')], '#detailed-description'))
        document.append(p)

    # Add inheriance
    inheritanceRefids:List[str] = []
    basecompoundrefs = compounddef.findall('basecompoundref')
    if len(basecompoundrefs) > 0:
        document.append(Br())
        document.append(Text('Inherits the following classes: '))
        isFirst = True
        for basecompoundref in basecompoundrefs:
            refid = basecompoundref.get('refid')

            if not isFirst:
                document.append(Text(', '))
            isFirst = False

            if refid is not None:
                document.append(MdBold([MdLink([Text(basecompoundref.text)], basecompoundref.get('refid') + '.md')]))
                inheritanceRefids.append(basecompoundref.get('refid'))
            else:
                document.append(MdBold([Text(basecompoundref.text)]))
        document.append(Br())

    # Add derivations
    derivedcompoundrefs = compounddef.findall('derivedcompoundref')
    if len(derivedcompoundrefs) > 0:
        document.append(Br())
        document.append(Text('Inherited by the following classes: '))
        isFirst = True
        for derivedcompoundref in derivedcompoundrefs:
            refid = derivedcompoundref.get('refid')

            if not isFirst:
                document.append(Text(', '))
            isFirst = False

            if refid is not None:
                document.append(MdBold([MdLink([Text(derivedcompoundref.text)], derivedcompoundref.get('refid') + '.md')]))
            else:
                document.append(MdBold([Text(derivedcompoundref.text)]))
        document.append(Br())

    # Find all inherited classes
    inheritanceCompounddefs:List[xml.etree.ElementTree.Element] = []
    findInheritedClassesRecursively(inheritanceCompounddefs, indexDir, inheritanceRefids)
    #for refid in inheritanceRefids:
    #    inheritanceCompounddefs.append(xml.etree.ElementTree.parse(os.path.join(indexDir, refid + '.xml')).getroot().find('compounddef'))
    
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

            row = MdTableRow([
                Text(typ),
                MdLink([MdBold([Text(name)])], refid + '.md')
            ])
            table.append(row)

        document.append(table)

    # We will record which sections to skip
    skipSections = {}

    # We will also record which functions have been overwritten
    reimplemented = []

    # Add sections
    sectiondefs = compounddef.findall('sectiondef')
    for sectiondef in sectiondefs:
        sectionKind = sectiondef.get('kind')

        if sectionKind.startswith('private'):
            continue

        document.append(MdHeader(2, [Text(SECTION_DEFS[sectionKind])]))

        table = makeSection(sectiondef, cache, reimplemented, [])
        document.append(table)

        for memberdef in sectiondef.findall('memberdef'):
            name = memberdef.find('name')
            if name is not None and name.text is not None:
                keywords.append(name.text)

        # Find inherited stuff
        for inheritanceCompounddef in inheritanceCompounddefs:
            inheritedSectiondefs = inheritanceCompounddef.findall('sectiondef')
            refid = inheritanceCompounddef.get('id')
            for sec in inheritedSectiondefs:
                if sec.get('kind') == sectionKind:
                    inheritedName = inheritanceCompounddef.find('compoundname').text

                    tmp = []
                    table = makeSection(sec, cache, tmp, reimplemented)
                    if table is not None:
                        document.append(MdHeader(4, [Text(SECTION_DEFS[sectionKind] + ' inherited from '), MdLink([Text(inheritedName)], refid + '.md')]))
                        document.append(table)
                    reimplemented.extend(tmp)

                    for memberdef in sec.findall('memberdef'):
                        name = memberdef.find('name')
                        if name is not None and name.text is not None:
                            keywords.append(name.text)

                    if not refid in skipSections:
                        skipSections[refid] = [sectionKind]
                    else:
                        skipSections[refid].append(sectionKind)

    missingSections = {}

    # Calculate if we need to create "Additional Inherited Members" section
    for inheritanceCompounddef in inheritanceCompounddefs:
        refid = inheritanceCompounddef.get('id')
        inheritedSectiondefs = inheritanceCompounddef.findall('sectiondef')
        for sec in inheritedSectiondefs:
            sectionKind = sec.get('kind')
            
            if sectionKind.startswith('private'):
                continue

            if refid in skipSections:
                if not sectionKind in skipSections[refid]:
                    if not refid in missingSections:
                        missingSections[refid] = [sectionKind]
                    else:
                        missingSections[refid].append(sectionKind)
            else:
                if not refid in missingSections:
                    missingSections[refid] = [sectionKind]
                else:
                    missingSections[refid].append(sectionKind)

    if missingSections:
        document.append(MdHeader(2, [Text('Additional Inherited Members')]))
        for inheritanceCompounddef in inheritanceCompounddefs:
            refid = inheritanceCompounddef.get('id')
            if refid in missingSections:
                inheritedSectiondefs = inheritanceCompounddef.findall('sectiondef')
                for sec in inheritedSectiondefs:
                    sectionKind = sec.get('kind')

                    if sectionKind.startswith('private'):
                        continue

                    if sectionKind in missingSections[refid]:
                        inheritedName = inheritanceCompounddef.find('compoundname').text

                        tmp = []
                        table = makeSection(sec, cache, tmp, reimplemented)
                        if table is not None:
                            document.append(MdHeader(4, [Text(SECTION_DEFS[sectionKind] + ' inherited from '), MdLink([Text(inheritedName)], refid + '.md')]))
                            document.append(table)
                        reimplemented.extend(tmp)

    # Add detailed description
    if len(detaileddescriptionParas) > 0:
        document.append(MdHeader(2, [Text('Detailed Description')]))
        document.extend(generateParagraph(compounddef.find('detaileddescription').findall('para'), cache))

    # Add detailed sections
    sectiondefs = compounddef.findall('sectiondef')
    for sectiondef in sectiondefs:
        sectionKind = sectiondef.get('kind')
        if sectionKind.startswith('private'):
            continue
            
        document.append(MdHeader(2, [Text(SECTION_DEFS[sectionKind] + ' Documentation')]))

        for memberdef in sectiondef.findall('memberdef'):
            kind = memberdef.get('kind')
            document.append(MdHeader(3, [Text(kind + ' <a id=\"' + memberdef.get('id')[-34:] + '\" href=\"#' + memberdef.get('id')[-34:] + '\">' + memberdef.find('name').text + '</a>')]))

            code = []
            if kind == 'function':
                code.extend(makeFunctionCode(compoundname, memberdef, False))

            elif kind == 'friend':
                argsstring = memberdef.find('argsstring')
                if argsstring is not None and argsstring.text is not None and len(argsstring.text) > 0:
                    code.extend(makeFunctionCode(compoundname, memberdef, True))
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

            else:
                definition = memberdef.find('definition')
                if definition is None:
                    code.append(memberdef.get('kind') + ' ' + memberdef.find('name').text + ';')
                else:
                    code.append(definition.text + ';')

            document.append(MdCodeBlock(code))
                
            # Add overrides
            reimplements = memberdef.find('reimplements')
            if reimplements is not None:
                try:
                    found = cache.get(reimplements.get('refid'))
                    document.append(MdParagraph([Text('Overrides '), MdBold([MdLink([Text(found.getFullName())], found.url)])]))
                except:
                    pass

            # Add descriptions
            detaileddescriptionParas = memberdef.find('detaileddescription').findall('para')
            briefdescriptionParas = memberdef.find('briefdescription').findall('para')
            document.extend(generateParagraph(briefdescriptionParas, cache))
            document.append(Text('\n'))
            document.extend(generateParagraph(detaileddescriptionParas, cache))
            document.append(Text('\n'))


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
    if not noindex:
        document.setKeywords(keywords)
    with open(outputFile, 'w+') as f:
        document.render(MdRenderer(f))

