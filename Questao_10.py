Nome_Usuario = str(input('Informe o seu nome de usuário: '))
Senha = str(input('Informe a sua senha: '))

while (Nome_Usuario == Senha):
    print("ERRO")
    Nome_Usuario = str(input('Informe o seu nome de usuário: '))
    Senha = str(input('Informe a sua senha: '))

else:
    print ("PARABÉNSSSSS!")
