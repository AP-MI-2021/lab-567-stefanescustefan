from Domain.cheltuiala2 import get_nr_apartament, get_suma, get_tip
from Logic.CRUD import add_cheltuiala, retrieve_cheltuiala
from Logic.functions import sterge_cheltuieli_apartament, adunare_valoare_pentru_data, cea_mai_mare_cheltuiala, \
    ordonare_desc_suma, suma_lunara_ap, do_undo, do_redo


def test_sterge_cheltuieli_apartament():
    lista = []
    undo_list = []
    redo_list = []
    lista = add_cheltuiala("101", 2, 57.9, "3.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("103", 6, 96.8, "15.06.2021", "intretinere", lista, undo_list, redo_list)
    lista = add_cheltuiala("105", 5, 87.6, "17.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("106", 5, 103.4, "29.06.2021", "alte cheltuieli", lista, undo_list, redo_list)

    lista = sterge_cheltuieli_apartament(5, lista, undo_list, redo_list)
    assert len(lista) == 2
    assert retrieve_cheltuiala("102", lista) is None
    assert retrieve_cheltuiala("105", lista) is None
    assert retrieve_cheltuiala("106", lista) is None
    assert get_nr_apartament(retrieve_cheltuiala("101", lista)) == 2


def test_adunare_valoare_pentru_o_data():
    lista = []
    undo_list = []
    redo_list = []
    lista = add_cheltuiala("101", 2, 57.9, "12.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("103", 6, 96.8, "15.06.2021", "intretinere", lista, undo_list, redo_list)
    lista = add_cheltuiala("105", 5, 87.6, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("106", 5, 103.4, "29.06.2021", "alte cheltuieli", lista, undo_list, redo_list)

    lista = adunare_valoare_pentru_data("12.06.2021", 5.0, lista, undo_list, redo_list)
    assert len(lista) == 5
    assert get_suma(retrieve_cheltuiala("101", lista)) == 62.9
    assert get_suma(retrieve_cheltuiala("102", lista)) == 101.8
    assert get_suma(retrieve_cheltuiala("105", lista)) == 92.6
    assert get_suma(retrieve_cheltuiala("103", lista)) == 96.8
    assert get_suma(retrieve_cheltuiala("106", lista)) == 103.4


def test_cea_mai_mare_cheltuiala():
    lista = []
    undo_list = []
    redo_list = []
    lista = add_cheltuiala("101", 2, 57.9, "12.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("103", 6, 96.8, "15.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("105", 5, 87.6, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("106", 5, 103.4, "29.06.2021", "alte cheltuieli", lista, undo_list, redo_list)

    assert get_suma(cea_mai_mare_cheltuiala("canal", lista)) == 96.8
    assert get_nr_apartament(cea_mai_mare_cheltuiala("canal", lista)) == 5
    assert cea_mai_mare_cheltuiala("intretinere", lista) is None
    assert get_suma(cea_mai_mare_cheltuiala("alte cheltuieli", lista)) == 103.4
    assert get_nr_apartament(cea_mai_mare_cheltuiala("alte cheltuieli", lista)) == 5


def test_ordonare_desc_suma():
    lista = []
    undo_list = []
    redo_list = []
    lista = add_cheltuiala("101", 2, 57.9, "12.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("103", 6, 96.8, "15.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("105", 5, 87.6, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("106", 5, 103.4, "29.06.2021", "alte cheltuieli", lista, undo_list, redo_list)

    lista = ordonare_desc_suma(lista)

    assert len(lista) == 5
    assert get_nr_apartament(lista[0]) == 5
    assert get_suma(lista[1]) == 96.8
    assert get_suma(lista[2]) == 96.8
    assert get_nr_apartament(lista[3]) == 5
    assert get_tip(lista[3]) == "canal"
    assert get_suma(lista[4]) == 57.9


def test_suma_lunara_ap():
    lista = []
    undo_list = []
    redo_list = []
    lista = add_cheltuiala("101", 2, 57.9, "12.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "intretinere", lista, undo_list, redo_list)
    lista = add_cheltuiala("103", 6, 96.8, "15.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("104", 2, 62.3, "24.07.2021", "intretinere", lista, undo_list, redo_list)
    lista = add_cheltuiala("105", 5, 87.6, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("106", 5, 103.4, "29.06.2021", "alte cheltuieli", lista, undo_list, redo_list)

    assert int(suma_lunara_ap(lista, 5, 6)) == 287
    assert suma_lunara_ap(lista, 2, 6) == 57.9
    assert suma_lunara_ap(lista, 6, 7) == 0
    assert suma_lunara_ap(lista, 2, 7) == 62.3


def test_undo_redo():
    lista = []
    undo_list = []
    redo_list = []

    lista = add_cheltuiala("101", 2, 57.9, "12.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "intretinere", lista, undo_list, redo_list)
    lista = add_cheltuiala("103", 6, 96.8, "15.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("104", 2, 62.3, "24.07.2021", "intretinere", lista, undo_list, redo_list)
    lista = add_cheltuiala("105", 5, 87.6, "12.06.2021", "canal", lista, undo_list, redo_list)
    lista = add_cheltuiala("106", 5, 103.4, "29.06.2021", "alte cheltuieli", lista, undo_list, redo_list)

    lista = do_undo(undo_list, redo_list, lista)
    assert len(lista) == 5

    lista = do_redo(undo_list, redo_list, lista)
    assert len(lista) == 6

    assert do_redo(undo_list, redo_list, lista) is None

    lista = sterge_cheltuieli_apartament(2, lista, undo_list, redo_list)
    lista = adunare_valoare_pentru_data("12.06.2021", 3.3, lista, undo_list, redo_list)

    lista = do_undo(undo_list, redo_list, lista)
    assert get_suma(lista[0]) == 96.8
    assert get_suma(lista[2]) == 87.6

    lista = do_redo(undo_list, redo_list, lista)
    assert len(lista) == 4
    assert get_suma(lista[0]) == 100.1
    assert int(get_suma(lista[2])) == 90
