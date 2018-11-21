class Stack():
    def __init__(self):
        self.pilha = []

    def Push(self,item):
        #Se nao for igual
        if not(self.Maxsize()):
            #adicione o item
            self.pilha.append(item)
        #Se nao remova e adicione o item
        else:
            self.Pop()
            self.pilha.append(item)

    #Funcao para verificar se o tamanho da lista eh igual  ao numero maximo    
    def Maxsize(self,maximum):
        return len(self.pilha)==maximum


    def Pop(self):
        if not(self.IsEmpty()):
            self.pilha.pop()

    def IsEmpty(self):
        return len(self.pilha)==0

