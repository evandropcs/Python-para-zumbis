# Versão 1
f = open(r'/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/x.txt')
for linha in f.readlines():
    print(linha.strip())
f.close()

# Versão 2
with open(r'/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/x.txt') as f:
    print(f.read())

