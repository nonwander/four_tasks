"""This module consists of class 'Technic'.
It definds the type of product by its cost and generate
property 'category' (cheep/expensive).
It unavailable to add any other attributes and methods.

Exceptions:
    AttributeError -- raises when modified attributes and methods
        in Child classes of Technic class.
"""
from functools import total_ordering
from typing import Any, Optional


# TODO: fix immutability solution in class Technic with metaclass.
class ProtectAttrsMethodsMetaclass(type):
    """The metaclass provides immutability for attributes and methods."""
    def __new__(meta_cls, cls_name, cls_bases, cls_attrs):
        cls = super().__new__(meta_cls, cls_name, cls_bases, cls_attrs)
        return cls

    def __setattr__(self, key, value):
        super().__setattr__(key, value)


@total_ordering
class Technic:
    """The class of any technic product.
    """
    _PRICE_THRESHOLD: int = 100
    _CATEGORY: tuple[str, str] = ('cheep', 'expensive', 'undefined')
    _ALLOWED_ATTRS: list[str] = ['title', 'price', 'availability']
    _ALLOWED_METHODS: list[str] = ['get_cls_attrs', 'category']

    def __new__(cls, *attrs):
        err_message = 'Unavailable to create object with method:'
        pulled_methods: list[str] = (
            [i for i in cls.__dict__.keys() if i[:1] != '_']
        )
        not_allowed = list(set(cls._ALLOWED_METHODS) ^ set(pulled_methods))
        if not_allowed:
            raise AttributeError(f'{err_message} {", ".join(not_allowed)}!')
        return super().__new__(cls)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name not in Technic._ALLOWED_ATTRS:
            print(f'ERROR! Attribute "{__name}" is not avalible to create!')
        return super().__setattr__(__name, __value)

    def __eq__(self, other):
        if self.__validate_type(other):
            return len(self.title) == len(other.title)

    def __lt__(self, other):
        if self.__validate_type(other):
            return len(self.title) < len(other.title)

    def __validate_type(self, other) -> bool:
        """Checks whether instances match the Technic type.
        Arguments:
            other -- second instance of Technic type.
        Raises:
            TypeError: raises if instance is not of Technic type.
        Returns:
            boolean value that depends of validation result.
        """
        err_msg: str = 'invalid type of the instance!'
        try:
            if isinstance(other, self.__class__):
                return True
            else:
                raise TypeError(err_msg)
        except TypeError as err:
            print(f'Error: {err}')
            return False

    @classmethod
    def get_cls_attrs(cls):
        return cls.__dict__.items()

    def __init__(self, title: str, price: int, availability: bool) -> None:
        """Creates an object.
        Arguments:
            title -- string;
            price -- foat;
            availability -- boolean.
        """
        self.title: str = title
        self.price: int = price
        self.availability: bool = availability

    @property
    def category(self) -> Optional[str]:
        """Get or set the current value for Cell's particle.
        New value will valideted according to range of price.
        Arguments:
            particle -- value of cell's elementary particles in integer.
        Returns:
            'undefined' -- if price is not set;
            category -- string type variant of Category.
        """
        if self.price:
            result = self._CATEGORY[1] if (
                self.price > self._PRICE_THRESHOLD
            ) else self._CATEGORY[0]
            return result
        else:
            return self._CATEGORY[2]

    def __str__(self) -> str:
        """Represents a Technic object as its contents.
        Returns:
            a string of all contents.
        """
        return (
            f'Title: {self.title}\n'
            f'Price: {self.price}\n'
            f'Available: {self.availability}\n'
            f'Category: {self.category}\n'
        )
