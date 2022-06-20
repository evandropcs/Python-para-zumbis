texto = open('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/texto.txt', 'r')
cripto = open('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/cripto.txt', 'w')


for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiou':
            cripto.write('*')
        else:
            cripto.write(letra)

texto.close()
cripto.close()
