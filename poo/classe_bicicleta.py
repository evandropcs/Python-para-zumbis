class Bicicleta():
    def __init__(self):
        self.cor = 'rosa'
        self.rodas = 2
        self.banco = 1
        self.lanterna = 1
        self.campainha = 1
        self.velocidade = 0

    def pedalar(self):
        self.velocidade += 5

    def freiar(self):
        self.velocidade = 0

    def pintar(self, cor_nova):
        self.cor = cor_nova

minha_caloi10 = Bicicleta()
# minha_caloi10.lanterna = False
# minha_caloi10.pintar('Preto')



class Caloi10(Bicicleta):
    def __init__(self):
        Bicicleta.__init__(self)
        self.cor = "Preto"
        self.lanterna = False
        self.marcha = 1

    def troca_marcha(self, marcha):
        self.marcha = marcha

    def pedalar(self):
        if self.marcha == 1:
            self.velocidade += 2
        elif self.marcha == 2:
            self.velocidade += 3
        elif self.marcha == 3:
            self.velocidade += 4
        else:
            self.velocidade += 5


meu_sirizinho = Caloi10()
#
# meu_sirizinho.pedalar()
# print(meu_sirizinho.velocidade)
# meu_sirizinho.troca_marcha(2)
# meu_sirizinho.pedalar()
# print(meu_sirizinho.velocidade)
# meu_sirizinho.troca_marcha(3)
# meu_sirizinho.pedalar()
# print(meu_sirizinho.velocidade)
# meu_sirizinho.troca_marcha(4)
# meu_sirizinho.pedalar()
# print(meu_sirizinho.velocidade)
# print(meu_sirizinho.campainha)

print(type(Bicicleta()))
print(type(minha_caloi10))
print(type(Caloi10()))
print(type(meu_sirizinho))