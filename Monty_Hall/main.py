import random

# к - козел, а - автомобиль
choices = ['к', 'к', 'а']
# число опытов
N = 10000


class choice_without_change:
    def without_change(choices):  # в начале каждой попытки случайно перемешаем массив
        random.shuffle(choices)
        return choices[random.randrange(len(choices))]

    # проверяем вариант с неизменным выбором
    win_count = 0
    for _ in range(N):
        result = without_change(choices)
        if result == 'а':
            win_count += 1
    # вероятность выиграть - частота выигранных опытов
    print(win_count / N)


class choice_with_change:
    def with_change(choices):   # в начале каждой попытки случайно перемешаем массив
        random.shuffle(choices)
        first_choice = random.randrange(len(choices))  # первый выбор
        for i in range(len(choices)):  # ведущий открывает дверь с козлом
            if i != first_choice and choices[i] == 'к':
                host_choice = i
                break
        for i in range(len(choices)):  # делаем второй выбор, меняя первое решение
            if i != first_choice and i != host_choice:
                return choices[i]


    # проверяем вариант с изменением выбора
    win_count = 0
    for _ in range(N):
        result = with_change(choices)
        if result == 'а':
            win_count += 1
    # вероятность выиграть - частота выигранных опытов
    print(win_count/N)
