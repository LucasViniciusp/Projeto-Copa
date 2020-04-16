from ler_jogos import *

def times():
    times = []
    for partida in info_jogos():
        if partida['time_casa'] not in times:
            times.append(partida['time_casa'])
        if partida['time_fora'] not in times:
            times.append(partida['time_fora'])
    return times


def qtd_jogos(jogos):
    qtd = len(jogos)
    return qtd


def qtd_jogos_selecao(selecao):
    qtd = 0
    for i in info_jogos():
        if i['time_casa'] == selecao:
            qtd += 1
        elif i['time_fora'] == selecao:
            qtd += 1   
    return qtd


def qtd_jogos_part_name(part):
    possivel = ''
    for jogo in info_jogos():
        if part in jogo['time_casa']:
            if jogo['time_casa'] not in possivel:
                possivel = jogo['time_casa']
        elif part in jogo['time_fora']:
            if jogo['time_fora'] not in possivel:
                possivel = jogo['time_fora']
    return possivel


def finais():
    jogos_final = [] 
    for i in info_jogos():
        if i['fase'] == 'Final':
            	jogos_final.append(i)
    return jogos_final


def jogos_por_placar(a,b):
    jogos = []
    for jogo in info_jogos():
        if int(jogo['time_casa_gols']) == a and int(jogo['time_fora_gols']) == b:
            jogos.append(jogo)
    return jogos


def media_gols_final():
    gols = 0
    for jogo in finais():
        gols += int(jogo['time_casa_gols']); gols += int(jogo['time_fora_gols'])
    media = gols / len(finais())
    return media


def media_gols_ano(ano):
    gols = 0
    jogos = 0
    for jogo in info_jogos():
        if jogo['ano'] == ano:
            jogos += 1
            gols += int(jogo['time_casa_gols']); gols += int(jogo['time_fora_gols'])
    media = gols / jogos
    return media


def ano_copa():
    anos_de_copa = []
    for jogo in info_jogos():
        if jogo['ano'] not in anos_de_copa:
            anos_de_copa.append(jogo['ano'])
    return anos_de_copa


def total_gols(ano=info_jogos()):
    gols = 0
    if ano == info_jogos():
        for jogo in info_jogos():
            gols += int(jogo['time_casa_gols']); gols += int(jogo['time_fora_gols'])
    else:
        for jogo in info_jogos():
            if jogo['ano'] == ano:
                gols += int(jogo['time_casa_gols']); gols += int(jogo['time_fora_gols'])
    return gols


def mais_gols_partida(qtd):
    todos_jogos = info_jogos()
    jogos = []
    for i in range(qtd):
        jogo = {}
        mais_gols = 0
        for partida in todos_jogos:
            saldo = int(partida['time_casa_gols']) + int(partida['time_fora_gols'])
            if saldo > mais_gols:
                mais_gols = saldo
                jogo = partida
        jogos.append(jogo)
        todos_jogos.remove(jogo)
    return jogos


def presenca_gols(selecao):
    gols_feitos = 0
    gols_tomados = 0 
    for partida in info_jogos():
        if partida['time_casa'] == selecao:
            gols_feitos += int(partida['time_casa_gols'])
            gols_tomados += int(partida['time_fora_gols'])
        elif partida['time_fora'] == selecao:
            gols_feitos += int(partida['time_fora_gols'])
            gols_tomados += int(partida['time_casa_gols'])
    return gols_feitos, gols_tomados 

#FUNÇÕES AUXILIARES - MAIN()

def menu_qtd_jogos_selecao():
    print('***** TIMES *****')
    for i in times():
        if i == times()[-1]:
            print(i, '\n')
        else:    
            print(i, end=' | ')
    selecao = input('Digite o nome da seleção: ')
    print('Seleçao',selecao, qtd_jogos_selecao(selecao), 'jogos\n')


def main_part_name():
    nome = input('Digite parte do nome da seleção: ')
    selecao = qtd_jogos_part_name(nome)
    for jogo in info_jogos():
        if jogo['time_casa'] == selecao or jogo['time_fora'] == selecao: 
            print('Copa de',jogo['ano'])
            print(jogo['time_casa'], jogo['time_casa_gols'], 'X', jogo['time_fora_gols'], jogo['time_fora'])
            print('Data:',jogo['datahora'],'\n')


def main_listar_por_placar():
    for final in finais():
        print('Copa de',final['ano'])
        print(final['time_casa'], final['time_casa_gols'], 'X', final['time_fora_gols'], final['time_fora'])
        print('Data:',final['datahora'],'\n')


def main_media_gols_final():
    placar = input('Digite um placar(ex: 3x1): ').split('x')
    jogos = jogos_por_placar(int(placar[0]),int(placar[1]))
    for jogo in jogos:
        print('\nCopa de',jogo['ano'])
        print(jogo['time_casa'], jogo['time_casa_gols'], 'X', jogo['time_fora_gols'], jogo['time_fora'])
        print('Data:',jogo['datahora'],'\n')


def total_gols_n_partidas():
    ano = input('Digite um ano:')
    print()     
    print('Total de gols do ano', str(ano)+':',total_gols(ano))
    print('Total de gols em todas as copas:', total_gols())
    print()


def goleadas_n_selecao():
    qtd = input('Digite N para os N primeiros jogos: ')
    print()
    jogos = mais_gols_partida(int(qtd))
    for jogo in jogos:
        print('Copa de',jogo['ano'])
        print(jogo['time_casa'], jogo['time_casa_gols'], 'X', jogo['time_fora_gols'], jogo['time_fora'])
        print('Data:',jogo['datahora'],'\n')


def total_gols_presenca():
    selecao = input('Digite o Nome da seleção: ')
    print()
    fez, tomou = presenca_gols(selecao)
    print('A seleção', selecao, 'fez:')
    print('Fez:', fez)
    print('Tomou:', tomou)
    print()
