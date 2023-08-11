"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
   retângulo, calcule e mostre o comprimento da hipotenusa"""

from math import hypot

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

print(f"O valor da hipotenusa é {(co**2 + ca**2)**(1/2):.2f}")
print(f"O valor da hipotenusa é {hypot(co, ca):.2f}")
