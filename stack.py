class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

vyhozene_cislo = stack.pop()

print(vyhozene_cislo)
print(stack.stack)
