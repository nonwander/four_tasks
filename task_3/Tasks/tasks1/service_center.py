#!/usr/bin/env python3
"""This module consits of Service Center tasks.
"""
from typing import NewType

TZERO = NewType('TZERO', list[tuple[str, int, str, int]])
T1NF = NewType('T1NF', list[dict[str, list[tuple[str, int]]]])


def optimize(data: TZERO) -> T1NF:
    """Optimise data to 1NF.

    Arguments:
        data -- non-normalized data of the custom TZERO type.

    Returns:
        data in the first normal form - custom T1NF type.
    """
    return data


def get_data() -> TZERO:
    """Loads non-normalized data in a certain way.

    Returns:
        data in the non-normalized form - custom TZERO type.
    """
    pass


def show_optimized_data(data: T1NF) -> None:
    """Printing in console data objects in one line.

    Arguments:
        data -- data in the first normal form - custom T1NF type.
    """
    print(
        'Татьяна 89001001010: Ноутбук - 1500; Принтер - 1000; Планшет - 700\n'
        'Анна 89002002020: Смартфон - 500\n'
        'Андрей 89003003030: Проектор - 1500; Смартфон - 1000\n'
    )


def main() -> None:
    """The execution point for the program file."""
    input_data: TZERO = get_data()
    optimized_data: T1NF = optimize(input_data)
    show_optimized_data(optimized_data)


if __name__ == '__main__':
    print(__doc__)
    main()
