#!/usr/bin/env python3
"""This module consits of Service Center tasks.
"""
from typing import NewType
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
    def_dict: T1NF = [
        {key: val} for key, val in zip(keys, values)
    ]
    pre_data = defaultdict(list)
    for obj in def_dict:
        for key, val in obj.items():
            pre_data[key].append(val)
    optimized_data = list({key: pre_data[key]} for key in pre_data)
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
    line = ''
    for obj in data:
        for key, value in obj.items():
            subline = ''
            for item in value:
                subline += f'{item[0]} - {item[1]}; '
            line += f'{key}: {subline[:-2]}\n'
    print(line)


def main() -> None:
    """The execution point for the program file."""
    input_data: TZERO = get_data()
    optimized_data: T1NF = optimize(input_data)
    show_optimized_data(optimized_data)


if __name__ == '__main__':
    print(__doc__)
    main()
