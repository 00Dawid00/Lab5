def srednia(lista):
    return sum(lista) / len(lista)

liczby = [1, 2, 3, 4, 5, 6, 10]
wynik = srednia(liczby)
print("Liczby w liście",liczby)
print("Średnia tych liczb:", wynik)
