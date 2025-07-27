from core.objects.Game import Game

jogo = Game(difficulty='baby')
# Difficulty é literalmente o 'modo' do jogo: russian_rolet/baby/easy/medium/hard/insane/custom
# Caso não queira um mapa pré feito usando o parâmetro difficulty pode indicar um mapa usando o parâmetro 'map' que recebe um objeto da classe Map (objects.Map)
# O parâmetro auto_clear da classe Map revela blocos com 0 ou 1 bombas em volta logo no inicio. Ele vem desabilitado nos modos Hard, Insano (False) e habilitado em todos os outros. No custom você pode selecionar se quer ele ligado ou desligado.

# Para startar o jogo.
# -> jogo.start_game() 


# --- Jogo Básico --- #
while True:
    disk_mode = input("Digite o número correspondente a dificuldade que deseja jogar:\n\n1-Baby\n2-Easy\n3-Medium\n4-Hard\n5-Insane\n6-Russian Rolet\n7-Custom\n\nAqui:     ")

    if disk_mode == '1':
        jogo = Game(difficulty='baby')
    elif disk_mode == '2':
        jogo = Game(difficulty='easy')
    elif disk_mode == '3':
        jogo = Game(difficulty='medium')
    elif disk_mode == '4':
        jogo = Game(difficulty='hard')
    elif disk_mode == '5':
        jogo = Game(difficulty='insane')
    elif disk_mode == '6':
        jogo = Game(difficulty='russian_rolet')
    elif disk_mode == '7':
        jogo = Game(difficulty='custom')
    else:
        print('\nEntrada Inválida. Tente novamente.\n')
        continue

    input('''
----TUTORIAL----
O jogo terá um campo composto por blocos, o campo possui bombas espalhadas em blocos aleatorios. Sua missão é evitar as bombas, selecionando apenas os blocos sem bombas. Cada bloco seguro mostrará o número de bombas ao redor dele (8 blocos em volta), se ele mostrar 00, significa que não possui nenhuma bomba em volta por exemplo. Quando você tiver certeza que um bloco for uma bomba, digite FL bloco (EX: FL A1), isso colocará uma flag no bloco, para tirar a flag basta fazer a mesma coisa. Você ganha o jogo quando todos os blocos seguros estiverem ativos e todas as bombas estiverem com flag.  Você pode parar o jogo digitando 'stop'. Caso ative uma bomba o jogo também será encerrado.
          

(Pressione ENTER para prosseguir)
''')
    jogo.start_game()

    restart = input('Deseja jogar novamente (Se sim, digite "sim" se não, pressione ENTER):    ')
    if restart == 'sim':
        continue
    else:
        break