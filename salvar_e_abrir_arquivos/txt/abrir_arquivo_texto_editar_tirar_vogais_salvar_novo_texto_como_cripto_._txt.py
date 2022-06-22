texto = open('/texto.txt', 'r')
cripto = open('/cripto.txt', 'w')


for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiou':
            cripto.write('*')
        else:
            cripto.write(letra)

texto.close()
cripto.close()
