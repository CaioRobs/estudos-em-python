dados = {"rex": ["biscoito", "agua", "racao"], "fifi": ["agua", "racao"]}

caes = list(dados.keys())

for cao in caes:
    print(f'A ultima refeicao de {cao} foi: ')
    refeicoes = dados[cao]
    for refeicao in refeicoes:
        print(refeicao)
    print()
