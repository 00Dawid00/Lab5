def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        zakres = "Niedowaga"
    elif 18.5 <= bmi < 25:
        zakres = "Pożądana masa ciała"
    elif 25 <= bmi < 30:
        zakres = "Nadwaga"
    elif 30 <= bmi < 35:
        zakres = "Otyłość I stopnia"
    elif 35 <= bmi < 40:
        zakres = "Otyłość II stopnia"
    else:
        zakres = "Otyłość III stopnia"

    return bmi, zakres


waga = float(input("Podaj wagę (kg): "))
wzrost = float(input("Podaj wzrost (m): "))

bmi, zakres = oblicz_bmi(waga, wzrost)
print(f"Twoje BMI wynosi: {bmi:.2f}")
print(f"Klasyfikacja BMI: {zakres}")
