largura = float(input('Qual seria a largura dessa parede em metros?'))
altura = float(input('Qual seria a altura dessa parede em metros?'))
area = largura * altura
quantidadeTinta = area /2

print('A área da parede é de {:.2f} metros quadrados.'.format(area))
print('Você precisará de {:.2f} litros de tinta para pintá-la.'.format(quantidadeTinta))