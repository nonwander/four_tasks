from .service_center import get_data, optimize, show_optimized_data


def test_optimize():
    """The input data is reduced to the first normal form."""
    input_data = [
        ('Ноутбук', 1500, 'Татьяна', '89001001010'),
        ('Смартфон', 500, 'Анна', '89002002020'),
        ('Проектор', 2500, 'Андрей', '89003003030'),
        ('Принтер', 1000, 'Татьяна', '89001001010'),
        ('Планшет', 700, 'Татьяна', '89001001010'),
        ('Смартфон', 1000, 'Андрей', '89003003030'),

    ]
    expected_data = [
        {'Татьяна 89001001010': [('Ноутбук', 1500), ('Принтер', 1000), ('Планшет', 700)]},
        {'Анна 89002002020': [('Смартфон', 500)]},
        {'Андрей 89003003030': [('Проектор', 2500), ('Смартфон', 1000)]},
    ]
    result = optimize(input_data)
    assert result == expected_data


def test_show_optimized_data(capsys):
    """Printing in console data objects in one line."""
    input_data = [
        {'Татьяна 89001001010': [('Ноутбук', 1500), ('Принтер', 1000), ('Планшет', 700)]},
        {'Анна 89002002020': [('Смартфон', 500)]},
        {'Андрей 89003003030': [('Проектор', 1500), ('Смартфон', 1000)]},
    ]
    print(
        'Татьяна 89001001010: Ноутбук - 1500; Принтер - 1000; Планшет - 700\n'
        'Анна 89002002020: Смартфон - 500\n'
        'Андрей 89003003030: Проектор - 1500; Смартфон - 1000\n'
    )
    expected_data = capsys.readouterr()
    show_optimized_data(input_data)
    result = capsys.readouterr()
    assert result.out == expected_data.out


def test_get_data():  # TODO:
    """Start to do this test.
    """
    pass
