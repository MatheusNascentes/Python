# Crie um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input("Digite qualquer coisa: ")

print(f"O tipo primitivo da variável é {type(palavra)}")
print(f"Contém apenas espaços? {palavra.isspace()}")
print(f"A variável é um número? {palavra.isnumeric}")
print(f"A variável é alfabética? {palavra.isalpha}")
print(f"A variável é alfanumérica? {palavra.isalpha}")
print(f"A variável está em maiúscula? {palavra.isupper}")
print(f"A variável está em minúscula? {palavra.islower}")
print(f"A variável está captalizada? {palavra.istitle}")
