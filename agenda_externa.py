import json


def gravar(dicionario):
    with open('agenda_externa' + '.json', 'w') as f:
        json.dump(dicionario, f, indent=2)
        f.close()


def ler():
    agenda_externa = {}
    try:
        with open('agenda_externa' + '.json', 'r') as f:
            agenda_externa = json.load(f)
            f.close()
            return agenda_externa
    except FileNotFoundError:
        gravar(agenda_externa)
        return agenda_externa


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

    elif '2' in inp:
        salvar_contato()

    elif '3' in inp:
        parar = stop()
        if parar:
            continue

    parar = stop()
