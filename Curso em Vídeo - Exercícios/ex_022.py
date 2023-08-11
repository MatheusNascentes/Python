# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo: ")).strip()

print(f"O seu nome com todas as letras maiúsculas é: {nome.upper()}.")
print(f"O seu nome com todas as letras maiúsculas é: {nome.lower()}.")
print(f"Seu nome ao todo tem {len(nome)-nome.count(' ')} letras.")
print(f"O seu primeiro nome tem {nome.find(' ')} letras")
