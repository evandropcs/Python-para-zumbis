from collections import OrderedDict
d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['span'] = 3
d['grok'] = 4


for chave, valor in d.items():
    print(chave, valor)
