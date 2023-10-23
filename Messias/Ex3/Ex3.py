def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

entrada = [1, 2, 3, 4, 5, 6]

saida = soma_pares(entrada)
print(f"A soma dos números pares é: {saida}")
