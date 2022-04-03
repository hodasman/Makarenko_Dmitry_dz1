for number in range(1, 101):
    if 5 <= number <= 20:
        print (number, 'процентов')
    elif number % 10 == 1:
        print(number, 'процент')
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        print(number, 'процента')
    else: print (number, 'процентов')
