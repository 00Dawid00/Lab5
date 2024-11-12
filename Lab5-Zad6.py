import math

def pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Nieprawidłowe długości boków")

    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

try:
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))

    wynik = pole_trojkata(a, b, c)
    print("Pole trójkąta:", wynik)

except ValueError as e:
    print(e)
