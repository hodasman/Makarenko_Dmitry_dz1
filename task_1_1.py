time = int (input('Введите секунды: '))
if 0 <= time < 60:
    print(time, 'сек')
elif 60 <= time < 3600:
    print(time // 60, 'мин', time - time // 60 * 60,'сек')
elif 3600 <= time < 86400:
    print(time // 3600, 'ч', (time % 3600) // 60, 'мин', time % 60, 'сек')
elif time >= 86400:
    print(time // 86400, 'дн', (time % 86400) // 3600, 'ч', (time % 3600) // 60, 'мин', time % 60, 'сек')
else: print('Не верное значение!')
