# Criar arquivo
# import csv
#
# with open ('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/pessoas.csv','w', newline='') as csvfile:
#     colunas = ['Nome', 'Nota 1', 'Nota 2']
#     writer = csv.DictWriter(csvfile, fieldnames=colunas)
#     writer.writeheader()
#     writer.writerow({'Nome': 'Annie', 'Nota 1': 8.5, 'Nota 2': 7.5})
#     writer.writerow({'Nome': 'Clara', 'Nota 1': 9.5, 'Nota 2': 10})
#
# csvfile.close()

# Abrir arquivo

# import csv
#
# with open('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/pessoas.csv', newline='') as arq:
#     reader = csv.DictReader(arq)
#     for linha in reader:
#         print(linha['Nome'], linha['Nota 1'], linha['Nota 2'])

