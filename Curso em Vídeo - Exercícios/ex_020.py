"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
   Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle
alunos = []

for c in range(1, 5):
    alunos.append(str(input(f"Digite o nome do {c}º aluno: ")))

shuffle(alunos)
print("A sequência de apresentação será:")

for s in alunos:
    print(f"{alunos.index(s)+1}º - {s}")
