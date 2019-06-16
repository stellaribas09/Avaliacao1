contador = 0
resp = str(input('Telefonou para a vítima? '))
if resp == 'sim' or resp == 's' :
    contador = contador + 1
else:
    contador = contador + 0
resp = str(input('Esteve no local do crime? '))
if resp == 'sim' or resp == 's':
    contador = contador + 1
else:
    contador = contador + 0
resp = str(input('Mora perto da vítima? '))
if resp == 'sim' or resp == 's':
    contador = contador + 1
else:
    contador = contador + 0
resp = str(input('Devia para a vítima? '))
if resp == 'sim' or resp == 's':
    contador = contador + 1
else:
    contador = contador + 0
resp = str(input('Já trabalhou com a vítima? '))
if resp == 'sim' or resp == 's':
    contador = contador + 1
else:
    contador = contador + 0
if contador == 2:
    print("Suspeita")
if contador == 3 or contador == 4:
    print("Cúmplice")
if contador == 5:
    print("Assassino")
if contador == 0:
    print("Inocente")
