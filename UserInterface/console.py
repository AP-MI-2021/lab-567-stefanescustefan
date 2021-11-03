from Domain.cheltuiala2 import to_string
from Logic.CRUD import add_cheltuiala, remove_cheltuiala, update_cheltuiala
from Logic.functions import sterge_cheltuieli_apartament, adunare_valoare_pentru_data, cea_mai_mare_cheltuiala


def print_menu():
    print("1. Adauga cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Stergerea tuturor cheltuielilor pentru un apartament")
    print("5. Adauga o valoare tuturor cheltuielilor dintr-o data anume")
    print("6. Afisarea celei mai mare cheltuiala din fiecare tip")
    print("a. Afiseaza toate cheltuielile")
    print("x. Iesire")


def ui_adauga_cheltuiala(lista):
    try:
        id = input("Dati id: ")
        nr_apartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma: "))
        data = input("Dati data: ")
        tipul = input("Dati tipul: ")
        return add_cheltuiala(id, nr_apartament, suma, data, tipul, lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_sterge_cheltuiala(lista):
    try:
        id = input("Dati id: ")
        return remove_cheltuiala(id, lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_modificare_cheltuiala(lista):
    try:
        id = input("Dati id: ")
        nr_apartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma: "))
        data = input("Dati data: ")
        tipul = input("Dati tipul: ")
        return update_cheltuiala(id, nr_apartament, suma, data, tipul, lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_afiseaza_toate(lista):
    for c in lista:
        print(to_string(c))


def ui_sterge_cheltuieli_apartament(lista):
    try:
        nr_apartament = int(input("Dati numarul apartamentului: "))
        return sterge_cheltuieli_apartament(nr_apartament, lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_adauga_valoare_pentru_data(lista):
    try:
        data = input("Dati o data: ")
        valoare = float(input("Dati o valoare: "))
        return adunare_valoare_pentru_data(data, valoare, lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_cea_mai_mare_cheltuiala(lista):
    if cea_mai_mare_cheltuiala("canal", lista) is not None:
        print("C maxim canal: ", to_string(cea_mai_mare_cheltuiala("canal", lista)))

    if cea_mai_mare_cheltuiala("intretinere", lista) is not None:
        print("C maxim intretinere: ", to_string(cea_mai_mare_cheltuiala("intretinere", lista)))

    if cea_mai_mare_cheltuiala("alte cheltuieli", lista) is not None:
        print("C maxim alte cheltuieli: ", to_string(cea_mai_mare_cheltuiala("alte cheltuieli", lista)))


def run_menu():
    lista = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == '1':
            lista = ui_adauga_cheltuiala(lista)
        elif optiune == '2':
            lista = ui_sterge_cheltuiala(lista)
        elif optiune == '3':
            lista = ui_modificare_cheltuiala(lista)
        elif optiune == '4':
            lista = ui_sterge_cheltuieli_apartament(lista)
        elif optiune == '5':
            lista = ui_adauga_valoare_pentru_data(lista)
        elif optiune == '6':
            ui_cea_mai_mare_cheltuiala(lista)
        elif optiune == 'a':
            ui_afiseaza_toate(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiune incorecta")
