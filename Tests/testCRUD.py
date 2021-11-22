from Logic.CRUD import add_cheltuiala, remove_cheltuiala, update_cheltuiala, retrieve_cheltuiala
from Domain.cheltuiala2 import get_id, get_nr_apartament, get_suma, get_data, get_tip


def test_add_cheltuiala():
    lista = []
    undo_lista = []
    redo_lista = []
    lista = add_cheltuiala("129", 9, 100.6, "1.04.2021", "canal", lista, undo_lista, redo_lista)
    assert len(lista) == 1
    assert get_id(retrieve_cheltuiala("129", lista)) == "129"
    assert get_nr_apartament(retrieve_cheltuiala("129", lista)) == 9
    assert get_suma(retrieve_cheltuiala("129", lista)) == 100.6
    assert get_data(retrieve_cheltuiala("129", lista)) == "1.04.2021"
    assert get_tip(retrieve_cheltuiala("129", lista)) == "canal"


def test_remove_cheltuiala():
    lista = []
    undo_list = []
    redo_list = []
    lista = add_cheltuiala("101", 2, 57.9, "3.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "canal", lista, undo_list, redo_list)

    lista = remove_cheltuiala("102", lista, undo_list, redo_list)
    assert len(lista) == 1
    assert retrieve_cheltuiala("102", lista) is None

    try:
        lista = remove_cheltuiala("43", lista, undo_list, redo_list)
        assert False
    except ValueError as ve:
        assert len(lista) == 1
    except Exception as e:
        assert False

    assert retrieve_cheltuiala("101", lista) is not None


def test_update_cheltuiala():
    lista = []
    undo_list = []
    redo_list = []
    lista = add_cheltuiala("101", 2, 57.9, "3.06.2021", "alte cheltuieli", lista, undo_list, redo_list)
    lista = add_cheltuiala("102", 5, 96.8, "12.06.2021", "canal", lista, undo_list, redo_list)

    lista = update_cheltuiala("102", 5, 113.2, "13.06.2021", "intretinere", lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_id(retrieve_cheltuiala("102", lista)) == "102"
    assert get_nr_apartament(retrieve_cheltuiala("102", lista)) == 5
    assert get_suma(retrieve_cheltuiala("102", lista)) == 113.2
    assert get_data(retrieve_cheltuiala("102", lista)) == "13.06.2021"
    assert get_tip(retrieve_cheltuiala("102", lista)) == "intretinere"
