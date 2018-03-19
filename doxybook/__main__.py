import argparse
import sys
import xml.etree.ElementTree

from doxybook.loader import loadRoot
from doxybook.kind import Kind
from doxybook.node import Node
from doxybook.generators.classindex import generateClassIndex
from doxybook.generators.classhierarchy import generateHierarchy
from doxybook.generators.member import generateMember
from doxybook.cache import Cache

def writeMembers(indexDir: str, outputDir: str, node: Node, cache: Cache):
    for member in node.members:
        if member.kind == Kind.STRUCT or member.kind == Kind.NAMESPACE or member.kind == Kind.CLASS:
            generateMember(indexDir, outputDir, member, cache)
            writeMembers(indexDir, outputDir, member, cache)

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

    cache = Cache()
    root = loadRoot(cache, args.input)

    generateClassIndex(args.output, root)
    generateHierarchy(args.output, root)
    writeMembers(args.input, args.output, root, cache)

if __name__ == '__main__':
    main()