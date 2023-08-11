# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input("Digite o nome de uma cidade: ")).strip().upper()
if cidade.find("SANTO") == 0:
    print("A cidade digitada começa com a palavra SANTO")
else:
    print("A cidade digitada não começa com a palavra SANTO")
