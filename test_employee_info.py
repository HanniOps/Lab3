import employee_info


def test_get_employees_by_age_range():
    test = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]

    result = employee_info.get_employees_by_age_range(22, 31)

    assert (result == test)


def test_calculate_average_salary():
    test = 60166.666666666664

    result = employee_info.calculate_average_salary()

    assert (result == test)


def test_get_employees_by_dept():
    test = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]

    result = employee_info.get_employees_by_dept('Sales')

    assert (result == test)
