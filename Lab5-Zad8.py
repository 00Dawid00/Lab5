#A
def wyswietl_parametry(*args):
    print("Podane parametry:", args if args else "Brak parametrów")

wyswietl_parametry(1, 2, 3, 4, 5, 6)
wyswietl_parametry()
print("\n\n")

#B
def wyswietl_i_znajdz_maks(*args):
    print("Podane parametry:", args if args else "Brak parametrów")
    if args:
        maks = max(args)
        print(f'Maksymalna wartość to: {maks}')
        return maks

wyswietl_i_znajdz_maks(1, 2, 3, 4, 5, 6)
wyswietl_i_znajdz_maks()

