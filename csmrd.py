from functools import reduce
from operator import mul
def prod(nodes_true):
    prod = 1
    for i in nodes_true:
        prod *= i * 2
    return prod

def binVet(n):
    return [int(x) for x in bin(n)[2:]]

def isValid(vet, tree):
    nodes_true = [i*x for i, x in enumerate(vet)]
    nodes_true = list(filter(lambda i: i != 0, [i*x for i, x in enumerate(vet)]))
    for node in nodes_true:
        for dependency in tree[node]:
            if dependency not in nodes_true:
                return []
    return nodes_true

def getCombinationValids(tree):
    mult = []
    combinations = []
    for i in range(0, 2 ** (len(tree) +1)):
        vet = binVet(i)
        nodes_true = isValid(vet, tree)
        #print(vet)
        if nodes_true:
            produto = prod(nodes_true)
            if produto not in mult:
                mult.append(produto)
                combinations.append(nodes_true)
                #print(nodes_true)
    return combinations

def read2int():
    n1, n2 = [int(i) for i in input().split(' ')]
    return n1, n2

# tree = {
#     1: [2],
#     2: [3],
#     3: [4],
#     4: [5],
#     5: [6],
# }
# vet = [5]
# print(isValid(vet, tree))

n, d = read2int()
tree = {}

for i in range(1, n+1):
    tree[i] = []

for i in range(0, d):
    n1, n2 = read2int()
    tree[n1].append(n2)
print(tree)
print(len(getCombinationValids(tree)))
