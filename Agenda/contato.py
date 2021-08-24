class Contato():
    def __init__(self, nome, telefone, email, twitter, instagram):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__twitter = twitter
        self.__instagram = instagram

    def getNome(self):
        return self.__nome

    def getTelefone(self):
        return self.__telefone

    def getEmail(self):
        return self.__email

    def getTwitter(self):
        return self.__twitter

    def getInstagram(self):
        return self.__instagram
