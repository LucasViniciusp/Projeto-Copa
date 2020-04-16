from ler_jogos import info_jogos

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

def menu():
    print('**** FIFA 1930 -- 2014 *****')
    print('1 - Quantidade de Jogos')
    print('2 - Quantidade de jogos de uma seleção')
    print('3 - Quantidade de Jogos de uma seleção por parte')
    print('4 - Listar todos os Jogos da FINAL')
    print('5 - Listar jogos por PLACAR')
    print('6 - Media de gols da final')
    print('7 - Media de gols de um Ano de Copa do Mundo')
    print('8 - Total de Gols de N jogos com mais Gols em todas as Copas')
    print('9 - exibir Dados de N jogos com mais de uma dada seleção')
    print('10 - Total de Gols Feitos e "pegos" de uma dada seleção')
    print('0 - Sair')
