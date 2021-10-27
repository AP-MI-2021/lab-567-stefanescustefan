from Domain.cheltuiala2 import create_cheltuiala, get_id, get_nr_apartament, get_data, get_suma, get_tip


def sterge_cheltuieli_apartament(nr_apartament, lista):
    """
    Sterge cheltuielile asociate apartamentului nr_apartament

    :param nr_apartament: Numarul apartamentului
    :param lista: O lista continand cheltuieli
    :return: Lista fara cheltuielile asociate unui apartament
    """
    return [c for c in lista if get_nr_apartament(c) != nr_apartament]


def adunare_valoare_pentru_data(data, valoare, lista):
    """
    Aduna la toate cheltuielile dintr-o data o valoare

    :param data: Data
    :param valoare: Valoarea adaugata
    :param lista: O lista continand cheltuieli
    :return: Lista noua
    """
    lista_noua = []
    for c in lista:
        if get_data(c) == data:
            cheltuiala_noua = create_cheltuiala(get_id(c), get_nr_apartament(c), get_suma(c)+valoare,
                                                get_data(c), get_tip(c))
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(c)
    return lista_noua
