import Agenda

print('~'*30)
print('\nIniciando Agenda\n')
print('~'*30)

contatos = []  # type: list

while True:
    print('Cadastrar contato -> 1')
    print('Buscar contato -> 2')
    print('Apagar contato -> 3')
    print('Atualizar contato -> 4')
    print('Apagar todos os contatos -> 5')
    print('Sair -> 6\n')
    option = int(input('Selecione uma opção: '))
    print('~'*30)

    if option == 1:
        nome = input('Digite o nome: ')
        telefone = int(input('Digite o telefone: '))
        email = input('Digite o email: ')
        twitter = input('Digite o twitter: ')
        instagram = input('Digite o instagram: ')
        contatos.append(Agenda.adicionar(nome, telefone, email, twitter, instagram))
        print('\nContato adicionado')
        print('~'*30+'\n')

    elif option == 2:
        nome = input('Digite o nome do contato: ')
        print()
        Agenda.buscar(contatos, nome)
        print('~'*30+'\n')

    elif option == 3:
        nome = input('Digite o nome do contato a deletar: ')
        print()
        resultado = Agenda.deletarContato(contatos, nome)
        print('~'*30+'\n')

    elif option == 4:
        nome = input('Digite o nome do contato a atualizar: ')
        print()
        Agenda.atualizar(contatos, nome)
        print('Contato atualizado!')
        print('~'*30+'\n')
