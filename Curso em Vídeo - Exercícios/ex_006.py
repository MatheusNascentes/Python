# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input("Digite um número para ser analisado: "))
print(f"O dobro de {num} é {num*2}.")
print(f"O tripo de {num} é {num*3}.")
print(f"A raiz quadrada de {num} é {pow(num,1/2):.2f}")

# Poderia colocar todos os prints em uma linha, mas por estética preferi deixar dessa forma.
