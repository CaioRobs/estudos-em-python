from contato import Contato


class Agenda():
    def adicionar(nome, telefone, email, twitter, instagram):
        return Contato(nome, telefone, email, twitter, instagram)

    def buscar(contatos, nome):
        for contato in contatos:
            if contato.getNome() == nome:
                print(f'{contato.getNome()} | {contato.getTelefone()} | {contato.getEmail()} | {contato.getTwitter()} | {contato.getInstagram()}')
                break

    def deletarContato(contatos, nome):
        if len(contatos) != 0:
            contador = 0
            for contato in contatos:
                if contato.getNome() == nome:
                    contatos.pop(contador)
                    return 'Contado {nome} removido com sucesso!'
                else:
                    return 'Nome não encontrado!'
                contador += 1
        else:
            return 'Lista está vazia!'
