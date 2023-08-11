"""Escreva um programa que faça o computador 'penssar' em um número inteiro entre 0 e 5 e
   peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
   O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint

numeropc = randint(0, 5)

print("=-" * 17)
print("VAMOS JOGAR UM JOGO DE ADIVINHAÇÃO")
print("=-" * 17)
numerousu = int(
    input("\nEu pensei em um número entre 0 e 5. Tente adivinhar: "))

while True:
    if 0 < numerousu > 5:
        numerousu = int(
            input(f"O número {numerousu} não é válido, digite um número entre 0 e 5: "))
    else:
        break

if numeropc == numerousu:
    print(f"Parabéns você acertou, pensei no número {numeropc}.")
else:
    print(f"Errou, eu pensei no número {numeropc}")
