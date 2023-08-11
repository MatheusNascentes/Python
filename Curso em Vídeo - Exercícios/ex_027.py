"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente
Ex: Ana Maria de Souza
Primeiro: Ana
Último: Souza"""

nome = str(input("Digite o seu nome: "))

# Usando lista para separar o nome

listanome = nome.split()
print(f"O seu primeiro nome é {listanome[0]}")
print(f"O seu último nome é {listanome[-1]}")

# Fazendo de uma forma sem usar lista

espini = nome.index(" ")
print(f"O seu primeiro nome é {nome[0:espini]}")

espfin = nome.rfind(" ")
print(f"O seu último nome é {nome[espfin+1:]}")
