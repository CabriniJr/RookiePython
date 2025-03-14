
conjuntos = []

num_conj = int(input("Quantos conjuntos tem na operação?(MAX 2 por enquanto)"))

# Função que cria os conjuntos
def criar_conjunto():
    print("\n---Quantos elementos tem o conjunto:")
    x = int(input())
    conjunto =[]
    for i in range(x):
        print("Valor do elemento ",i+1) 
        num = int(input()) 
        conjunto.append(num) 
        print(conjunto) 
    return conjunto

def mem_print():
    conjuntos.append(resultado)
    print(conjuntos,resultado)

# Método "main"

for i in range(num_conj):
    conjunto = criar_conjunto() 
    conjunto.sort()
    conjuntos.append(conjunto)
print(conjuntos)

print("\n\n---Para a operação escolhida, digite o nome ao lado---")
print("UNI (união)- Ex. A = [1,2,3]; B = [3,4,5] ==> AUB = [1,2,3,4,5]")
print("INT (interseçao)- Ex. A = [1,3]; B = [1,2] ==> AintB = [1]")
print("DIF (diferença)- Ex. A = [1,2]; B = [1,3]==>A-B = [2]")
operacao = str(input("\n\nQual operação você deseja?"))  
match operacao:
    case "UNI":
        resultado = list(set(conjuntos[0]).union(set(conjuntos[1])))
        mem_print()
    case "INT":
        resultado =list(set(conjuntos[0]) & set(conjuntos[1]))
        mem_print()
    case "DIF": 
        resultado = list(set(conjuntos[0]) - set(conjuntos[1]))
        mem_print()
    case _:
        print("Digite uma operação válida")
print("\n\nResultado = ",conjuntos[2])
