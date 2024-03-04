catetoOposto = float(input('Qual o comprimento do cateto oposto: '))
adjacente = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = float (input('Qual o comprimento da hipotenusa: '))

seno = hipotenusa / catetoOposto
cos = hipotenusa / adjacente
tan = catetoOposto / adjacente

print('O valor do seno é {}, o valor do cosseno é {} e o valor da tangente é {}'.format(seno, cos, tan))
