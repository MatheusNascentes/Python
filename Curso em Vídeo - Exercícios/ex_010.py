# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considerando US$ 1,00 = R$ 3,27

reais = float(input("Quantos reais você possui? "))
print(f"Com R$ {reais:.2f} você consegue comprar US$ {reais/3.27:.2f}.")
