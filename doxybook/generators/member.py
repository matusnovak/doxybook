import os

from doxybook.markdown import MdDocument, MdText, MdLink, MdHeader, MdList, MdParagraph, MdRenderer, MdLine
from doxybook.node import Node
from doxybook.kind import Kind

def generate(outputDir: str, node: Node):
    document = MdDocument()

    # Add title
    document.append(MdHeader(1, [MdText(node.name + ' ' + node.kind.value + ' Reference')]))

    document.append(MdLine())
    document.append(MdParagraph([MdText('The documentation for this class was generated from the following file:')]))

    # Save
    os.makedirs(outputDir, exist_ok=True)
    with open(os.path.join(outputDir, node.url), 'w+') as f:
        document.render(MdRenderer(f))

