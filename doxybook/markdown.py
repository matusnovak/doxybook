from typing import List, TextIO

def escape(s: str):
    ret = s.replace('*', '\\*')
    ret = ret.replace('_', '\\_')
    return ret

class MdRenderer:
    def __init__(self, f: TextIO):
        self.f = f
        self.eolFlag = True

    def write(self, s: str):
        self.f.write(s)
        self.eolFlag = False

    def eol(self):
        if not self.eolFlag:
            self.f.write('\n')
            self.eolFlag = True

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

class MdBold(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        f.write('**')
        for child in self.children:
            child.render(f, '')
        f.write('**')

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

    def render(self, f: MdRenderer):
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
        isFirst = True
        f.eol()
        for child in self.children:
            child.render(f, '')
            if isFirst:
                for i in range(0, len(child.children)):
                    f.write('|-----')
                f.write('|')
            isFirst = False
        f.write('\n\n')
