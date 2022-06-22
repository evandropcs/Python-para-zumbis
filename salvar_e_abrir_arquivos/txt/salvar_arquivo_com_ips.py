f = open(r'/ips.txt', 'w')
texto = '''
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.284.5
192.168.0.256
'''

# Retira o /n para corrigir o erro gerado na execução do arquivo:
# abrir_arquivo_ips_verificar_faixas_maiores_que_255_retirar_e_salvar_novo_arquivo_como_ips_validos_e_outro_com_invalidos
# na hora de verificar se int(byte) > 255
# ValueError: invalid literal for int() with base 10:
texto = texto.strip()


f.write(texto)
f.close()

