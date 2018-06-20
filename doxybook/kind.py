from enum import Enum

class Kind(Enum):
    ROOT = 'root'
    NAMESPACE = 'namespace'
    CLASS = 'class'
    STRUCT = 'struct'
    UNION = 'union'
    FUNCTION = 'function'
    VARIABLE = 'variable'
    DEFINE = 'define'
    TYPEDEF = 'typedef'
    ENUM = 'enum'
    ENUMVALUE = 'enumvalue'
    FRIEND = 'friend'
    FILE = 'file'
    DIR = 'dir'
    PAGE = 'page'
    EXAMPLE = 'example'
    GROUP = 'group'
    INTERFACE = 'interface'

LANGUAGE = [
    Kind.ROOT,
    Kind.FUNCTION,
    Kind.VARIABLE,
    Kind.NAMESPACE,
    Kind.DEFINE,
    Kind.CLASS,
    Kind.STRUCT,
    Kind.TYPEDEF,
    Kind.ENUM,
    Kind.ENUMVALUE,
    Kind.FILE,
    Kind.UNION,
    Kind.INTERFACE
]

def isKindLanguage(kind: Kind) -> bool:
    if kind in LANGUAGE:
        return True
    return False

def isKindParent(kind: Kind) -> bool:
    return kind == Kind.NAMESPACE or kind == Kind.CLASS or kind == Kind.STRUCT or kind == Kind.UNION or kind == Kind.INTERFACE

def isKindMember(kind: Kind) -> bool:
    return isKindLanguage(kind) and not isKindParent(kind)