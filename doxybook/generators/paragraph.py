from typing import List
import xml.etree.ElementTree

from doxybook.markdown import MdParagraph, MdTable, MdCode, MdTableRow, MdCodeBlock, MdTableCell, MdHeader, MdImage, MdList, MdBlockQuote, MdLink, MdBold, MdItalic, MdHint, Text, Br
from doxybook.cache import Cache
from doxybook.config import config
from doxybook.utils import lookahead

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

SIMPLE_SECTIONS_HINTS_VUEPRESS = {
    'note': 'tip',
    'bug': 'danger',
    'warning': 'warning'
}

def convert_xml_para(p: xml.etree.ElementTree.Element, cache: Cache) -> list:
    ret = []
    if p is None:
        return ret
    if p.text:
        ret.append(Text(p.text))
    for item in p.getchildren():
        # para
        if item.tag == 'para':
            ret.append(MdParagraph(convert_xml_para(item, cache)))
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
            got_lang = False
            code = MdCodeBlock([])
            for codeline in item.findall('codeline'):
                line = ''
                for highlight in codeline.findall('highlight'):
                    if not got_lang and len(highlight.getchildren()) == 0 and highlight.text is not None and highlight.text.startswith('{') and highlight.text.endswith('}'):
                        lang = highlight.text[1:-1]
                        code.set_lang(lang)
                        got_lang = True
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
                        r.append(MdTableCell(convert_xml_para(para, cache)))
                t.append(r)
            ret.append(t)

        # blockquote
        elif item.tag == 'blockquote':
            b = MdBlockQuote([])
            for para in item.findall('para'):
                b.extend(convert_xml_para(para, cache))
            ret.append(b)

        # heading
        elif item.tag == 'heading':
            ret.append(MdHeader(int(item.get('level')), convert_xml_para(item, cache)))

        # orderedlist
        elif item.tag == 'orderedlist' or item.tag == 'itemizedlist':
            lst = MdList([])
            for listitem in item.findall('listitem'):
                i = MdParagraph([])
                for para in listitem.findall('para'):
                    i.extend(convert_xml_para(para, cache))
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
                    ret.append(MdBold([MdLink([Text(ref.get_full_name())], ref.url)]))
            except:
                pass

        # sect1:
        elif item.tag == 'sect1':
            title = item.find('title').text
            ret.append(MdHeader(2, [Text(title)]))
            ret.extend(convert_xml_para(item, cache))

        # sect2:
        elif item.tag == 'sect2':
            title = item.find('title').text
            ret.append(MdHeader(3, [Text(title)]))
            ret.extend(convert_xml_para(item, cache))

        # variablelist
        elif item.tag == 'variablelist':
            varlistentry = item.find('varlistentry')
            
            ret.append(MdHeader(4, convert_xml_para(varlistentry.find('term'), cache)))

            term = varlistentry.find('term')
            for listitem in item.findall('listitem'):
                for para in listitem.findall('para'):
                    ret.append(MdParagraph(convert_xml_para(para, cache)))

        # parameterlist
        elif item.tag == 'parameterlist':
            parameteritems = item.findall('parameteritem')
            lst = MdList([])
            for parameteritem in parameteritems:
                name = parameteritem.find('parameternamelist').find('parametername')
                description = parameteritem.find('parameterdescription').findall('para')
                par = MdParagraph([])
                par.append(MdBold(convert_xml_para(name, cache)))
                par.append(Text(' '))
                for ip in description:
                    par.extend(convert_xml_para(ip, cache))
                lst.append(par)
            ret.append(Br())
            ret.append(MdBold([Text(SIMPLE_SECTIONS[item.get('kind')])]))
            ret.append(Br())
            ret.append(lst)

        # simplesect
        elif item.tag == 'simplesect':
            kind = item.get('kind')
            if config.target == 'vuepress' and kind in SIMPLE_SECTIONS_HINTS_VUEPRESS:
                ret.append(Br())
                children = []
                for sp in item.findall('para'):
                    children.extend(convert_xml_para(sp, cache))
                    children.append(Br())
                ret.append(MdHint(children, SIMPLE_SECTIONS_HINTS_VUEPRESS[kind], SIMPLE_SECTIONS[kind]))

            else:
                ret.append(Br())
                ret.append(MdBold([Text(SIMPLE_SECTIONS[kind])]))
                if kind != 'see':
                    ret.append(Br())
                else:
                    ret.append(Text(' '))

                for sp, has_more in lookahead(item.findall('para')):
                    ret.extend(convert_xml_para(sp, cache))
                    if kind == 'see':
                        if has_more:
                            ret.append(Text(', '))
                    else:
                        ret.append(Br())

        # xrefsect
        elif item.tag == 'xrefsect':
            xreftitle = item.find('xreftitle')
            xrefdescription = item.find('xrefdescription')
            kind = xreftitle.text.lower()
            if config.target == 'vuepress' and kind in SIMPLE_SECTIONS_HINTS_VUEPRESS:
                children = []
                for sp in xrefdescription.findall('para'):
                    children.extend(convert_xml_para(sp, cache))
                    children.append(Br())
                ret.append(MdHint(children, SIMPLE_SECTIONS_HINTS_VUEPRESS[kind], SIMPLE_SECTIONS[kind]))
            else:
                ret.append(Br())
                ret.append(MdBold(convert_xml_para(xreftitle, cache)))
                ret.append(Br())
                for sp in xrefdescription.findall('para'):
                    ret.extend(convert_xml_para(sp, cache))
                    ret.append(Br())

        # Hard link
        elif item.tag == 'ulink':
            ret.append(MdLink(convert_xml_para(item, cache), item.get('url')))

        # Bold
        elif item.tag == 'bold':
            ret.append(MdBold(convert_xml_para(item, cache)))

        # Emphasis
        elif item.tag == 'emphasis':
            ret.append(MdItalic(convert_xml_para(item, cache)))

        # End of the item text
        if item.tail:
            ret.append(Text(item.tail))
    return ret

def generate_paragraph(paras: List[xml.etree.ElementTree.Element], cache: Cache) -> List[MdParagraph]:
    ret = []
    for para in paras:
        ret.append(MdParagraph(convert_xml_para(para, cache)))
    return ret