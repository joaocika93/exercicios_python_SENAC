class Avaliacao:
    def __init__(self, marca, nota):
        self.marca = marca
        self.nota = nota

    def set_marca(self, marca):
        self.marca = marca

    def set_nota(self, nota):
        self.nota = nota

    def get_marca(self):
        return self.marca

    def get_nota(self):
        return self.nota
