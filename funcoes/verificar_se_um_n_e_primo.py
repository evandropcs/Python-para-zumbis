def e_primo(n):
    x = 2
    while x < n:
        if n % x == 0:
            return n, 'Não é primo'
        return n, 'É primo'
    x += 1


print(e_primo(77))
