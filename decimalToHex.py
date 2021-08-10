mensagem = "Valor decimal: {0}\nValor Hexadecial: {1}"

print('Programa para converter de decimal pra hexa\n')

num_dec = int(input('Digite um número: '))
print()

num_hex = format(num_dec, 'X')

print(mensagem.format(num_dec, num_hex))
