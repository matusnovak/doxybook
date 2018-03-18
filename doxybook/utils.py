from typing import List

def contains(a, pos, b):
    ai = pos
    bi = 0
    if len(b) > len(a) - pos:
        return False
    while bi < len(b):
        if a[ai] != b[bi]:
            return False
        ai += 1
        bi += 1
    return True

def tokenize(s: str, delim: str) -> List[str]:
    tokens = []
    i = 0
    last = 0
    inside = 0
    while i < len(s):
        c = s[i]
        if i == len(s)-1:
            tokens.append(s[last:i+1])
        if c == '<' or c == '[' or c == '{':
            inside += 1
            i += 1
            continue
        if c == '>' or c == ']' or c == '}':
            inside -= 1
            i += 1
            continue
        if inside > 0:
            i += 1
            continue
        if contains(s, i, delim):
            tokens.append(s[last:i])
            i += 2
            last = i
        i += 1
    return tokens

ALLOWED_FILE_NAME_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"

def mangleName(name: str) -> str:
    out = ''
    i = 0
    while i < len(name):
        c = name[i]
        if c in ALLOWED_FILE_NAME_CHARS:
            out += c
        else:
            out += '_'
        i += 1
    return out