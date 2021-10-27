from Domain.cheltuiala2 import create_cheltuiala, get_id, get_nr_apartament, get_suma, get_data, get_tip


def test_domain():
    c = create_cheltuiala("345", 5, 210.7, "11.05.2021", "canal")
    assert get_id(c) == "345"
    assert get_nr_apartament(c) == 5
    assert get_suma(c) == 210.7
    assert get_data(c) == "11.05.2021"
    assert get_tip(c) == "canal"
