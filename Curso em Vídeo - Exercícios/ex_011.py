""" Faça um prgrama que leia a largura e a altura de uma parede em metros, calcule a sua área
    e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
    uma área de 2m²"""

larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parade: "))

print(f"Uma parede de {larg}x{alt} tem {larg*alt:.2f}m²")
print(f"Portanto você gastará {(larg*alt)/2}litros de tinta.")
