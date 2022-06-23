def abrir_arq(caminho_arq: str):
    with open(caminho_arq, 'r') as arquivo:
        for texto in arquivo:
            if 'Simple' in texto:
                with open('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/funcoes/criar_abrir_manipular_txt_gerar_novo_arq/zen2.txt', 'w') as arq:
                    arq.write(texto)
                    arq.close()
        arquivo.close()


arquivo = abrir_arq('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/funcoes/criar_abrir_manipular_txt_gerar_novo_arq/zen.txt')


