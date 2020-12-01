from trabalho_03.domain.Estado import Estado


class Cidade:
    def __init__(self):
        self._nome = ""
        self._estado = Estado()
        self._qt_casos = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def qt_casos(self):
        return self._qt_casos

    @qt_casos.setter
    def qt_casos(self, qt_casos):
        self._qt_casos = self._qt_casos + qt_casos
        self._estado.qt_estado = self._estado.qt_estado + qt_casos
