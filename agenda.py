import json


def gravar(dicionario):
    with open('agenda' + '.json', 'w') as f:
        json.dump(dicionario, f, indent=2)
        f.close()


def ler():
    agenda = {}
    try:
        with open('agenda' + '.json', 'r') as f:
            agenda = json.load(f)
            f.close()
            return agenda
    except FileNotFoundError:
        gravar(agenda)
        return agenda


def salvar_contato():
    nome = input('Name: ')
    telefone = input('Phone number: ')
    dicionario = ler()
    dicionario[nome] = telefone
    gravar(dicionario)


def ver_contatos():
    dicionario = ler()
    for (chave, valor) in dicionario.items():
        print(f'{chave}: {valor}')


def stop():
    p = input('Close? [y/n]: ')
    if 'y' in p:
        return True


parar = False
while not parar:
    inp = input('See contacts= 1 | New contact= 2 | Close= 3 | Your option: ')
    if '1' in inp:
        ver_contatos()

    if '2' in inp:
        salvar_contato()

    if '3' in inp:
        parar = stop()
        if parar:
            continue

    parar = stop()
