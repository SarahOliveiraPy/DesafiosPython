salario = float(input('Digite o seu salario?'))
porcentagemAumento = 0.15
aumento = salario + (salario * 15/ 100)
novoSalario = salario + aumento

print('O seu novo salario será de {:.3f}'.format(aumento))
