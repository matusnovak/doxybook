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

    def is_language(self) -> bool:
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

        if self in LANGUAGE:
            return True
        return False

    def is_parent(self) -> bool:
        return self == Kind.NAMESPACE or self == Kind.CLASS or self == Kind.STRUCT or self == Kind.UNION or self == Kind.INTERFACE

    def is_member(self) -> bool:
        return self.is_language() and not self.is_parent()