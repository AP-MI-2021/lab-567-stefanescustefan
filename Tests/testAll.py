from Tests.testDomain import test_domain
from Tests.testCRUD import test_add_cheltuiala, test_remove_cheltuiala, test_update_cheltuiala


def test_all():
    test_domain()
    test_add_cheltuiala()
    test_remove_cheltuiala()
    test_update_cheltuiala()
