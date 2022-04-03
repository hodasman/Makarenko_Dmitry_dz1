# list = []
# list_sum = []
# for number in range(1, 1000, 2):
#     number = number**3
#     list.append (number)
# for number in list:
#      sum = 0
#      number1 = number
#      while number1 > 0:
#          digit = number1 % 10
#          sum = sum + digit
#          number1 = number1 // 10
#      if sum % 7 == 0:
#          list_sum.append(number)
# a = 0
# for x in list_sum:
#     a += x
# print(a) # Первый ответ
#
# list_b = []
# list_sum_b = []
# for number in list:
#     number_b = number + 17
#     list_b.append(number_b)
# for number in list_b:
#      sum = 0
#      number1 = number
#      while number1 > 0:
#          digit = number1 % 10
#          sum = sum + digit
#          number1 = number1 // 10
#      if sum % 7 == 0:
#          list_sum_b.append(number)
# b = 0
# for x in list_sum_b:
#     b += x
# print(b) # Второй ответ


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    dataset = []
    list_sum = []
    for number in range(1, 1000, 2):
        number = number ** 3
        dataset.append(number)
    for number in dataset:
        sum = 0
        number1 = number
        while number1 > 0:
            digit = number1 % 10
            sum = sum + digit
            number1 = number1 // 10
        if sum % 7 == 0:
            list_sum.append(number)
    a = 0
    for x in list_sum:
        a += x
    return a


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    dataset = []
    list_sum_b = []
    for number in range(1, 1000, 2):
        number = number ** 3 + 17
        dataset.append(number)
    for number in dataset:
        sum = 0
        number1 = number
        while number1 > 0:
            digit = number1 % 10
            sum = sum + digit
            number1 = number1 // 10
        if sum % 7 == 0:
            list_sum_b.append(number)
    b = 0
    for y in list_sum_b:
        b += y
    return b  # Верните значение полученной суммы


my_list = []  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)