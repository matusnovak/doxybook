import argparse
import sys
import xml.etree.ElementTree

from doxybook.loader import loadRoot
from doxybook.kind import Kind
from doxybook.node import Node
import doxybook.generators.classindex as classIndexWriter
import doxybook.generators.classhierarchy as classHierarchyWriter
import doxybook.generators.member as memberWriter

def writeMembers(outputDir: str, node: Node):
    for member in node.members:
        if member.kind == Kind.STRUCT or member.kind == Kind.NAMESPACE or member.kind == Kind.CLASS:
            memberWriter.generate(outputDir, member)
            writeMembers(outputDir, member)

def main():
    parser = argparse.ArgumentParser(description='Convert doxygen XML output into GitBook markdown output.')
    parser.add_argument('-i', '--input', 
        type=str, 
        help='Path to doxygen generated xml folder',
        required=True
    )
    parser.add_argument('-o', '--output', 
        type=str, 
        help='Path to the destination folder',
        required=True
    )

    args = parser.parse_args()
    root = loadRoot(args.input)

    classIndexWriter.generate(args.output, root)
    classHierarchyWriter.generate(args.output, root)
    writeMembers(args.output, root)

if __name__ == '__main__':
    main()