#!/usr/bin/env python3
"""This module consits of Service Center tasks.
"""
from typing import NewType, Union
from collections import defaultdict

TZERO = NewType('TZERO', list[tuple[str, int, str, int]])
T1NF = NewType('T1NF', list[dict[str, list[tuple[str, int]]]])


def optimize(data: TZERO) -> T1NF:
    """Optimise data to 1NF.

    Arguments:
        data -- non-normalized data of the custom TZERO type.

    Returns:
        optimized data in the first normal form - custom T1NF type.
    """
    keys = [f'{item[2]} {item[3]}' for item in data]
    values = [(item[0], item[1]) for item in data]
    pre_data = defaultdict(list)
    optimized_data = [
        {key: pre_data[key]} for key in
        {key: pre_data[key].append(val) for key, val in zip(keys, values)}
    ]
    return optimized_data


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
    def formatter(object: Union[list, dict, tuple, int, str]) -> str:
        if type(object) is dict:
            items: list[str] = [
                str(key) + ': ' + formatter(object[key])
                for key in object
            ]
            return f'{"".join(items)[:-2]}\n'
        elif type(object) is list:
            items: list[str] = [
                formatter(item)
                for item in object
            ]
            return f'{"".join(items)}'
        elif type(object) is tuple:
            items: list[str] = [
                formatter(item)
                for item in object
            ]
            return f'{" - ".join(items)}; '
        else:
            return str(object)

    print(formatter(data))


def main() -> None:
    """The execution point for the program file."""
    input_data: TZERO = get_data()
    optimized_data: T1NF = optimize(input_data)
    show_optimized_data(optimized_data)


if __name__ == '__main__':
    print(__doc__)
    main()
