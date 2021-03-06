from Domain.cheltuiala2 import create_cheltuiala, get_id


def add_cheltuiala(id, nr_apartament, suma, data, tipul, lista, undo_list, redo_list):
    """
    Adauga o cheltuiala in lista

    :param id: id
    :param nr_apartament: Numar apartament
    :param suma: Suma
    :param data: Data
    :param tipul: Tipul cheltuielii (intretinere, canal, alte cheltuieli)
    :param lista: Lista de cheltuieli
    :param undo_list: Lista undo
    :param redo_list: Lista redo
    :return: Noua lista
    """
    if retrieve_cheltuiala(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    cheltuiala = create_cheltuiala(id, nr_apartament, suma, data, tipul)

    undo_list.append(lista)
    redo_list.clear()

    return lista + [cheltuiala]


def remove_cheltuiala(id, lista, undo_list, redo_list):
    """
    Sterge o cheltuiala cu id-ul dat

    :param id: Id de sters
    :param lista: Lista de cheltuieli
    :param undo_list
    :param redo_list
    :return: Lista fara elementul cu id-ul dat
    """
    if retrieve_cheltuiala(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat!")

    undo_list.append(lista)
    redo_list.clear()

    return [c for c in lista if get_id(c) != id]


def update_cheltuiala(id, nr_apartament, suma, data, tipul, lista, undo_list, redo_list):
    """
    Modifica o cheltuiala dupa id

    :param id: id-ul cheltuielii de modificat
    :param nr_apartament: nr apartament
    :param suma: noua suma
    :param data: noua data
    :param tipul: noul tip
    :param lista: Lista de cheltuieli
    :param undo_list
    :param redo_list
    :return: Lista cu elementul modificat
    """
    if retrieve_cheltuiala(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat!")
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            cheltuiala_noua = create_cheltuiala(id, nr_apartament, suma, data, tipul)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)

    undo_list.append(lista)
    redo_list.clear()

    return lista_noua


def retrieve_cheltuiala(id, lista):
    """
    Gaseste cheltuiala cu id-ul dat

    :param id:
    :param lista: Lista de cheltuieli
    :return: Cheltuiala cu id-ul dat
    """
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None
