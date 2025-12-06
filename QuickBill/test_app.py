from app import check_input, check_item, create_bill
import pytest
import os


def test_order():
    assert check_item("soda") == {'name': 'soda', 'price': 1.49}
    assert check_item("pdkfd") == False
    assert check_item("apple") == False
    assert check_item("pizza") == {'name': 'pizza', 'price': 8.99}

def test_input():
    with pytest.raises(ValueError):
        check_input("3 pizza")
        check_input("1soda")
        check_input("123")
        

def test_file():
    test_list = [{'name': 'pizza', 'price': 8.99}]
    total = 8.99
    create_bill(test_list, total)
    assert os.path.exists("bill.txt")
