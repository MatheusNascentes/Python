# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, consseno e tangente desse ângulo
from math import sin, cos, tan, radians

angulo = radians(float(input("Digite o valor do ângulo: ")))
print(f"O seno do ângulo é {sin(angulo):.2f}")
print(f"O cosseno do ângulo é {cos(angulo):.2f}")
print(f"A tangente do ângulo é {tan(angulo):.2f}")
