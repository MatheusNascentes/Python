"""Escreva um programa que leia a velocidade de um carro.
   Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
   A multa vai custar R$ 7,00 por cada km acima do limite"""

velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print(f"A sua velocidade é maior que a permitida!! \n\
Você ultrapassou a velocidade em {velocidade-80} Km/h. \n\
A multa será de R${(velocidade -80)*7}.")
else:
    print("Velocidade dentro o permitido. Tenha uma ótima viagem!!")
