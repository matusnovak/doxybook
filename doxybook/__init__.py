import argparse
import sys
import os
import xml.etree.ElementTree

from doxybook.loader import load_root
from doxybook.kind import Kind
from doxybook.node import Node
from doxybook.cache import Cache
from doxybook.generators import (
    generate_annotated,
    generate_class_index,
    generate_dir,
    generate_file,
    generate_files,
    generate_member,
    generate_modules,
    generate_page,
    generate_pages,
    generate_summary,
    generate_function_index,
    generate_variable_index,
    generate_enum_index
)
from doxybook.config import config

def write_groups(index_path: str, output_path: str, node: Node, cache: Cache):
    for member in node.members:
        if member.kind == Kind.GROUP:
            generate_member(index_path, output_path, member.refid, cache)
            write_groups(index_path, output_path, member, cache)

def write_members(index_path: str, output_path: str, node: Node, cache: Cache):
    for member in node.members:
        if member.kind == Kind.STRUCT or member.kind == Kind.NAMESPACE or member.kind == Kind.CLASS or member.kind == Kind.INTERFACE:
            generate_member(index_path, output_path, member.refid, cache)
            write_members(index_path, output_path, member, cache)

def main():
    parser = argparse.ArgumentParser(description='Convert doxygen XML output into GitBook or Vuepress markdown output.')
    parser.add_argument('-t', '--target', 
        type=str, 
        help='Select the target: Gitbook (default) or Vuepress, for example: "-t vuepress" or "-t gitbook"',
        required=False,
        default=config.target
    )
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
        help='Path to the summary file which contains a link to index.md in the folder pointed by --input (default: false)',
        required=False
    )
    parser.add_argument('-d', '--debug', 
        type=bool, 
        help='Debug the class hierarchy (default: false)',
        required=False,
        default=config.debug
    )
    parser.add_argument('--noindex', 
        type=bool, 
        help='If set to true, no search keywords will be generated at the file headers (default: false)',
        required=False,
        default=config.noindex
    )
    parser.add_argument('--hints', 
        type=bool, 
        help='(Vuepress only) If set to true, hints will be generated for the sections note, bug, and a warning (default: true)',
        required=False,
        default=config.hints
    )

    args = parser.parse_args()

    if args.target != 'gitbook' and args.target != 'vuepress':
        raise Exception('Unknown target: ' + str(args.target))

    config.debug = args.debug
    config.target = args.target
    config.noindex = args.noindex
    config.hints = args.hints

    if args.summary and not os.path.exists(args.summary):
        raise Exception('The provided summary file does not exist!')

    if not os.path.exists(args.output) or not os.path.isdir(args.output):
        raise Exception('The target output directory does not exist!')

    os.makedirs(args.output, exist_ok=True)
    cache = Cache()
    root = load_root(cache, args.input)

    # Generate Index
    generate_class_index(args.output, root)
    generate_function_index(args.output, root)
    generate_variable_index(args.output, root)
    generate_enum_index(args.output, root)

    # Generate Class List
    generate_annotated(args.output, root)

    # Write all members out
    write_members(args.input, args.output, root, cache)

    # Generate modules page
    modules = generate_modules(args.input, args.output, root, cache)

    # Write all grouos out
    write_groups(args.input, args.output, root, cache)

    # Generate pages page
    pages = generate_pages(args.input, args.output, root, cache)

    # Write all pages out
    for child in root.members:
        if child.kind == Kind.PAGE:
            generate_page(args.input, args.output, child.refid, cache)

    # Generate files page
    files = generate_files(args.input, args.output, root, cache)

    # Write all files out
    for child in root.members:
        if child.kind == Kind.FILE:
            generate_member(args.input, args.output, child.refid, cache)
            generate_file(args.input, args.output, child, cache)
        if child.kind == Kind.DIR:
            generate_dir(args.input, args.output, child, cache)

    # Update summary
    if args.summary:
        generate_summary(args.output, args.summary, root, modules, pages, files)