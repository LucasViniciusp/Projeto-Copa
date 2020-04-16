def info_jogos():
    with open('Partidas_CopaMundo_1930_2014.csv' , encoding="ISO-8859-1") as jogos:
        all_games = []
        for i in jogos:
            jogo = i.strip().split(';')
            detalhes_do_jogo = {
                'ano':jogo[0], 'datahora':jogo[1], 'fase':jogo[2], 'estadio':jogo[3], 'cidade':jogo[4],
                'time_casa':jogo[5], 'time_casa_gols':jogo[6], 'time_fora_gols':jogo[7], 'time_fora':jogo[8] 
            }
            if detalhes_do_jogo['ano'] != 'ANO':
                all_games.append(detalhes_do_jogo)
    return all_games

