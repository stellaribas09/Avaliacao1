Salario_Hora = float(input('Quanto você ganha por hora: R$ '))
Horas_Trabalhadas = float(input('Quantas horas você trabalha por mês: '))
Salario_Bruto = Salario_Hora * Horas_Trabalhadas

print ("Seu salário bruto é R$:", Salario_Bruto)

Salario_Descontado = (Salario_Bruto * 0.11) + (Salario_Bruto * 0.08) + (Salario_Bruto * 0.05)
Salario_Liquido = Salario_Bruto - Salario_Descontado
print ("Seu salário líquido é R$:", Salario_Liquido)

Pagamento_INSS = Salario_Bruto * 0.08
print ("Seu pagamento ao INSS é de R$:", Pagamento_INSS)

Pagamento_Sindicato = Salario_Bruto * 0.05
print ("Seu pagamento ao Sindicato é de R$:", Pagamento_Sindicato)





