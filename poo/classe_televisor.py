class Televisor():
    def __init__(self):
        self.tamanho = '60 polegadas'
        self.cor = 'preto/cinza'
        self.resolucao = 'UHD'
        self.conexao = 'Wifi'
        self.volume = 0
        self.transmisssao = 'inativo'
        self.canal = 'sem canal'

    def ligar(self):
        self.volume = 1
        self.transmisssao = 'ativo'

    def desligar(self):
        self.volume = 0
        self.transmisssao = 'inativo'
        self.canal = 'sem canal'

    def mudar_canal(self, canal: int):
        self.canal = canal


    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1


baratinha = Televisor()
baratinha.ligar()
# print(baratinha.transmisssao)
# print(baratinha.volume)
baratinha.mudar_canal(13)

baratinha.aumentar_volume()
baratinha.aumentar_volume()
baratinha.aumentar_volume()
baratinha.aumentar_volume()
baratinha.aumentar_volume()
baratinha.diminuir_volume()
baratinha.diminuir_volume()
baratinha.diminuir_volume()
baratinha.diminuir_volume()
baratinha.desligar()
print(baratinha.canal)
print(baratinha.transmisssao)
print(baratinha.volume)

