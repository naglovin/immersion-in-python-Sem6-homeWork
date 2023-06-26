"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""


from sys import argv

# def _find_visikos(year):
#     ULIAN = 4
#     GRIG_1 = 400
#     GRIG_2 = 100
#     return year % GRIG_1 == 0 or year % GRIG_2 != 0 and year % ULIAN == 0
#     """Тоже самое только в одну строку"""
#     # if year % 4 != 0:
#     #     return False
#     # elif year % 100 != 0:
#     #     return True
#     # elif year % 400 != 0:
#     #     return False
#     # else:
#     #     return True
#
# def input_data(data):
#     m_30 = [4, 6, 9, 11]
#     m_31 = [1, 3, 5, 7, 8, 10, 12]
#     day, month, year = map(int, data.split('.'))
#     if 1 <= year <= 9999:
#         if 1 <= month <= 12:
#             if month == 2:
#                 if _find_visikos(year):
#                     if 1 <= day <= 29:
#                         return True
#                 else:
#                     if 1 <= day <= 28:
#                         return True
#             if month in m_30 and 1 <= day <= 30:
#                 return True
#             if month in m_31 and 1 <= day <= 31:
#                 return True
#     return False
#
# print(input_data('30.13.2023'))
#
# if __name__ == '__main__':
#     _, *data = argv
#     print(input_data(*data))


def check_date(date: list) -> bool:
    def find_sep(str_date: str) -> str:
        for char in str_date:
            if not char.isdigit():
                return char

    if len(date) == 1:
        day, month, year = tuple(map(int, date[0].split(find_sep(date[0]))))
    else:
        day, month, year = tuple(map(int, date))
    if 0 < month < 13 and 0 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not 0 < day < 32:
                return False
        elif month in [4, 6, 9, 11]:
            if not 0 < day < 31:
                return False
        else:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                if not 0 < day < 30:
                    return False
            else:
                if not 0 < day < 29:
                    return False
    else:
        return False
    return True


if __name__ == '__main__':
    _, *data = argv
    print('Верная дата' if check_date(data) else 'Такой даты не может быть')