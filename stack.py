import os


class EmptyStack(Exception):
    """Exception for stack ADT"""
    pass


class Stack:
    """Implementation of a Stack Abstract Data Type"""

    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def is_empty(self):
        return len(self._stack) == 0

    def pop(self):
        if self.is_empty():
            raise EmptyStack()
        return self._stack.pop()

    def top(self):
        if self.is_empty():
            raise EmptyStack()
        return self._stack[-1]  # return the last item in the list

    def push(self, e):
        return self._stack.append(e)


def reverse_file(filename):
    if not os.path.exists(filename):
        raise AttributeError("Give a valid filename")
    S = Stack()
    file = open(filename)
    for line in file:
        S.push(line.rstrip('\n'))
    file.close

    out = open(filename, 'w')
    while not S.is_empty():
        out.write(S.pop() + '\n')
    out.close


def is_matched(expr):
    """Algorithm to match properly delimiters"""
    lefty = '({['
    righty = ']})'
    stack = Stack()
    for k in expr:
        if k in lefty:
            stack.push(k)
        elif k in righty:
            if stack.is_empty():
                return False
            if righty.index(k) != lefty.index(stack.pop()):
                return False
    return stack.is_empty()


def match_tags(raw):
    """Match tags in a Markup Language"""
    stack = Stack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith('/'):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if tag[1:] != stack.pop():
                return False
        j = raw.find('<', k + 1)
    return stack.is_empty()


if __name__ == '__main__':
    expr = "<html> </html/> "
    print(match_tags(expr))
