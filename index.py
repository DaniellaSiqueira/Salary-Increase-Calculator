salario = int(input('digite o valor atual do salário: '))
porcentagem = int(input('digite o valor da porcentagem de aumento: '))
porcentagem = porcentagem / 100
aumento = (salario * porcentagem)
print (f' O valor do aumento é de: {salario * porcentagem}')
print (f' O novo salário é de: {aumento + salario}')
