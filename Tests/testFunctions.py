from Domain.cheltuiala2 import get_nr_apartament, get_suma
from Logic.CRUD import add_cheltuiala, retrieve_cheltuiala
from Logic.functions import sterge_cheltuieli_apartament, adunare_valoare_pentru_data


def test_sterge_cheltuieli_apartament():
    lista = []
    lista = add_cheltuiala("101", 2, 57.9, "3.06.2021", "alte cheltuieli", lista)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "canal", lista)
    lista = add_cheltuiala("103", 6, 96.8, "15.06.2021", "intretinere", lista)
    lista = add_cheltuiala("105", 5, 87.6, "17.06.2021", "canal", lista)
    lista = add_cheltuiala("106", 5, 103.4, "29.06.2021", "alte cheltuieli", lista)

    lista = sterge_cheltuieli_apartament(5, lista)
    assert len(lista) == 2
    assert retrieve_cheltuiala("102", lista) is None
    assert retrieve_cheltuiala("105", lista) is None
    assert retrieve_cheltuiala("106", lista) is None
    assert get_nr_apartament(retrieve_cheltuiala("101", lista)) == 2


def test_adunare_valoare_pentru_o_data():
    lista = []
    lista = add_cheltuiala("101", 2, 57.9, "12.06.2021", "alte cheltuieli", lista)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "canal", lista)
    lista = add_cheltuiala("103", 6, 96.8, "15.06.2021", "intretinere", lista)
    lista = add_cheltuiala("105", 5, 87.6, "12.06.2021", "canal", lista)
    lista = add_cheltuiala("106", 5, 103.4, "29.06.2021", "alte cheltuieli", lista)

    lista = adunare_valoare_pentru_data("12.06.2021", 5.0, lista)
    assert len(lista) == 5
    assert get_suma(retrieve_cheltuiala("101", lista)) == 62.9
    assert get_suma(retrieve_cheltuiala("102", lista)) == 101.8
    assert get_suma(retrieve_cheltuiala("105", lista)) == 92.6
    assert get_suma(retrieve_cheltuiala("103", lista)) == 96.8
    assert get_suma(retrieve_cheltuiala("106", lista)) == 103.4
