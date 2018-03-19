from typing import List
import xml.etree.ElementTree

from doxybook.markdown import MdParagraph, MdLink, MdBold, MdItalic, Text, Br
from doxybook.cache import Cache

SIMPLE_SECTIONS = {
    'see': 'See also'
}

def convertXmlPara(p: xml.etree.ElementTree.Element, cache: Cache) -> list:
    ret = []
    if p is None:
        return ret
    if p.text:
        ret.append(Text(p.text))
    for item in p.getchildren():
        # Reference
        if item.tag == 'ref':
            refid = item.get('refid')
            try:
                ref = cache.get(refid)
                if item.text:
                    ret.append(MdBold([MdLink([Text(item.text)], ref.url)]))
                else:
                    ret.append(MdBold([MdLink([Text(ref.getFullName())], ref.url)]))
            except:
                pass

        # simplesect
        elif item.tag == 'simplesect':
            ret.append(Br())
            ret.append(MdBold([Text(SIMPLE_SECTIONS[item.get('kind')])]))
            ret.append(Br())
            for sp in item.findall('para'):
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