from Domain.cheltuiala import get_nr_apartament


def sterge_cheltuieli_apartament(nr_apartament, lista):
    """
    Sterge cheltuielile asociate apartamentului nr_apartament

    :param nr_apartament: Numarul apartamentului
    :param lista: O lista continand cheltuieli
    :return: Lista fara cheltuielile asociate unui apartament
    """
    return [c for c in lista if get_nr_apartament(c) != nr_apartament]
