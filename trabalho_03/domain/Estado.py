class Estado:
    def __init__(self):
        self._nome_estado = ""
        self._sigla = ""
        self._pais = "BRASIL"
        self._qt_estado = 0

    @property
    def nome_estado(self):
        return self._nome_estado

    @nome_estado.setter
    def nome_estado(self, nome_estado):
        self._nome_estado = nome_estado

    @property
    def sigla(self):
        return self._sigla

    @sigla.setter
    def sigla(self, sigla):
        self._sigla = sigla

    @property
    def qt_estado(self):
        return self._qt_estado

    @qt_estado.setter
    def qt_estado(self, qt_estado):
        self._qt_estado = qt_estado