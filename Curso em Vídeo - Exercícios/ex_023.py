"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
        Digite um número: 1834
        Unidade: 4
        Dezena: 3
        Centena: 8
        Milhar:1 """

numero = input("Digite um númer entre 0 e 9999: ")
if len(numero) == 1:
    print(
        f"O número tem apenas um dígito, portanto: \n   Unidade: {numero[0]}")
elif len(numero) == 2:
    print(
        f"O número tem dois dígitos, portanto: \n   Unidade: {numero[1]} \n   Dezena: {numero[0]}")
elif len(numero) == 3:
    print(
        f"O número tem três dígitos, portanto: \n   Unidade: {numero[2]} \n   Dezena: {numero[1]} \n\
   Centena: {numero[0]}")
else:
    print(
        f"O número tem três dígitos, portanto: \n   Unidade: {numero[3]} \n   Dezena: {numero[2]} \n\
   Centena: {numero[1]}\n   Milhar: {numero[0]}")
