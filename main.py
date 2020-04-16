from Project_copa import *
from ler_jogos import *
import os 

def main():
    while True:

        menu()
        x = input('Digite a opção: ')

        if x == '1':
            print('\n>> Total de Jogos << \nJogos FIFA:', qtd_jogos(info_jogos()),'\n')

        elif x == '2':
            print('***** TIMES *****')
            for i in times():
                if i == times()[-1]:
                    print(i, '\n')
                else:    
                    print(i, end=' | ')
            selecao = input('Digite o nome da seleção: ')
            print('Seleçao',selecao, qtd_jogos_selecao(selecao), 'jogos\n')

        elif x == '3':
            nome = input('Digite parte do nome da seleção: ')
            selecao = qtd_jogos_part_name(nome)
            for jogo in info_jogos():
                if jogo['time_casa'] == selecao or jogo['time_fora'] == selecao: 
                    print('Copa de',jogo['ano'])
                    print(jogo['time_casa'], jogo['time_casa_gols'], 'X', jogo['time_fora_gols'], jogo['time_fora'])
                    print('Data:',jogo['datahora'],'\n')

        elif x == '4':
            for final in finais():
                print('Copa de',final['ano'])
                print(final['time_casa'], final['time_casa_gols'], 'X', final['time_fora_gols'], final['time_fora'])
                print('Data:',final['datahora'],'\n')
        
        elif x == '5':
            placar = input('Digite um placar(ex: 3x1): ').split('x')
            jogos = jogos_por_placar(int(placar[0]),int(placar[1]))
            for jogo in jogos:
                print('Copa de',jogo['ano'])
                print(jogo['time_casa'], jogo['time_casa_gols'], 'X', jogo['time_fora_gols'], jogo['time_fora'])
                print('Data:',jogo['datahora'],'\n')

        elif x == '6':
            print()
            print('Media de gols de finais:', round(media_gols_final(),2),'\n')

        elif x == '7':
            ano = input('Digite um ano:')
            print()     
            print('Media de gols do ano', str(ano)+':',round(media_gols_ano(ano),2), '\n')

        elif x == '8':            
            ano = input('Digite um ano:')
            print()     
            print('Total de gols do ano', str(ano)+':',total_gols(ano))
            print('Total de gols em todas as copas:', total_gols())
            print()
        elif x == '9':
            qtd = input('Digite N para os N primeiros jogos: ')
            print()
            jogos = mais_gols_partida(int(qtd))
            for jogo in jogos:
                print('Copa de',jogo['ano'])
                print(jogo['time_casa'], jogo['time_casa_gols'], 'X', jogo['time_fora_gols'], jogo['time_fora'])
                print('Data:',jogo['datahora'],'\n')

        elif x == '10':
            selecao = input('Digite o Nome da seleção: ')
            print()
            fez, tomou = presenca_gols(selecao)
            print('A seleção', selecao, 'fez:')
            print('Fez:', fez)
            print('Tomou:', tomou)
            print()

        elif x == '0':
            break

        if input('Enter para continuar...') != '':
            break
        os.system('cls')


if __name__ == '__main__':
    main()