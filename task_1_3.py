# for number in range(1, 101):
#     if 5 <= number <= 20:
#         print (number, 'процентов')
#     elif number % 10 == 1:
#         print(number, 'процент')
#     elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
#         print(number, 'процента')
#     else: print (number, 'процентов')

def transform_string(number: int) -> str:
    text = 0
    if 5 <= number <= 20:
        text = f'{number} процентов'
    elif number % 10 == 1:
        text = f'{number} процент'
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        text = f'{number} процента'
    else: text = f'{number} процентов'
    return text


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))