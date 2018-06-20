import argparse
import sys
import os
import xml.etree.ElementTree

from doxybook.loader import loadRoot
from doxybook.kind import Kind
from doxybook.node import Node
from doxybook.generators.classindex import generateClassIndex
from doxybook.generators.annotated import generateAnnotated
from doxybook.generators.member import generateMember
from doxybook.generators.summary import generateSummary
from doxybook.generators.modules import generateModules
from doxybook.generators.page import generatePage
from doxybook.generators.pages import generatePages
from doxybook.generators.file import generateFile
from doxybook.generators.files import generateFiles
from doxybook.generators.dir import generateDir
from doxybook.cache import Cache

def writeMembers(indexDir: str, outputDir: str, node: Node, cache: Cache, noindex: bool):
    for member in node.members:
        if member.kind == Kind.STRUCT or member.kind == Kind.NAMESPACE or member.kind == Kind.CLASS or member.kind == Kind.INTERFACE:
            generateMember(indexDir, outputDir, member.refid, cache, noindex)
            writeMembers(indexDir, outputDir, member, cache, noindex)

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
    parser.add_argument('-s', '--summary', 
        type=str, 
        help='Path to the summary file which contains a link to index.md in the folder pointed by --input',
        required=False
    )
    parser.add_argument('-d', '--debug', 
        type=bool, 
        help='Debug the class hierarchy',
        required=False
    )
    parser.add_argument('--noindex', 
        type=bool, 
        help='If set to true, adds section at the top of the file to disable indexing for all generated files',
        required=False
    )
    parser.add_argument('--limitindex', 
        type=bool, 
        help='If set to true, adds section at the top of the file to disable indexing for all generated files, except class and annotated lists',
        required=False
    )

    args = parser.parse_args()

    if args.summary and not os.path.exists(args.summary):
        raise Exception('The provided summary file does not exist!')

    os.makedirs(args.output, exist_ok=True)
    cache = Cache()
    root = loadRoot(cache, args.input, args.debug)

    annotatedIndexing = True
    memberIndexing = True

    if args.noindex:
        annotatedIndexing = False
        memberIndexing = False
    if args.limitindex:
        annotatedIndexing = True
        memberIndexing = False

    # Generate Class Index
    generateClassIndex(args.output, root, not annotatedIndexing)

    # Generate Class List
    generateAnnotated(args.output, root, not annotatedIndexing)

    # Write all members out
    writeMembers(args.input, args.output, root, cache, not memberIndexing)

    # Generate modules page
    modules = generateModules(args.input, args.output, root, cache)

    # Write all grouos out
    for child in root.members:
        if child.kind == Kind.GROUP:
            generateMember(args.input, args.output, child.refid, cache, not memberIndexing)

    # Generate pages page
    pages = generatePages(args.input, args.output, root, cache)

    # Write all pages out
    for child in root.members:
        if child.kind == Kind.PAGE:
            generatePage(args.input, args.output, child.refid, cache)

    # Generate files page
    files = generateFiles(args.input, args.output, root, cache)

    # Write all files out
    for child in root.members:
        if child.kind == Kind.FILE:
            generateMember(args.input, args.output, child.refid, cache, not memberIndexing)
            generateFile(args.input, args.output, child, cache)
        if child.kind == Kind.DIR:
            generateDir(args.input, args.output, child, cache)

    # Update summary
    if args.summary:
        generateSummary(args.output, args.summary, root, modules, pages, files)