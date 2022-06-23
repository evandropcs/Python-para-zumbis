import string

caracters = string.punctuation

texto = open('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/eva.txt').read()


for pontuacao in caracters:
    livro = texto.replace(pontuacao, " ")

def contar_palavras(texto):
    contador = {}
    for palavra in texto.split():
        if palavra not in contador:
            contador[palavra] = 1
        else:
            contador[palavra] += 1
    return contador


contador_dicionario = (contar_palavras(livro))


for palavras, quantidades in contador_dicionario.items():
    print(palavras, quantidades)
