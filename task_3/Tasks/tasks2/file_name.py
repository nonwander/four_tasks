#!/usr/bin/env python3
"""This module consits of File Name tasks.
"""
from typing import Any


def get_list() -> list[str]:
    """Loads list of filenames in a certain way.

    Returns:
        list of filenames in string type.
    """
    pass


def vatidate(input_list: list[str]) -> list[str]:
    """Compiles a new list of valid names.
    A filename is considered valid if there are no identical characters
    duplicated in a row in it.

    Returns:
        output_list -- list without unvalid names.
    """
    pass


def get_maxlen_name(input_list: list[str]) -> int:
    """Finds the longest filename from the list
    and counts its length.

    Returns:
        max_len -- the maximal item length in list.
    """
    pass


def change_filenames(input_list: list[str], max_len: int) -> list[str]:
    """Сhanges the filenames to the required length.
    Fills in the missing characters with an underscore.

    Arguments:
        input_list -- list of filenames in string type.
        max_len -- the maximal item length in list.

    Returns:
        output_list -- list of filenames with correct length.
    """
    pass


def main() -> None:
    """The execution point for the program file."""
    input_list: list[str] = get_list()
    validated_list = vatidate(input_list)
    maximal_lenght: int = get_maxlen_name(validated_list)
    corrected_list: list[str] = change_filenames(validated_list, validated_list)


if __name__ == '__main__':
    print(__doc__)
    main()
