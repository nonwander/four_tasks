from .file_name import change_filenames, get_list, get_maxlen_name, validate


def test_get_maxlen_name():
    """Determined the longest filename in the list."""
    input_data = [
        'a', 'bb', 'ccc', 'dddd', 'ccc', 'bb', 'a',
    ]
    expected_data = 4
    result = get_maxlen_name(input_data)
    assert result == expected_data


def test_validate():
    """The input filenames in list are returned without duplicated chars."""
    input_data = [
        'one', 'two', 'three', 'four', 'ffff',
    ]
    expected_data = [
        'one', 'two', 'thre', 'four', 'f'
    ]
    result = validate(input_data)
    assert result == expected_data


def test_change_filenames():
    """The input filenames in list are modified to the correct length."""
    MAX_LEN = 10
    input_data = [
        'one', 'f'
    ]
    expected_data = [
        'one_______', 'f_________'
    ]
    result = change_filenames(input_data, MAX_LEN)
    assert result == expected_data


def test_get_list():  # TODO:
    """Start to do this test.
    """
    pass
