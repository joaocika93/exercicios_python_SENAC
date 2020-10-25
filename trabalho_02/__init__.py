# Trabalho 02 - Algoritmos e programação 1
# Senac
# João Marcos Castro dos Santos


from trabalho_01.domain.Avaliacao import Avaliacao
from trabalho_01.domain.Avaliador import Avaliador
from trabalho_01.util.Notas import Notas
from trabalho_01.util.Refrigerantes import Refrigerantes

list_avaliadores = []
list_produtos = []
notas = {}
pesquisa = {}
notas_totais = {Refrigerantes.COCACOLA.value: 0, Refrigerantes.GUARANA.value: 0, Refrigerantes.PEPSI.value: 0,
                Refrigerantes.FANTA.value: 0, Refrigerantes.SPRITE.value: 0}


def busca_arquivo():
    carregar_marcas = open("marcas.txt", "r")
    carregar_notas = open("notas.txt", "r")

    marcas = str(carregar_marcas.readline()).split(";")
    notas_marcas = str(carregar_notas.readline()).split(";")

    for marca in marcas:
        list_produtos.append(marca)

    count = 0
    for i in range(len(notas_marcas)):
        if count == len(notas_marcas):
            break
        notas[notas_marcas[count]] = notas_marcas[count+1]
        count = count + 2

    carregar_marcas.close()
    carregar_notas.close()


def salvar_dicionario():
    salvar_avaliacao = open("avaliacao.txt", "w")
    salvar_avaliacao.write(str(pesquisa.items()))

    salvar_avaliacao.close()


def cadastrar_avaliador():
    avaliador = Avaliador(input("Digite o nome do avaliador: ").upper())
    for avaliadores in list_avaliadores:
        if avaliador.get_nome() == avaliadores.get_nome():
            print('Avaliador já cadastrado')
            break
    else:
        list_avaliadores.append(avaliador)
        pesquisa[avaliador.get_nome()] = []


def realizar_avaliacao():
    name_avaliador = input('Nome do avaliador: ').upper()
    for avaliador in list_avaliadores:
        if avaliador.get_nome() == name_avaliador:
            print(list_produtos)
            choice_product = input("Escolha a marca a ser avaliado: ").upper()
            if choice_product in list_produtos:
                list_avaliador = avaliador.get_list_avaliacao()
                if choice_product not in list_avaliador:
                    print(notas)
                    nota = input("Escolha nota da sua avaliação: ")
                    if nota in notas.values():
                        avaliacao = Avaliacao(choice_product, nota)
                        avaliador.set_avaliacao(avaliacao)
                        pesquisa[avaliador.get_nome()] = avaliador.get_avaliacao()
                        break
                    else:
                        print("Nota inválida")
                        break
                else:
                    print("Produto já Avaliado")
                    break
            else:
                print("Marca inválida")
                break
    else:
        print("Avaliador não cadastrado")


def relatorio_avaliadores():
    print(pesquisa)


def relatorio_produtos():
    for avaliadores in pesquisa:
        for marca in list_produtos:
            if marca in pesquisa[avaliadores]:
                for avaliador in list_avaliadores:
                    if avaliadores == avaliador.get_nome():
                        soma_nota = avaliador.get_notas(marca)
                        soma_nota += notas_totais[marca]
                        notas_totais[marca] = soma_nota
                else:
                    soma_nota = 0

    print(notas_totais)


def main():
    busca_arquivo()
    while True:
        choice = input(
            "Menu:\n0 - Finalizar programa\n1 - Cadastrar avaliador\n"
            "2 - Realizar avaliação\n3 - Relatório de avaliadores\n4 - Relatório de produtos\nOpção: ")

        if choice == '0':
            salvar_dicionario()
            break
        elif choice == '1':
            cadastrar_avaliador()
        elif choice == '2':
            realizar_avaliacao()
        elif choice == '3':
            relatorio_avaliadores()
        elif choice == '4':
            relatorio_produtos()
        else:
            print("Opção inválida")


if __name__ == '__main__':
    main()
