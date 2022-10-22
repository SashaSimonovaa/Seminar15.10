import random


def Parametrs():
    print('> Параметры:', f'Здоровье (З) = {health}', f'Длина норы (Д) = {den_size}', f'Уважение (У) = {respect}',
          f'Вес (В) = {weight}', sep='\n', end='\n\n')

def Night(den_size, health, respect, weight):
    return den_size - 2, health + 20, respect - 2, weight - 5

def Dig(x):
    if x == '1':
        print(' ', '> Длина норы увеличилась на 5, здоровье понизилось на 30', sep='\n')
        return den_size + 5, health - 30
    else:
        print(' ', '> Длина норы увеличилась на 2, здоровье понизилось на 10', sep='\n')
        return den_size + 2, health - 10

def Eat(x):
    if x == '1':
        print(' ', '> Здоровье повысилось на 10, вес повысился на 15', sep='\n')
        return health + 10, weight + 15
    elif x == '2' and respect >= 30:
        print(' ', '> Здоровье повысилось на 30, вес повысился на 30', sep='\n')
        return health + 30, weight + 30
    elif x == '2' and respect < 30:
        print(' ', '> Вас не пустили на луг. Здоровье понизилось на 30', sep='\n')
        return health - 30, weight

def Fight(x):
    if x == '1':
        f = random.randint(1, weight + 31)
        if f <= weight:
            print(' ', '> Вы победили', 'Уважение повысилось на 10, здоровье понизилось на 10', sep='\n')
            return health - 10, respect + 10
        else:
            print(' ', '> Противник победил', 'Здоровье понизилось на 10', sep='\n')
            return health - 10, respect
    elif x == '2':
        f = random.randint(1, weight + 51)
        if f <= weight:
            print(' ', '> Вы победили', 'Уважение повысилось на 20, здоровье понизилось на 20', sep='\n')
            return health - 20, respect + 20
        else:
            print(' ', '> Противник победил', 'Здоровье понизилось на 20', sep='\n')
            return health - 20, respect
    elif x == '3':
        f = random.randint(1, weight + 71)
        if f <= weight:
            print(' ', '> Вы победили', 'Уважение повысилось на 40, здоровье понизилось на 40', sep='\n')
            return health - 40, respect + 40
        else:
            print(' ', '> Противник победил', 'Здоровье понизилось на 40', sep='\n')
            return health - 40, respect


den_size = 10
health = 100
respect = 20
weight = 30

while respect < 100 and (den_size > 0 and health > 0 and respect > 0 and weight > 0):
    Parametrs()

    # День
    print('>>>>> ДЕНЬ', '', '> Для выбора действия введите соответствующую цифру', ' 1. Копать нору',
          ' 2. Поесть травки', ' 3. Подраться', ' 4. Поспать', sep='\n')
    choice = input()

    while choice != '1' and choice != '2' and choice != '3' and choice != '4':
        choice = input('Команда не распознана. Введите цифру ещё раз:')

    if choice == '1':
        print(' ', 'Чтобы копать интенсивно (Д+5, З-30), введите 1', 'Чтобы копать лениво (Д+2, З-10), введите 2',
              sep='\n')
        x = input()
        den_size, health = Dig(x)

    if choice == '2':
        print(' ', 'Чтобы поесть жухлой травки (З+10, В+15), введите 1',
              'Чтобы поесть зеленой травки (если У < 30, то З-30; иначе З+30, В+30), введите 2', sep='\n')
        x = input()
        health, weight = Eat(x)

    if choice == '3':
        print(' ', 'Выберите противника:', f'1.Слабый (шанс победы {weight}/{weight + 30}, 3-10, при победе У+10)',
              f'2.Средний (шанс победы {weight}/{weight + 50}, 3-20, при победе У+20)',
              f'3.Сильный (шанс победы {weight}/{weight + 70}, 3-40, при победе У+40)', sep='\n')
        x = input()
        health, respect = Fight(x)

    if choice == '4':
        Night(den_size, health, respect, weight)

    # Ночь
    print(' ', '>>>>> НОЧЬ', ' ', sep='\n')
    den_size, health, respect, weight = Night(den_size, health, respect, weight)
    #:)

Parametrs()
if respect > 100:
    print('Победа :)')
else:
    print('Поражение :(')
