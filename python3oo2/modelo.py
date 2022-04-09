class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes}'


class filme(programa):
    def __init__(self, nome, ano, duracao ):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} Duração - {self.likes}'

class serie(programa):

    def __init__(self, nome, ano, temporada ):
        super().__init__(nome,ano)
        self.temporada = temporada

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporada} Temporada - {self.likes}'

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = filme('vingadores-guerra infinita', 2018, 160)

atlanta = serie('atlanta', 2018, 2)
tmep = filme("todo mundo em panico", 1999, 100)
demolidor = serie("Demolido", 2016, 2)

vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_series)

print(f'Tamanho do Playlist {len(playlist_fim_de_semana)}')

for program in playlist_fim_de_semana:
    print(program)

print(f'Tem demolidor na minha playlist : {demolidor in playlist_fim_de_semana}')

print(playlist_fim_de_semana)


#for programa in filmes_series:
#    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada
#    print(f'{programa.nome} - {detalhes} D - {programa.likes}')

