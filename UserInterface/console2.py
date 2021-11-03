from Domain.cheltuiala2 import to_string
from Logic.CRUD import add_cheltuiala, remove_cheltuiala, update_cheltuiala
from Logic.functions import sterge_cheltuieli_apartament, adunare_valoare_pentru_data, cea_mai_mare_cheltuiala


def print_help():
    print("add,<id>,<nr_ap>,<suma>,<data>,<tipul> - Adauga o cheltuiala")
    print("del,<id> - Sterge o cheltuiala")
    print("update,<id>,<nr_ap>,<suma>,<data>,<tipul> - Modifica o cheltuiala")
    print("del_ap,<nr_ap> - Sterge toate cheltuielile asociate apartamentului dat")
    print("add_val,<data>,<val> - Adauga o valoare tuturor cheltuielilor dintr-o data")
    print("largest,<tip> - Cea mai mare cheltuiala de un anumit tip")
    print("showall - Afiseaza toate cheltuielile")
    print("quit - Iesire")


def ui_showall(lista):
    for c in lista:
        print(to_string(c))


def ui_add(args, lista):
    try:
        if len(args) != 6:
            raise ValueError("Insuficiente argumente")
        return add_cheltuiala(args[1], int(args[2]), float(args[3]), args[4], args[5], lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_del(args, lista):
    try:
        if len(args) != 2:
            raise ValueError("Insuficiente argumente")
        return remove_cheltuiala(args[1], lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_update(args, lista):
    try:
        if len(args) != 6:
            raise ValueError("Insuficiente argumente")
        return update_cheltuiala(args[1], int(args[2]), float(args[3]), args[4], args[5], lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_del_ap(args, lista):
    try:
        if len(args) != 2:
            raise ValueError("Insuficiente argumente")
        return sterge_cheltuieli_apartament(int(args[1]), lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_add_val(args, lista):
    try:
        if len(args) != 3:
            raise ValueError("Insuficiente argumente")
        return adunare_valoare_pentru_data(args[1], float(args[2]), lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_largest_tip(args, lista):
    try:
        if len(args) != 2:
            raise ValueError("Insuficiente argumente")
        if args[1] not in ['canal', 'intretinere', 'alte cheltuieli']:
            raise ValueError("Tip invalid")
        print(to_string(cea_mai_mare_cheltuiala(args[1], lista)))
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def run_menu():
    print_help()
    done = False
    lista = []
    while not done:
        cmd_line = input("Introduceti comenzi: ")
        cmd_list = cmd_line.split(";")
        for command in cmd_list:
            args = command.strip().split(",")
            cmd_title = args[0]
            if cmd_title == 'quit':
                done = True
            elif cmd_title == 'showall':
                ui_showall(lista)
            elif cmd_title == 'add':
                lista = ui_add(args, lista)
            elif cmd_title == 'del':
                lista = ui_del(args, lista)
            elif cmd_title == 'update':
                lista = ui_update(args, lista)
            elif cmd_title == 'del_ap':
                lista = ui_del_ap(args, lista)
            elif cmd_title == 'add_val':
                lista = ui_add_val(args, lista)
            elif cmd_title == 'largest':
                ui_largest_tip(args, lista)
            else:
                print("Comanda nerecunoscuta ignorata")
