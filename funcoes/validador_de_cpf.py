
num = input('Digite os 11 numeros do seu cpf: ')


# Dados gerais

cpf = str(num)
digitos_9 = cpf[0:9]
digitos_finais = cpf[9:]

# Validar primeiro digito

sequencia_padrao = list(range(10, 1, -1))
sequencia_criada_1 = []
x = 0
while x < 9:
    sequencia_criada_1.append(int(digitos_9[x]) * int(sequencia_padrao[x]))
    x += 1
primeiro_digito = str((sum(sequencia_criada_1) * 10) % 11)
if primeiro_digito == 10:
    primeiro_digito = 0

# Validar segundo digito

digitos_10 = digitos_9 + digitos_finais[0]
sequencia_padrao_2 = list(range(11, 1, -1))
# sequencia_padrao_2 = sequencia_padrao_2[::-1]
sequencia_criada_2 = []
x = 0
while x < 10:
    sequencia_criada_2.append(int(digitos_10[x]) * int(sequencia_padrao_2[x]))
    x += 1
segundo_digito = str((sum(sequencia_criada_2) * 10) % 11)
if segundo_digito == 10:
    segundo_digito = 0

def validar(dig_1, val_1, dig_2, val2):
    if dig_1 == val_1 and dig_2 == val2:
        print(f'O CPF {num} é Válido')
    else:
        print(f'O CPF {num} é inválido')

validar(digitos_finais[0], primeiro_digito, digitos_finais[1],  segundo_digito)




