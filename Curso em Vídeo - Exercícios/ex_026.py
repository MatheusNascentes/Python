"""Faça um programa que leia uma franse pelo teclado e mostre:
Quantas vezes aparece a letra A.
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez."""

frase = str(input("Digite uma frase: ")).strip().upper()
if frase.count("A") == 0:
    print("A frase não contém a letra a.")
else:
    print(f"A letra a aparece {frase.count('A')} vezes.")
    print(
        f"A primeira ocorrência da letra a é na posição {frase.index('A')+1}.")
    print(f"A última ocorrência da letra a é na posição {frase.rfind('A')+1}.")
