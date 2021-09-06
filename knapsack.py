def knapsack(v, w, C):
    """
    v: valores dos itens
    w: peso dos itens
    C: capacidade da mochila
    """
    N = len(v)
    m = {}
    for c in range(C+1):
        m[(0,c)] = 0
    for i in range(1, N+1):
        for c in range(C+1):
            if w[i-1] <= c:
                m[(i,c)] = max(m[(i-1,c)], v[i-1] + m[(i-1,c-w[i-1])])
            else: 
                m[(i,c)] = m[(i-1,c)]
    return m[(N,C)]

# v = [500, 250, 1500, 1200, 1200, 800]
# w = [4, 3, 10, 12, 9, 6]
# C = 30
C = int(input("Digite a capacidade da mochila (peso): "))
qtde = int(input("Digite a quantidade de itens para se levar na mochila: "))
nomeItens = []
v = []
w = []
for i in range (0, qtde):
    elem = str(input("Digite o nome do item {}: ".format(i+1)))
    nomeItens.append(elem)

for i in range (0, qtde):
    elem = float(input("Digite o valor do item {}: ".format(i+1)))
    v.append(elem)

for i in range (0, qtde):
    elem = int(input("Digite o peso do item {}: ".format(i+1)))
    w.append(elem)    


print("O maior valor possível para se carregar na mochila é:",knapsack(v, w, C))