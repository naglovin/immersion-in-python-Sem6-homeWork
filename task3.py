# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки. *Выведите все успешные варианты расстановок

from random import randint

# N = 8
# x = []
# y = []
# for i in range(N):
#     new_x, new_y = [int(s) for s in input("Вводите по две цифры, через пробел: ").split()]
#     x.append(new_x), y.append(new_y)
#
# game = True
# for i in range(N):
#     for j in range(i + 1, N):
#         if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#             game = False
#
# if game:
#     print('False')
# else:
#     print('True')


x = []
y = []
def add_digit(n):
    count = 0
    while count < n:
        a = randint(1, 8)
        b = randint(1, 8)
        x.append(a), y.append(b)
        count += 1
    game = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                game = False

    if game:
        print('False')
    else:
        print('True')

print(add_digit(8))
    # random_integer_array = numpy.random.random_integers(1, 10, size=(3, 2))
    # print("2-мерный массив случайных целых чисел \n", random_integer_array)