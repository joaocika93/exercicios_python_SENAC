import csv
import sys
from datetime import datetime

from classes.temp_diaria import temp_diaria
from utils.constantes import constantes

temp = temp_diaria()


def valida_filtro(mes_inicial, mes_final, ano_incial, ano_final):
    if mes_inicial > 12 or mes_final > 12:
        return False, 'mes inválido'
    elif ano_incial > ano_final:
        return False, 'o ano inicial deve ser menor que o ano final'
    elif ano_incial == ano_final and mes_inicial > mes_final:
        return False, 'o mes inicial deve ser menor que o mes final'

    return True, ' '


def menu():
    print("[1] - Exibir dados por tempo (mês e ano iniciais e mês e ano finais.)\n"
          "[2] - Exibir todos os dados\n"
          "[3] - Exibir apenas os dados de precipitação\n"
          "[4] - Exibir apenas os dados de temperatura\n"
          "[5] - Exibir apenas os dados de vento e umidade\n"
          "[6] - Exibir apenas os dados de máxima insolação\n"
          "[0] - Sair do programa\n")
    return int(input("Opção: "))


def exibir_dados_filtrado(dado):
    global i
    exibir_dados = None
    ano_inicial = int(input("ano inicial:"))
    mes_inicial = int(input("mes inicial:"))
    ano_final = int(input("ano final:"))
    mes_final = int(input("mes final:"))

    validado, erro = valida_filtro(mes_inicial, mes_final, ano_inicial, ano_final)

    if validado:
        for i, date_dia in enumerate(temp.get_data()):
            if date_dia.year == ano_inicial and date_dia.month == mes_inicial:
                exibir_dados = True
            elif date_dia.year == ano_final and date_dia.month == mes_final:
                break

            if exibir_dados and dado == constantes.TODOS_DADOS:
                temp.to_string_print(i)
            elif exibir_dados and dado == constantes.PRECIP:
                print(f"Precipitação - {temp.get_precip()[i]}")
            elif exibir_dados and dado == constantes.TEMPERATURA:
                print(f"Temperatura Máxima - {temp.get_maxima()[i]}\n"
                      f"Temperatura Mínima - {temp.get_minima()[i]}")
            elif exibir_dados and dado == constantes.MAXIMA_INSOL:
                print(f"Máxima Insolação - - {temp.get_maxima_insol()[i]}")
            elif exibir_dados and dado == constantes.VENTO_UMIDADE:
                print(f"Velocidade do Vento - {temp.get_vel_vento()[i]}\n"
                      f"Umidade Relativa - {temp.get_um_relativa()[i]}")

    else:
        print(erro)


def set_atributos(diaria):
    temp.set_data(diaria[0])
    temp.set_precip(diaria[1])
    temp.set_maxima(diaria[2])
    temp.set_minima(diaria[3])
    temp.set_maxima_insol(diaria[4])
    temp.set_temp_media(diaria[5])
    temp.set_um_relativa(diaria[6])
    temp.set_vel_vento(diaria[7])
    temp.count_dados()


def leitura_csv():
    nome_ficheiro = 'temp.csv'
    with open(nome_ficheiro, 'r') as ficheiro:
        reader = csv.reader(ficheiro)
        try:
            for linha in reader:
                if reader.line_num != 1:
                    set_atributos(linha)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))


if __name__ == '__main__':
    leitura_csv()
    rodar = True
    while rodar:
        opcao = menu()
        if opcao == 1:
            exibir_dados_filtrado(constantes.TODOS_DADOS)
        elif opcao == 2:
            temp.to_string()
        elif opcao == 3:
            exibir_dados_filtrado(constantes.PRECIP)
        elif opcao == 4:
            exibir_dados_filtrado(constantes.TEMPERATURA)
        elif opcao == 5:
            exibir_dados_filtrado(constantes.VENTO_UMIDADE)
        elif opcao == 6:
            exibir_dados_filtrado(constantes.MAXIMA_INSOL)
        elif opcao == 0:
            break
