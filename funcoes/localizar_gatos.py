def achei_um_gato(dic, coord):
    for nome, coordenada in dic.items():
        if coordenada == coord:
            print(nome, coordenada)

coord_gatos = {'Pompom': (1, 1), 'mingau': (4, 0), 'Fifi': (2, 4), 'Fofona': (4, 0)}

if __name__ == '__main__':

    print(achei_um_gato(coord_gatos, (4, 0)))
    print(achei_um_gato(coord_gatos, (10, 10)))


