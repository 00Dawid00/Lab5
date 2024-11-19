def potega(a, n):
    if n == 0:
        return 1
    else:
        return a * potega(a, n - 1)

a = float(input("Podaj liczbę a: "))
n = int(input("Podaj wykładnik n: "))

wynik = potega(a, n)
print(f'{a} do potęgi {n} wynosi {wynik}')
