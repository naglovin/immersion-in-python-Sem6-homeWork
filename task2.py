# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# k = 8
# coord_list = []
# answer = None
#
# for _ in range(k):
#     p = [int(s) for s in input().split()]
#
# for elem in coord_list:
#     if (elem[0] == p[0] or elem[1] == p[1]):  # checking for horizontal & vertical crossing
#         answer = "YES"
#         break
#     elif (elem[0] - p[0] == elem[1] - p[1]) or (elem[0] + elem[1] == p[0] + p[1]):  # checking for diagonal crossing
#         answer = "YES"
#         break
#
#     if answer == "YES":
#         break
#     else:
#         answer = "NO"
#         coord_list.append(p)  # appending element after loop for not cheching element itself
#         continue
#
# print(answer)


N = 8
x = []
y = []
for i in range(N):                                   # По длине 8 закидываем две пары цифр через пробел
    new_x, new_y = [int(s) for s in input("Вводите по две цифры, через пробел: ").split()] # заносим данные в наши списки
    x.append(new_x), y.append(new_y)

game = True
for i in range(N):
    for j in range(i + 1, N):
        """Функция Python abs () используется для возврата абсолютного значения числа, 
        т. е. удаляет отрицательный знак числа. """
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            game = False

if game:
    print('False')
else:
    print('True')

