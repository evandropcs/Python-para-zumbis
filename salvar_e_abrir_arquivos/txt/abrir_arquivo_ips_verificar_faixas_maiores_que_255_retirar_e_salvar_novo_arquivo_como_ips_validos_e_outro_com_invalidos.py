def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True


arq = open('/ips.txt')
ips_validos = open('/ips_validos.txt', 'w')
ips_invalidos = open('/ips_invalidos.txt', 'w')


for linha in arq.readlines():
    if ip_ok(linha):
        ips_validos.write(linha)
    else:
        ips_invalidos.write(linha)


arq.close()
ips_validos.close()
ips_invalidos.close()


