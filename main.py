print("""Witaj w programie!
Wybierz z następujących opcji:
1 - Sprawdź czy dane nazwisko istnieje w bazie
2 - Dodaj nazwisko pracownika do bazy
3 - Wyświetl wszytkie nazwiska
""")

list_of_surnames = ["Kowalska", "Rajczyk", "Porębski"]

while True:

    option = int(input("Proszę wybierz opcję (1-3): "))


    if option == 1:
        surname = str(input("Proszę podaj nazwisko do wyszukania: "))
        if surname in list_of_surnames:
            print("Podane nazwisko znajduje się w badnie")
        elif surname not in list_of_surnames:
            print("Podanego nazwiska nie ma w bazie")

    if option == 2:
        surname = str(input("Proszę podaj nazwisko, które chcesz dodać do bazy: "))
        if surname not in list_of_surnames:
            list_of_surnames.append(surname)
            print("Nazwisko zostało dodane do bazy")
        elif surname in list_of_surnames:
            print("Takie nazwisko istnieje już w bazie!")

    if option == 3:
        list_of_surnames.sort()
        print(list_of_surnames)


