class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()

print (s.is_empty())
s.push(4)
s.push('dog')
print (s.peek())
print (s.size())
print(s)

print(s.is_empty())
s.push(8.4)

print(s.pop())
print(s.pop())
print(s.size())


# Stacks using the head of the list

class Stack2:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s2 = Stack2()

s.push('hello')
s.push('true')
print(s.pop())

# Paranthesis Checker

def par_checker(symbol_string):
    st = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            st.push(symbol)
        else:
            if st.is_empty():
                balanced = False
            else:
                st.pop()
        index += 1

    if balanced and st.is_empty():
        return True
    else:
        return False

print(par_checker('((()))'))

print(par_checker('((())'))