import os
import re
from typing import TextIO

from doxybook.node import Node
from doxybook.kind import Kind
from doxybook.config import config

def generate_link(name, url) -> str:
    return '* [' + name + '](' + url + ')\n'

def generate_recursive(f: TextIO, node: Node, level: int, diff: str):
    for child in node.members:
        if child.kind.is_parent():
            f.write(' ' * level + generate_link(child.kind.value + ' ' + child.name, diff + '/' + child.refid + '.md'))
            generate_recursive(f, child, level + 2, diff)

def generate_recursive_modules(f: TextIO, modules: dict, level: int, diff: str):
    for key,value in modules.items():
        f.write(' ' * level + generate_link(value['name'], diff + '/' + key + '.md'))
        if 'innergroups' in value:
            generate_recursive_modules(f, value['innergroups'], level + 2, diff)

def generate_files(f: TextIO, files: dict, level: int, diff: str):
    for key,value in files.items():
        if key == '#':
            continue
        if isinstance(value, dict):
            f.write(' ' * level + generate_link(key + '/', diff + '/' + value['#'] + '.md'))
            generate_files(f, value, level + 2, diff)
        else:
            f.write(' ' * level + generate_link(key, diff + '/' + value + '.md'))
            f.write(' ' * level + generate_link(key + ' - source', diff + '/' + value + '_source.md'))

def generate_summary(output_path: str, summary_file: str, root: Node, modules: list, pages: list, files: dict):
    print('Modifying', summary_file)
    summaryDir = os.path.dirname(os.path.abspath(summary_file))
    output_path = os.path.abspath(output_path)
    diff = output_path[len(summaryDir)+1:].replace('\\', '/')
    link = diff + '/index.md'

    content = []
    with open(summary_file, 'r') as f:
        content = f.readlines()

    start = None
    offset = 0
    end = None
    for i in range(0, len(content)):
        line = content[i]
        if start is None and re.search(re.escape(link), line):
            m = re.search('\\* \\[', line)
            if m is not None:
                start = m.start()
                start = i
            continue
        
        if start is not None and end is None:
            if not line.startswith(' ' * (offset + 2)):
                end = i

    if start is None:
        print('WARNING: Could not generate summary! Unable to find \"* [...](' + link + ')\" in SUMMARY.md')
        return

    if end is None:
        end = len(content)

    with open(summary_file, 'w+') as f:
        # Write first part of the file
        for i in range(0, start+1):
            f.write(content[i])

        if pages:
            f.write(' ' * (offset+2) + generate_link('Related Pages', diff + '/' + 'pages.md'))
            for key,value in pages.items():
                f.write(' ' * (offset+4) + generate_link(value, diff + '/' + key + '.md'))
        if modules:
            f.write(' ' * (offset+2) + generate_link('Modules', diff + '/' + 'modules.md'))
            generate_recursive_modules(f, modules, offset + 4, diff)
            #for key,value in modules.items():
            #    f.write(' ' * (offset+4) + generate_link(value, diff + '/' + key + '.md'))
        f.write(' ' * (offset+2) + generate_link('Class Index', diff + '/' + 'classes.md'))
        f.write(' ' * (offset+2) + generate_link('Function Index', diff + '/' + 'functions.md'))
        f.write(' ' * (offset+2) + generate_link('Variable Index', diff + '/' + 'variables.md'))
        f.write(' ' * (offset+2) + generate_link('Enumeration Index', diff + '/' + 'enumerations.md'))
        f.write(' ' * (offset+2) + generate_link('Class List', diff + '/' + 'annotated.md'))
        generate_recursive(f, root, offset + 4, diff)
        if files:
            f.write(' ' * (offset+2) + generate_link('Files', diff + '/' + 'files.md'))
            generate_files(f, files, offset + 4, diff)
        
        # Write second part of the file
        for i in range(end, len(content)):
            f.write(content[i])
                
