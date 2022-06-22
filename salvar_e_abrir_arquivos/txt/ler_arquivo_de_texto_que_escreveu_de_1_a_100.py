# Versão 1
f = open(r'/x.txt')
for linha in f.readlines():
    print(linha.strip())
f.close()

# Versão 2
with open(r'/x.txt') as f:
    print(f.read())

