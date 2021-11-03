from Tests.testDomain import test_domain
from Tests.testCRUD import test_add_cheltuiala, test_remove_cheltuiala, test_update_cheltuiala
from Tests.testFunctions import test_sterge_cheltuieli_apartament, test_adunare_valoare_pentru_o_data, test_cea_mai_mare_cheltuiala


def test_all():
    test_domain()
    test_add_cheltuiala()
    test_remove_cheltuiala()
    test_update_cheltuiala()

    test_sterge_cheltuieli_apartament()
    test_adunare_valoare_pentru_o_data()
    test_cea_mai_mare_cheltuiala()
