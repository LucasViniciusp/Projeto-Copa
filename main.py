from Project_copa import *
import os

def main():
    x = ''
    menu = '1 - Quantidade de Jogos\n' \
    '2 - Quantidade de jogos de uma seleção\n' \
    '3 - Quantidade de Jogos de uma seleção por parte\n' \
    '4 - Listar todos os Jogos da FINAL\n'\
    '5 - Listar jogos por PLACAR\n' \
    '6 - Media de gols da final\n' \
    '7 - Media de gols de um Ano de Copa do Mundo\n' \
    '8 - Total de Gols de N jogos com mais Gols em todas as Copas\n' \
    '9 - exibir Dados de N jogos com mais de uma dada seleção\n' \
    '10 - Total de Gols Feitos e "pegos" de uma dada seleção\n'\
    '0 - Sair\n'\
    'Digite uma Opção: '

    while x != 0:
        x = int(input(menu))

        if x == 1:
            print('\n>> Total de Jogos << \nJogos FIFA:', qtd_jogos(info_jogos()),'\n')
        elif x == 2:
            menu_qtd_jogos_selecao()
        elif x == 3:
            main_part_name()
        elif x == 4:
            main_listar_por_placar()
        elif x == 5:
            main_media_gols_final()
        elif x == 6:
            print()
            print('Media de gols de finais:', round(media_gols_final(),2),'\n')
        elif x == 7:
            ano = input('Digite um ano:')
            print()     
            print('Media de gols do ano', str(ano)+':',round(media_gols_ano(ano),2), '\n')
        elif x == 8:            
            total_gols_n_partidas()
        elif x == 9:
            goleadas_n_selecao()
        elif x == 10:
            total_gols_presenca()
        elif x == 0:
            os.system('cls')
            break

        if input('Enter para continuar...') != '':
            break
        os.system('cls')


if __name__ == '__main__':
    main()