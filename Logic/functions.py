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


def cea_mai_mare_cheltuiala(tip, lista):
    """
    Returneaza cele mai mari cheltuieli pentru fiecare tip

    :param tip: Tipul cheltuielii
    :param lista: Lista de cheltuieli
    :return: Cheltuiala cea mai mare de tipul dat
    """

    if not any(get_tip(c) == tip for c in lista):
        return None

    return max([c for c in lista if get_tip(c) == tip], key=lambda c: get_suma(c))


def ordonare_desc_suma(lista):
    """
    Returneaza lista ordonata descrescator dupa suma

    :param lista: Lista de cheltuieli
    :return: Lista ordonata descrescator
    """

    return sorted(lista, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)


def suma_lunara_ap(lista, ap, luna):
    """
    Determina sumele lunare pentru un apartament si o luna

    :param lista: Lista de cheltuieli
    :param ap: Apartamentul
    :param luna: Luna
    :return: Suma cheltuielilor dintr-o luna pentru un apartament
    """
    suma = 0
    for c in lista:
        if get_nr_apartament(c) == ap and int(get_data(c).split(".")[1]) == luna:
            suma = suma + get_suma(c)

    return suma
