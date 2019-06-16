print("Até 5 Kg: Morango R$ 2,50 por Kg")
print ("Acima de 5 Kg: Morango  R$ 2,20 por Kg")
print ("Até 5 Kg: Maçã R$ 1,80 por Kg")
print ("Acima de 5 Kg: Maçã R$ 1,50 por Kg")



Quant_Morangos = int(input('Quantidade de morangos: '))
Quant_Maçã = int(input('Quantidade de maçãs: '))

if Quant_Morangos <= 5:
    Valor_Morangos = Quant_Morangos * 2.50
if Quant_Morangos > 5:
    Valor_Morangos = Quant_Morangos * 2.20
if Quant_Maçã <= 5:
    Valor_Maçã = Quant_Maçã * 1.80
if Quant_Maçã > 5:
    Valor_Maçã = Quant_Maçã * 1.50

Quant_total = Quant_Maçã + Quant_Morangos
Valor_total = Valor_Maçã + Valor_Morangos
if Quant_total <= 8:
    print (Quant_total)

if Valor_total <= 25:
    print (Valor_total)

if Quant_total > 8:
    print (Quant_total)


if Valor_total > 25:
    Valor_total = Valor_total + (Valor_total * 0.1)

