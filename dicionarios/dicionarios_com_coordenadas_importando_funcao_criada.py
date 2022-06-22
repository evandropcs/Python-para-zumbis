from funcoes.funcoes_para_dicionarios import mostrar_chaves, mostrar_items, mostrar_valores

coordenadas = {
(1, 1): 'cafeteria', (300, 990): 'pet shop',
(2, 4): {'1 andar': None, '2 andar': ['restaurante', 'bar', 'banheiros'],
'3 andar': 'estacionamento'}, (5 , 100, 400000): 'topo da colina'
}

if __name__ == '__main__':
    mostrar_chaves(coordenadas)
    mostrar_valores(coordenadas)
    mostrar_items(coordenadas)