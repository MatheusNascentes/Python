# Faça um programa que leia um número inteiro qualquer e mostre na tela sua taboada.

num = int(input("Digite um número para ver a taboada: "))
print("-" * 20)
for c in range(1, 11):
    print(f"{c:2} x {num} = {c*num}")
print("-" * 20)
