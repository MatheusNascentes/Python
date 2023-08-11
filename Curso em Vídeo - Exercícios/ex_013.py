# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input("Digite o valor do salário do funcionário: R$ "))
print(f"O novo salário com 15% de aumento é R$ {salario+(salario*0.15):.2f}")
