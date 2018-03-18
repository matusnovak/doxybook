import hashlib

from doxybook.kind import Kind, isKindMember
from doxybook.utils import mangleName

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

    def getFullName(self, includeNamespace: bool = False) -> str:
        ret = self.name
        namespaceCheck = True
        if self.parent is not None and self.parent.kind == Kind.NAMESPACE and includeNamespace == False:
            namespaceCheck = False
        if self.parent is not None and self.parent.kind != Kind.ROOT and namespaceCheck:
            ret = self.parent.getFullName(includeNamespace) + '::' + ret
        return ret

    def getNamespace(self) -> 'Node':
        if self.kind == Kind.ROOT:
            return None
        elif self.kind == Kind.NAMESPACE:
            return self
        else: 
            return self.parent.getNamespace()

    def addMember(self, member: 'Node'):
        member.parent = self
        self.members.append(member)

    def findMember(self, name: str) -> 'Node':
        for child in self.members:
            if(child.name == name):
                return child

        return None

    def getAnchorHash(self):
        return hashlib.md5(self.refid.encode('utf-8')).hexdigest()[0:8]

    def getKindStr(self):
        return self.kind.value

    def generateUrl(self) -> str:
        url = ''
        if isKindMember(self.kind):
            url = '#' + self.getAnchorHash()
        else:
            url = mangleName(self.name) + '.md'
        parent = self.parent
        while parent != None and parent.kind != Kind.ROOT:
            if url[0] == '#':
                url = mangleName(parent.name) + '.md' + url
            else:
                url = mangleName(parent.name) + '_' + url
            parent = parent.parent
        return '' + url

    def finalize(self):
        self.url = self.generateUrl()