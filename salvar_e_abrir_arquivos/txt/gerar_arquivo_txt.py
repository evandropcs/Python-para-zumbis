def escreve_novo_zen():
    # Abre arquivo Zen
    with open('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/salvar_e_abrir_arquivos/txt/zen.txt', 'r') as conteudo:
        for x in conteudo:
            print(x)
            if "Simple" in x:
                with open('/home/evandrosilva/Workspace/logica-programacao/outros_projetos/python_para_zumbis/salvar_e_abrir_arquivos/txt/zen2.txt', 'w') as arq:
                    arq.write(f'{x}')
                    print(x)
                    arq.close()

        conteudo.close()







