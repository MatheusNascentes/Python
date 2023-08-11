# Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

"""Também seria possível fazer de uma forma mais direta como o exemplo abaixo.
soma = int(input("Digite o primeiro número: ")) + \
    int(input("Digite o segundo número: "))
print(f"A soma dos números digitados é {soma}")"""

soma = num1 + num2

print(f"A soma entre {num1} e {num2} é {soma}!")
