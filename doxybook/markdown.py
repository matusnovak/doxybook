from typing import List, TextIO
from doxybook.config import config

def escape(s: str):
    ret = s.replace('*', '\\*')
    ret = ret.replace('_', '\\_')
    return ret

class MdRenderer:
    def __init__(self, f: TextIO):
        self.f = f
        self.eol_flag = True

    def write(self, s: str):
        self.f.write(s)
        self.eol_flag = False

    def eol(self):
        if not self.eol_flag:
            self.f.write('\n')
            self.eol_flag = True

class Md:
    def __init__(self, children: List['Md']):
        self.children = children

    def append(self, child: 'Md'):
        self.children.append(child)

    def extend(self, child: List['Md']):
        self.children.extend(child)

class Text:
    def __init__(self, text: str):
        self.text = text

    def render(self, f: MdRenderer, indent: str):
        if self.text:
            f.write(escape(self.text))

class Br:
    def __init__(self):
        pass

    def render(self, f: MdRenderer, indent: str):
        f.write('\n\n')

class MdHint(Md):
    def __init__(self, children: List[Md], typ: str, title: str):
        Md.__init__(self, children)
        self.title = title
        self.typ = typ

    def render(self, f: MdRenderer, indent: str):
        f.write('::: ' + self.typ + ' ' + self.title + '\n')
        for child in self.children:
            child.render(f, '')
        f.write(':::')

class MdBold(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        f.write('**')
        for child in self.children:
            child.render(f, '')
        f.write('**')

class MdImage:
    def __init__(self, url: str):
        self.url = url

    def render(self, f: MdRenderer, indent: str):
        f.write('![Image](' + self.url + ')')

class MdCode(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        f.write('`')
        for child in self.children:
            child.render(f, '')
        f.write('`')

class MdCodeBlock:
    def __init__(self, lines: List[str], lang:str = 'cpp'):
        self.lines = lines
        self.lang = lang

    def set_lang(self, lang:str):
        self.lang = lang

    def append(self, line: str):
        self.lines.append(line)

    def render(self, f: MdRenderer, indent: str):
        f.write('```' + self.lang + '\n')
        for line in self.lines:
            f.write(line)
            f.write('\n')
        f.write('```\n\n')

class MdBlockQuote(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        f.write('\n')
        for child in self.children:
            f.write('> ')
            child.render(f, '')
            f.write('\n')

class MdItalic(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        f.write('_')
        for child in self.children:
            child.render(f, '')
        f.write('_')

class MdParagraph(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        for child in self.children:
            child.render(f, indent)
        f.eol()

class MdLink(Md):
    def __init__(self, children: List[Md], url: str):
        Md.__init__(self, children)
        self.url = url

    def render(self, f: MdRenderer, indent: str):
        f.write('[')
        for child in self.children:
            child.render(f, '')
        f.write('](' + self.url + ')')

class MdDocument(Md):
    def __init__(self):
        Md.__init__(self, [])
        self.keywords = []
        self.title = ''

    def set_title(self, title: str):
        self.title = title
    
    def set_keywords(self, keywords: List[str]):
        self.keywords = keywords

    def header_gitbook(self, f: MdRenderer):
        if len(self.keywords) > 0:
            f.write('search:\n')
            f.write('    keywords: ' + str(self.keywords) + '\n')
        else:
            f.write('search: false\n')

    def header_vuepress(self, f: MdRenderer):
        f.write('title: ' + self.title + '\n')
        if len(self.keywords) > 0:
            #f.write('sidebar: auto\n')
            #f.write('sidebarDepth: 1\n')
            f.write('meta:\n')
            f.write('  - name: keywords\n')
            f.write('    content: ' + ' '.join(self.keywords) + '\n')

    def render(self, f: MdRenderer):
        f.write('---\n')

        if config.target == 'gitbook':
            self.header_gitbook(f)
        elif config.target == 'vuepress':
            self.header_vuepress(f)
        f.write('---\n\n') 

        for child in self.children:
            child.render(f, '')

class MdList(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        f.eol()
        for child in self.children:
            f.write(indent + '* ')
            child.render(f, indent + '  ')

class MdLine:
    def __init__(self):
        pass

    def render(self, f: MdRenderer, indent: str):
        f.eol()
        f.write('----------------------------------------')
        f.eol()

class MdHeader(Md):
    def __init__(self, level: int, children: List[Md]):
        Md.__init__(self, children)
        self.level = level

    def render(self, f: MdRenderer, indent: str):
        f.write('#' * self.level + ' ')
        for child in self.children:
            child.render(f, indent + '')
        f.write('\n')
        f.eol()

class MdTableCell(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        for child in self.children:
            child.render(f, indent)

class MdTableRow(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        f.eol()
        f.write('|')
        for child in self.children:
            child.render(f, '')
            f.write('|')
        f.eol()

class MdTable(Md):
    def __init__(self):
        Md.__init__(self, [])
    
    def render(self, f: MdRenderer, indent: str):
        is_first = True
        f.eol()
        for child in self.children:
            child.render(f, '')
            if is_first:
                for i in range(0, len(child.children)):
                    f.write('|-----')
                f.write('|')
            is_first = False
        f.write('\n\n')
