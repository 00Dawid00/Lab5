def powitanie(imie="Użytkowniku", jezyk="dpolski"):
    if jezyk == "polski":
        print(f"Cześć, {imie}.")
    elif jezyk == "angielski":
        print(f"Hello, {imie}.")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}.")
    else:
        print(f"Witaj, {imie}.")

powitanie("Anna", "polski")
powitanie("John", "angielski")
powitanie("Hans", "niemiecki")
powitanie("Kylian", "francuski")
powitanie()
