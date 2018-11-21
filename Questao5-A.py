class Stack():
    def __init__(self):
        self.pilha = []

    def Push(self,item):
        self.pilha.append(item)

    def Pop(self):
        if not(self.IsEmpty()):
            return self.pilha.pop()

    def IsEmpty(self):
        return len(self.pilha)==0

    def length(self):
        return len(self.pilha)

    def Peek(self):
        if not(self.IsEmpty()):
            return self.pilha[-1]



stack = Stack()
for i in range(16):
    if (i%3==0):
        stack.Push(i)
        print('O valor %d foi empilhado'%(i))
        
