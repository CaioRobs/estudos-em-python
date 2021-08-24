from contato import Contato


class Agenda():
    def adicionar(nome, telefone, email, twitter, instagram):
        return Contato(nome, telefone, email, twitter, instagram)

    def buscar(contatos, nome):
        if len(contatos) != 0:
            for contato in contatos:
                if contato.getNome() == nome:
                    print(f'{contato.getNome()} | {contato.getTelefone()} | {contato.getEmail()} | {contato.getTwitter()} | {contato.getInstagram()}')
                    return
            print('Contato não encontrado!\n')
        else:
            print('Lista está vazia!')

    def deletarContato(contatos, nome):
        if len(contatos) != 0:
            contador = 0
            for contato in contatos:
                if contato.getNome() == nome:
                    contatos.pop(contador)
                    print(f'Contato {nome} removido com sucesso!')
                    return
                contador += 1
            print('Contato não encontrado!')
        else:
            print('Lista está vazia!')

    def atualizar(contatos, nome):
        if len(contatos) != 0:
            for contato in contatos:
                if contato.getNome() == nome:
                    print('Selecione um dado para ser atualizado')
                
            print('Contato não encontrado')
        else:
            print('Lista está vazia!')
