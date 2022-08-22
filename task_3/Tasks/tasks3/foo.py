#!/usr/bin/env python3
"""This module calls main functions from Service Center and File Name tasks.
"""
from ..tasks1.service_center import show_optimized_data
from ..tasks2.file_name import change_filenames


def bar(input_data, validated_list, maximal_lenght):
    corrected_list: list[str] = change_filenames(
        validated_list, maximal_lenght
    )
    optimized_data = show_optimized_data(input_data)


def main() -> None:
    """The execution point for the program file."""


if __name__ == '__main__':
    print(__doc__)
    main()
