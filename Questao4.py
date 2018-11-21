def Stack(pilha):
    soma = 0
    for item in pilha:
        soma+=item


    for i in pilha:
        pilha.pop()
    return soma

pilha = [1,2,3,4,5]
soma = Stack(pilha)
print(soma)

