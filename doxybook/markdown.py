from typing import List, TextIO

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

class MdText:
    def __init__(self, text: str):
        self.text = text

    def render(self, f: MdRenderer, indent: str):
        f.write(self.text)

class MdParagraph(Md):
    def __init__(self, children: List[Md]):
        Md.__init__(self, children)

    def render(self, f: MdRenderer, indent: str):
        for child in self.children:
            child.render(f, indent)
        f.eol()

class MdLink:
    def __init__(self, text: str, url: str):
        self.text = text
        self.url = url

    def render(self, f: MdRenderer, indent: str):
        f.write('[' + self.text + '](' + self.url + ')')

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
        f.eol()