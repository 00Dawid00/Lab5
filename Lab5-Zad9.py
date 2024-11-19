def fibonacci(n):
    if n <= 0:
        return "Podaj liczbę większą od zera."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Podaj n-ty wyraz ciągu Fibonacciego: "))
print(f'{n}-ty wyraz ciągu Fibonacciego to: {fibonacci(n)}')
