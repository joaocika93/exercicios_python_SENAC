# Trabalho 03 - Algoritmos e programação 1
# Senac
# João Marcos Castro dos Santos


from trabalho_03.domain.Cidade import Cidade
from trabalho_03.domain.Estado import Estado

list_estado = []
list_cidade = []


def escolhe_estado():
    for estado in list_estado:
        print("Estado --- " + estado.nome_estado + " ----- " + estado.sigla)

    escolha = input("Escolha o estado digitando a sigla: ").upper()

    for estado in list_estado:
        if estado.sigla == escolha:
            return estado
    else:
        return "Sigla não valida"


def popular_estados():
    try:
        estados_upload = open("casos_estados.txt", "r")

        estados = str(estados_upload.read()).replace("\n", "").split("|")
        count = 0
        length = int(len(estados) / 3)
        for i in range(length):
            obj_estado = Estado()
            obj_estado.nome_estado = estados[count]
            obj_estado.sigla = estados[count + 1]
            obj_estado.qt_estado = int(estados[count + 2])
            list_estado.append(obj_estado)
            count = count + 3
        list = list_estado
        estados_upload.close()
    except NameError:
        print("Erro ao carregar estados")


def popular_cidade():
    try:
        cidade_upload = open("casos_cidades.txt", "r")

        cidades = str(cidade_upload.read()).replace("\n", "").split("|")
        count = 0
        length = int(len(cidades) / 3)
        for i in range(length):
            obj_cidade = Cidade()
            obj_cidade.nome = cidades[count]
            for estado in list_estado:
                if estado.sigla == cidades[count + 1]:
                    obj_cidade.estado = estado
                    break
            obj_cidade.qt_casos = int(cidades[count + 2])
            list_cidade.append(obj_cidade)
            count = count + 3

        cidade_upload.close()
    except NameError:
        print("Erro ao carregar estados")


def cadastrar_estados():
    estado_sigla = input("Digite a sigla do estado: ").upper()
    for estados in list_estado:
        if estado_sigla == estados.sigla:
            print("Estado já cadastrado")
            return False

    estado = Estado()
    estado.sigla = estado_sigla
    estado.nome_estado = input("Digite o nome do Estado: ")
    list_estado.append(estado)


def cadastrar_cidades():
    if len(list_estado) > 0:
        cidade_nome = input("Digite o nome da cidade: ")
        for cidades in list_cidade:
            if cidades.nome == cidade_nome:
                print("Cidade já cadastrada")
                return False

        estado = escolhe_estado()
        if estado != "Sigla não valida":
            cidade = Cidade()
            cidade.nome = cidade_nome
            cidade.estado = estado
            list_cidade.append(cidade)
        else:
            print("Cidade não cadastrada")
    else:
        print("Cadastre pelo menos um Estado")


def relatorio_estados():
    if len(list_estado) > 0:
        for estado in list_estado:
            print("---> " + estado.sigla + "........ - total de casos: " + estado.nome_estado)
    input("[ENTER] Retorna ao menu.")


def relatorio_cidades():
    if len(list_cidade) > 0:
        for cidade in list_cidade:
            print("---> " + cidade.nome + "........ - Casos Registrados: " + str(cidade.qt_casos))
    input("[ENTER] Retorna ao menu.")


def atualiza_casos():
    if len(list_cidade) > 0:
        nome_cidade = input("Digite o nome da cidade que deseja atualizar o numero de casos: ")
        for cidade in list_cidade:
            if nome_cidade == cidade.nome:
                casos = int(input("Digite a nova quantidade de casos: "))

                if casos > 0:
                    cidade.qt_casos = casos
                    break
                else:
                    print("A quantidade não pode ser negativa")
                    break
    else:
        print("Cadastre pelo menos uma cidade")


def salva_relatorio():
    try:
        estado_save = open("casos_estados.txt", "w")
        cidade_save = open("casos_cidades.txt", "w")

        for estado in list_estado:
            estado_save.write(estado.nome_estado + "|" + estado.sigla + "|" + str(estado.qt_estado) + "|\n")

        for cidade in list_cidade:
            cidade_save.write(cidade.nome + "|" + cidade.estado.sigla + "|" + str(cidade.qt_casos) + "|\n")

    except NameError:
        print("Erro ao salvar as informações")


def main():
    popular_estados()
    popular_cidade()
    list = list_estado
    list2 = list_cidade
    print()
    while True:
        choice = input(
            "Menu:\n0 - Finalizar programa\n1 - Cadastrar Estados\n"
            "2 - Cadastrar Cidades\n3 - Relatório de Estados\n4 - Relatório de Cidades\n5 - Atualizar Numero de "
            "Casos\nOpção: ")

        if choice == '0':
            salva_relatorio()
            break
        elif choice == '1':
            cadastrar_estados()
        elif choice == '2':
            cadastrar_cidades()
        elif choice == '3':
            relatorio_estados()
        elif choice == '4':
            relatorio_cidades()
        elif choice == '5':
            atualiza_casos()
        else:
            print("Opção inválida")


if __name__ == '__main__':
    main()
