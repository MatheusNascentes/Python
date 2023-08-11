# Crie um programa que leia o nome de uma pessoa e diga se la tem SILVA no nome.

nome = str(input("Digite o seu nome completo: ")).strip().upper()

if "SILVA" in nome:
    print("O nome digitado contém SILVA")
else:
    print("O nome digitado não contém SILVA")
