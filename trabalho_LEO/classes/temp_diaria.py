from datetime import datetime


class temp_diaria:
    data = []
    precip = []
    maxima = []
    minima = []
    maxima_insol = []
    temp_media = []
    um_relativa = []
    vel_vento = []
    num_dados = 0

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data.append(datetime.strptime(data, '%d/%m/%Y'))

    def get_precip(self):
        return self.precip

    def set_precip(self, precip):
        self.precip.append(precip)

    def get_maxima(self):
        return self.maxima

    def set_maxima(self, maxima):
        self.maxima.append(maxima)

    def get_minima(self):
        return self.minima

    def set_minima(self, minima):
        self.minima.append(minima)

    def get_maxima_insol(self):
        return self.maxima_insol

    def set_maxima_insol(self, maxima_insol):
        self.maxima_insol.append(maxima_insol)

    def get_temp_media(self):
        return self.temp_media

    def set_temp_media(self, temp_media):
        self.temp_media.append(temp_media)

    def get_um_relativa(self):
        return self.um_relativa

    def set_um_relativa(self, um_relativa):
        self.um_relativa.append(um_relativa)

    def get_vel_vento(self):
        return self.vel_vento

    def set_vel_vento(self, vel_vento):
        self.vel_vento.append(vel_vento)

    def count_dados(self):
        self.num_dados = self.num_dados + 1

    def to_string(self):
        for i in range(self.num_dados):
            print(
                f"{self.data[i].strftime('%d/%m/%Y')}: Precipitação - {self.precip[i]}, Temperatura Máxima - {self.maxima[i]},"
                f" Temperatura Mínima - {self.minima[i]}, Máxima Insolação - {self.maxima_insol[i]},"
                f" Temperatura Média - {self.temp_media[i]}, Umidade Relativa - {self.um_relativa[i]}%,"
                f" Velocidade do Vento - {self.vel_vento[i]}")

    def to_string_print(self, i):
        print(
            f"{self.data[i].strftime('%d/%m/%Y')}: Precipitação - {self.precip[i]}, Temperatura Máxima - {self.maxima[i]},"
            f" Temperatura Mínima - {self.minima[i]}, Máxima Insolação - {self.maxima_insol[i]},"
            f" Temperatura Média - {self.temp_media[i]}, Umidade Relativa - {self.um_relativa[i]}%,"
            f" Velocidade do Vento - {self.vel_vento[i]}")

