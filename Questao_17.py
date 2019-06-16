def int(n):
    return len((str(n)))

n = str(input('Informe um número: ')).strip()
print(f'A quantidade de dígitos foram: {int(n)}')
