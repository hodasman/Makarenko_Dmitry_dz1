# Сразу делал без исходного кода. В методичке его нет
# time = int (input('Введите секунды: '))
# if 0 <= time < 60:
#     print(time, 'сек')
# elif 60 <= time < 3600:
#     print(time // 60, 'мин', time - time // 60 * 60,'сек')
# elif 3600 <= time < 86400:
#     print(time // 3600, 'ч', (time % 3600) // 60, 'мин', time % 60, 'сек')
# elif time >= 86400:
#     print(time // 86400, 'дн', (time % 86400) // 3600, 'ч', (time % 3600) // 60, 'мин', time % 60, 'сек')
# else: print('Не верное значение!')

def convert_time(duration: int) -> str:
    if 0 <= duration < 60:
        text = duration, 'сек'
    elif 60 <= duration < 3600:
        text = f'{duration // 60} мин {duration - duration // 60 * 60} сек'
    elif 3600 <= duration < 86400:
        text = f'{duration // 3600} ч {duration % 3600 // 60} мин {duration % 60} сек'
    elif duration >= 86400:
        text = f'{duration // 86400} дн {duration % 86400 // 3600} ч {duration % 3600 // 60} мин {duration % 60} сек'
    else: text = f'Неверное значение'
    return text


duration = 400153
result = convert_time(duration)
print(result)