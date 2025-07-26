from core.objects.Game import Game

jogo = Game(difficulty='easy', auto_clear=True)
# Difficulty é literalmente o 'modo' do jogo: russian_rolet/baby/easy/medium/hard/insane/custom
# Caso não queira um mapa pré feito usando o parâmetro difficulty pode indicar um mapa usando o parâmetro map que recebe um objeto da classe Map (objects.Map)
# O parâmetro auto_clear revela blocos com 0 ou 1 bombas em volta logo no inicio. Com exceção do modo Hard, Insano (False) e Baby (True) por padrão

jogo.start_game() # Para startar o jogo.