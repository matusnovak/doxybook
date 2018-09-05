from doxybook.kind import Kind
from doxybook.utils import mangle_name
from doxybook.config import config

class Node:
    def __init__(self, name: str, refid: str, kind: str):
        if not isinstance(kind, Kind):
            raise TypeError('kind must be an instance of Kind Enum, got: ' + kind)

        self.name = name
        self.refid = refid
        self.kind = kind
        self.parent = None
        self.members = []
        self.url = None
        self.overloaded = False
        self.overload_num = 1
        self.overload_total = 1

    def get_full_name(self, include_namespace: bool = False) -> str:
        ret = self.name
        namespace_check = True
        if self.parent is not None and self.parent.kind == Kind.NAMESPACE and include_namespace == False:
            namespace_check = False
        if self.parent is not None and self.parent.kind != Kind.ROOT and namespace_check:
            ret = self.parent.get_full_name(include_namespace) + '::' + ret
        return ret

    def get_namespace(self) -> 'Node':
        if self.kind == Kind.ROOT:
            return None
        elif self.kind == Kind.NAMESPACE:
            return self
        else: 
            return self.parent.get_namespace()

    def add_member(self, member: 'Node'):
        member.parent = self
        self.members.append(member)

    def find_member(self, name: str) -> 'Node':
        for child in self.members:
            if(child.name == name):
                return child

        return None

    def get_anchor_hash(self):
        if config.target == 'gitbook':
            return self.refid[-34:]
        anchor = self.kind.value + '-' + self.name.replace(' ', '-').replace('_', '-').replace('=', '').replace('~', '').lower()
        if self.overloaded:
            return anchor + '-' + str(self.overload_num) + '-' + str(self.overload_total)
        else:
            return anchor

    def get_kind_str(self):
        return self.kind.value

    def generate_url(self) -> str:
        if self.kind.is_parent():
            return self.refid + '.md'
        else:
            if self.refid.startswith('group_'):
                return self.refid[:-36] + '.md#' + self.get_anchor_hash()
            return self.refid[:-35] + '.md#' + self.get_anchor_hash()

    def finalize(self):
        self.url = self.generate_url()
