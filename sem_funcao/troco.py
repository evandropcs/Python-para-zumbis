conta = 122
pagamento = 200
troco = pagamento - conta
troco_notas = []
notas = [50, 20, 10, 5, 2, 1]
print(f'O troco é de {troco:4.2f} R$')
for nota in notas:
    if troco >= nota:
        troco_notas.append(nota)
        print(f'Uma nota de {nota:6.2f} R$')
        troco -= nota

