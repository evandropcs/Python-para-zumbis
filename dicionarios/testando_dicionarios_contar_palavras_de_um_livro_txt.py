import string

texto = open('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/alice.txt').read().lower()

for pontuacao in string.punctuation:
    texto = texto.replace(pontuacao, ' ')

palavras = texto.split()

wc = {}

for p in palavras:
    if p in wc:
        wc[p] += 1
    else:
        wc[p] = 1

def contador(dupla):
    return dupla[1]

duplas = sorted(wc.items(), key=contador, reverse=True)

for dupla in duplas[:20]:
    print(dupla[0], dupla[1])
