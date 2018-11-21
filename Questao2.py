class Stack():
    def __init__(self):
        self.pilha = []

    def Push(self,item):
        if not(self.AlreadyHas(item)):
            self.pilha.append(item)

    def AlreadyHas(self,item):
        return item in self.pilha
