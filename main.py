from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    calculate_salary()
    get_employees()


# ver 2.0
# from application import salary
# from application.db import people


# if __name__ == '__main__':
#     salary.calculate_salary()
#     people.get_employees()
