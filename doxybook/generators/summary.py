import os
import re
from typing import TextIO

from doxybook.node import Node
from doxybook.kind import Kind

def generateLink(name, url) -> str:
    return '* [' + name + '](' + url + ')\n'

def generateRecursive(f: TextIO, node: Node, level: int, diff: str):
    for child in node.members:
        if child.kind is Kind.STRUCT or child.kind is Kind.CLASS or child.kind is Kind.NAMESPACE:
            f.write(' ' * level + generateLink(child.kind.value + ' ' + child.name, diff + '/' + child.refid + '.md'))
            generateRecursive(f, child, level + 2, diff)

def generateFiles(f: TextIO, files: dict, level: int, diff: str):
    for key,value in files.items():
        if key == '#':
            continue
        if isinstance(value, dict):
            f.write(' ' * level + generateLink(key + '/', diff + '/' + value['#'] + '.md'))
            generateFiles(f, value, level + 2, diff)
        else:
            f.write(' ' * level + generateLink(key, diff + '/' + value + '.md'))
            f.write(' ' * level + generateLink(key + ' - source', diff + '/' + value + '_source.md'))

def generateSummary(outputDir: str, summaryFile: str, root: Node, modules: list, pages: list, files: dict):
    print('Modifying', summaryFile)
    summaryDir = os.path.dirname(os.path.abspath(summaryFile))
    outputDir = os.path.abspath(outputDir)
    diff = outputDir[len(summaryDir)+1:].replace('\\', '/')
    link = diff + '/index.md'

    content = []
    with open(summaryFile, 'r') as f:
        content = f.readlines()

    start = None
    offset = None
    end = None
    for i in range(0, len(content)):
        line = content[i]
        if start is None and re.search(re.escape(link), line):
            offset = re.search('\\* \\[', line).start()
            start = i
            continue
        
        if start is not None and end is None:
            if not line.startswith(' ' * (offset + 2)):
                end = i

    if end is None:
        end = len(content)

    with open(summaryFile, 'w+') as f:
        # Write first part of the file
        for i in range(0, start+1):
            f.write(content[i])

        if pages:
            f.write(' ' * (offset+2) + generateLink('Related Pages', diff + '/' + 'pages.md'))
            for key,value in pages.items():
                f.write(' ' * (offset+4) + generateLink(value, diff + '/' + key + '.md'))
        if modules:
            f.write(' ' * (offset+2) + generateLink('Modules', diff + '/' + 'modules.md'))
            for key,value in modules.items():
                f.write(' ' * (offset+4) + generateLink(value, diff + '/' + key + '.md'))
        f.write(' ' * (offset+2) + generateLink('Class Index', diff + '/' + 'classes.md'))
        f.write(' ' * (offset+2) + generateLink('Class List', diff + '/' + 'annotated.md'))
        generateRecursive(f, root, offset + 4, diff)
        if files:
            f.write(' ' * (offset+2) + generateLink('Files', diff + '/' + 'files.md'))
            generateFiles(f, files, offset + 4, diff)
        
        # Write second part of the file
        for i in range(end, len(content)):
            f.write(content[i])
                
