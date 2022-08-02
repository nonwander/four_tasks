#!/usr/bin/env python3
from task_1 import Technic


class TestTechnic1(Technic):
    def __init__(self, title, price, availability, one, two, three):
        super().__init__(title, price, availability)
        self.title: str = title
        self.price: int = price
        self.availability: str = availability
        self.one = one
        self.two = two
        self.three = three


class TestTechnic2(Technic):
    def __init__(self, title, price, availability):
        super().__init__(title, price, availability)
        self.title: str = title
        self.price: int = price
        self.availability: str = availability

    def new_method(self):
        pass


def test_class_immutability():
    zero = Technic('Zero', 0, False)
    print(zero)
    one = Technic('One', 101, True)
    print(one)
    two = Technic('Two', 202, True)
    print(two)
    assert one < zero, 'Неправильное неравенство <'
    assert one == two, 'Неправильное равенство ='
    try:
        two = TestTechnic1('Two', 202, False, 1, 2, 3)
    except AttributeError as err:
        print(err)
    try:
        tree = TestTechnic2('Three', 303, False)
    except AttributeError as err:
        print(err)


if __name__ == '__main__':
    test_class_immutability()
