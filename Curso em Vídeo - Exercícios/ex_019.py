"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
   lendo o nome deles e escrevendo o nome do escolhido."""
from random import randint
# Farei aqui de uma forma mais básica simples.

aluno1 = str(input("Digite o nome do primeiro aluno(a): "))
aluno2 = str(input("Digite o nome do segundo aluno(a): "))
aluno3 = str(input("Digite o nome do terceiro aluno(a): "))
aluno4 = str(input("Digite o nome do quarto aluno(a): "))

sorteio = randint(1, 4)
if sorteio == 1:
    print(f"O aluno sorteado para apagaro quadro foi {aluno1}")
if sorteio == 2:
    print(f"O aluno sorteado para apagaro quadro foi {aluno2}")
if sorteio == 3:
    print(f"O aluno sorteado para apagaro quadro foi {aluno3}")
if sorteio == 4:
    print(f"O aluno sorteado para apagaro quadro foi {aluno4}")

# Agora farei de uma forma mais prática
alunos = []

for c in range(1, 5):
    alunos.append(str(input(f"Digite o nome do {c}º aluno(a): ")))
print(f"O aluno sorteado para apagaro quadro foi {alunos[randint(0,4)]}.")
