texto = '''
Mussum Ipsum, cacilds! vidis litro abertis. 
Nec orci ornare consequat. 
Praesent lacinia' ultrices consectetur. 
Sed non ipsum felis.
Cevadis im? ampola pa arma uma pindureta.
Não sou faixa preta cumpadi, sou preto inteiris;, inteiris.
Praesent# vel viverra nisi. 
Mauris aliquet@ nunc non turpis %scelerisque, eget.
'''

print(texto)

from string import punctuation

for pontuacao in punctuation:
    if pontuacao in texto and pontuacao != '.':
        texto = texto.replace(pontuacao, "")
print(texto)

