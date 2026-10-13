class Nota:
    def __init__(self, nome, notas, media, aprovado, n1, n2):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.media = media
        self.aprovado = aprovado

    def analisar_notas(n1, n2):
        media = n1+n2

        aprovados = 0
        for n in media:
            if n >= 7.0:
                aprovado += 1
            if n <= 7.0:
                reprovado -= 1
        return media, aprovado, reprovado

    def calcular_media(self, media):
        print(f"seu nome {self.nome} | sua media foi: {media:.2f} | voce foi: {self.aprovado} ")


    