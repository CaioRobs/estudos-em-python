op_validos = ['+', '-', '/', '*']

while True:
    e = input('Digite o primeiro valor: ')
    op = input(f'Digite o operador (opções: {op_validos}): ')
    d = input('Digite o segundo valor: ')
    if op in op_validos and e.isnumeric() and d.isnumeric():
        if op == '/' and d == '0':
            print('Divisão por 0! Tente novamente.')
            continue
        expressao = e + ' ' + op + ' ' + d
        print(e, op, d, '=', eval(expressao))
        break
    print('Valores ou operador incorreto!')
    continue
