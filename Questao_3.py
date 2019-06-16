altura = float(input('Informe sua altura: '))
sexo = int(input('Digite seu sexo: (1)Para mulher (2)Para homem: '))

if sexo == 1:
    pessoa = (62.1 * altura) - 44.7

elif sexo == 2:
    pessoa = (72.7 * altura) - 58

    
print ("Seu peso é: ", pessoa)
