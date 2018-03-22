from typing import List
import xml.etree.ElementTree

from doxybook.markdown import MdParagraph, MdTable, MdCode, MdTableRow, MdCodeBlock, MdTableCell, MdHeader, MdImage, MdList, MdBlockQuote, MdLink, MdBold, MdItalic, Text, Br
from doxybook.cache import Cache

SIMPLE_SECTIONS = {
    'see': 'See also:',
    'note': 'Note:',
    'bug': 'Bug:',
    'warning': 'Warning:',
    'return': 'Returns:',
    'returns': 'Returns:',
    'param': 'Parameters:',
    'templateparam': 'Template parameters:',
    'retval': 'Return value:',
    'author': 'Author:',
    'authors': 'Authors:',
    'since': 'Since:',
    'pre': 'Precondition:',
    'remark': 'Remark:',
    'copyright': 'Copyright',
    'post': 'Post',
    'rcs': 'Rcs',
    'attention': 'Attention:',
    'invariant': 'Invariant:',
    'exception': 'Exception:',
    'date': 'Date:'
}

def convertXmlPara(p: xml.etree.ElementTree.Element, cache: Cache) -> list:
    ret = []
    if p is None:
        return ret
    if p.text:
        ret.append(Text(p.text))
    for item in p.getchildren():
        # para
        if item.tag == 'para':
            ret.append(MdParagraph(convertXmlPara(item, cache)))
            ret.append(Text('\n'))

        # image
        elif item.tag == 'image':
            url = item.get('name')
            ret.append(MdImage(url))

        # computeroutput
        elif item.tag == 'computeroutput':
            ret.append(MdCode([Text(item.text)]))

        # programlisting
        elif item.tag == 'programlisting':
            gotLang = False
            code = MdCodeBlock([])
            for codeline in item.findall('codeline'):
                line = ''
                for highlight in codeline.findall('highlight'):
                    if not gotLang and len(highlight.getchildren()) == 0 and highlight.text is not None and highlight.text.startswith('{') and highlight.text.endswith('}'):
                        lang = highlight.text[1:-1]
                        code.setLang(lang)
                        gotLang = True
                        continue
                    else:
                        if highlight.text is not None:
                            line += highlight.text
                        for c in highlight.getchildren():
                            if c.tag == 'sp':
                                line += ' '
                            if c.text:
                                line += c.text
                            if c.tail:
                                line += c.tail
                code.append(line)
            ret.append(Text('\n'))
            ret.append(code)

        # table
        elif item.tag == 'table':
            t = MdTable()
            for row in item.findall('row'):
                r = MdTableRow([])
                for cell in row.findall('entry'):
                    for para in cell.findall('para'):
                        r.append(MdTableCell(convertXmlPara(para, cache)))
                t.append(r)
            ret.append(t)

        # blockquote
        elif item.tag == 'blockquote':
            b = MdBlockQuote([])
            for para in item.findall('para'):
                b.extend(convertXmlPara(para, cache))
            ret.append(b)

        # heading
        elif item.tag == 'heading':
            ret.append(MdHeader(int(item.get('level')), convertXmlPara(item, cache)))

        # orderedlist
        elif item.tag == 'orderedlist' or item.tag == 'itemizedlist':
            lst = MdList([])
            for listitem in item.findall('listitem'):
                i = MdParagraph([])
                for para in listitem.findall('para'):
                    i.extend(convertXmlPara(para, cache))
                lst.append(i)
            ret.append(lst)

        # Reference
        elif item.tag == 'ref':
            refid = item.get('refid')
            try:
                ref = cache.get(refid)
                if item.text:
                    ret.append(MdBold([MdLink([Text(item.text)], ref.url)]))
                else:
                    ret.append(MdBold([MdLink([Text(ref.getFullName())], ref.url)]))
            except:
                pass

        # sect1:
        elif item.tag == 'sect1':
            title = item.find('title').text
            ret.append(MdHeader(2, [Text(title)]))
            ret.extend(convertXmlPara(item, cache))

        # sect2:
        elif item.tag == 'sect2':
            title = item.find('title').text
            ret.append(MdHeader(3, [Text(title)]))
            ret.extend(convertXmlPara(item, cache))

        # variablelist
        elif item.tag == 'variablelist':
            varlistentry = item.find('varlistentry')
            
            ret.append(MdHeader(4, convertXmlPara(varlistentry.find('term'), cache)))

            term = varlistentry.find('term')
            for listitem in item.findall('listitem'):
                for para in listitem.findall('para'):
                    ret.append(MdParagraph(convertXmlPara(para, cache)))

        # parameterlist
        elif item.tag == 'parameterlist':
            parameteritems = item.findall('parameteritem')
            lst = MdList([])
            for parameteritem in parameteritems:
                name = parameteritem.find('parameternamelist').find('parametername')
                description = parameteritem.find('parameterdescription').findall('para')
                par = MdParagraph([])
                par.append(MdItalic(convertXmlPara(name, cache)))
                par.append(Text(' '))
                for ip in description:
                    par.extend(convertXmlPara(ip, cache))
                lst.append(par)
            ret.append(Br())
            ret.append(MdBold([Text(SIMPLE_SECTIONS[item.get('kind')])]))
            ret.append(Br())
            ret.append(lst)

        # simplesect
        elif item.tag == 'simplesect':
            ret.append(Br())
            ret.append(MdBold([Text(SIMPLE_SECTIONS[item.get('kind')])]))
            ret.append(Br())
            for sp in item.findall('para'):
                ret.extend(convertXmlPara(sp, cache))
                ret.append(Br())

        # xrefsect
        elif item.tag == 'xrefsect':
            xreftitle = item.find('xreftitle')
            xrefdescription = item.find('xrefdescription')
            ret.append(Br())
            ret.append(MdBold(convertXmlPara(xreftitle, cache)))
            ret.append(Br())
            for sp in xrefdescription.findall('para'):
                ret.extend(convertXmlPara(sp, cache))
                ret.append(Br())

        # Hard link
        elif item.tag == 'ulink':
            ret.append(MdLink(convertXmlPara(item, cache), item.get('url')))

        # Bold
        elif item.tag == 'bold':
            ret.append(MdBold(convertXmlPara(item, cache)))

        # Emphasis
        elif item.tag == 'emphasis':
            ret.append(MdItalic(convertXmlPara(item, cache)))

        # End of the item text
        if item.tail:
            ret.append(Text(item.tail))
    return ret

def generateParagraph(paras: List[xml.etree.ElementTree.Element], cache: Cache) -> List[MdParagraph]:
    ret = []
    for para in paras:
        ret.append(MdParagraph(convertXmlPara(para, cache)))
    return ret