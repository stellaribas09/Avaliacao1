Salario = float(input('Informe o seu salário: '))
if Salario <280:
    aumento = (Salario * 0.2) + Salario
    valor_aumento = (Salario * 0.2)
    print ("Seu percentual foi de 20%")
               
elif Salario >=280 and Salario <700:
    aumento = (Salario * 0.15) + Salario
    valor_aumento = (Salario * 0.15)
    print ("Seu percentual foi de 15%")
    
elif Salario >=700 and Salario <1500:
    aumento = (Salario * 0.1) + Salario
    valor_aumento = (Salario * 0.1)
    print ("Seu percentual foi de 10%")
    
elif Salario >1500:
    aumento = (Salario * 0.05) + Salario
    valor_aumento = (Salario * 0.05)
    print ("Seu percentual foi de 5%")

print ("Seu salário antes do reajuste: R$ ", Salario)
print ("O salário após o aumento foi de: R$", aumento)
print ("O valor do aumento foi de: R$", valor_aumento)

    
               
