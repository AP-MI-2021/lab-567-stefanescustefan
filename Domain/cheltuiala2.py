def create_cheltuiala(id, nr_apartament, suma, data, tipul):
    """
    Creeaza o cheltuiala

    :param id: string
    :param nr_apartament: int
    :param suma: float
    :param data: string
    :param tipul: string
    :return: o cheltuiala
    """
    return [id, nr_apartament, suma, data, tipul]


def get_id(cheltuiala):
    """
    Determina id-ul unei cheltuieli

    :param cheltuiala: dictionar
    :return: id
    """
    return cheltuiala[0]


def get_nr_apartament(cheltuiala):
    return cheltuiala[1]


def get_suma(cheltuiala):
    return cheltuiala[2]


def get_data(cheltuiala):
    return cheltuiala[3]


def get_tip(cheltuiala):
    return cheltuiala[4]


def to_string(cheltuiala):
    return f"id: {get_id(cheltuiala)}, numar apartament: {get_nr_apartament(cheltuiala)}, " \
           f"suma: {get_suma(cheltuiala)}, data: {get_data(cheltuiala)}, tip: {get_tip(cheltuiala)}"
