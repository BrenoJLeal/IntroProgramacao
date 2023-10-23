Q = []
for i in range(20):
    while True:
        num = float(input(f"Digite o número {i + 1}º (positivo): "))
        if num > 0:
            Q.append(num)
            break
        else:
            print("Por favor, digite um número positivo.")

maior_elemento = max(Q)
posicao_maior = Q.index(maior_elemento)

menor_elemento = min(Q)
posicao_menor = Q.index(menor_elemento)

print(f"O maior elemento de Q é {maior_elemento} e ocupa a {posicao_maior + 1}º posição.")
print(f"O menor elemento de Q é {menor_elemento} e ocupa a {posicao_menor + 1}º posição.")
