from agenda import Agenda

print('~'*30)
print('\nIniciando Agenda\n')
print('~'*30)

contatos = []

while True:
    print('Cadastrar contato -> 1')
    print('Buscar contato -> 2')
    print('Apagar contato -> 3')
    print('Listar contatos -> 4')
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
        print('~'*30+'\n')

    elif option == 2:
        nome = input('Digite o nome do contato: ')
        print('\n')
        Agenda.buscar(contatos, nome)
        print('~'*30+'\n')

    elif option == 3:
        nome = input('Digite o nome do contato a deletar: ')
        print(Agenda.deletarContato(contatos, nome))
        print('~'*30+'\n')
  