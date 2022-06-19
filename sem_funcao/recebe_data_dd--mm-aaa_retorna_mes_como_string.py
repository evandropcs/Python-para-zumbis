mes = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'.split()


data = input('Escolha uma data, use o formato: DD/MM/AAAA: ')

d, m, a = data.split('/')

print(f'{d} de {mes[(int(m))-1]} de {a}')
