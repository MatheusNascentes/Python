"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
   e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
   que o carro custa R$ 60 por dia e R$0.15 por Km rodado"""

dias = int(input("Por quantos dias o carro foi locado? "))
km = float(input("Quantos quilômetros foi rodado? "))

print(
    f"O total a pagar por {dias} dias e {km} Km é R${dias*60+km*0.15:.2f}")
