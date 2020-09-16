from trabalho_01.domain.Avaliacao import Avaliacao


class Avaliador:
    def __init__(self, nome):
        self.nome = nome
        self.avaliacao = []

    def set_nome(self, nome):
        self.nome = nome

    def set_avaliacao(self, avaliacao):
        self.avaliacao.append(avaliacao)

    def get_nome(self):
        return self.nome

    def get_avaliacao(self):
        list_avaliacao = []
        for avaliacao in self.avaliacao:
            list_avaliacao.append(avaliacao.get_marca())
            list_avaliacao.append(avaliacao.get_nota())

        return list_avaliacao

    def get_notas(self, marca):
        for avaliacao in self.avaliacao:
            if marca == avaliacao.get_marca():
                return avaliacao.get_nota()
