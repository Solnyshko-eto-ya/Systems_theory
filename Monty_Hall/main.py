import random


class MontyHall:
    def __init__(self):
        self.choices = ['к', 'к', 'а']
        self.iter = 10000

    @staticmethod
    def counter(func):
        # проверяем вариант с неизменным выбором
        def wrapper(self):
            win_count = 0
            for _ in range(self.iter):
                result = func(self)
                if result == 'а':
                    win_count += 1
            # вероятность выиграть - частота выигранных опытов
            print(win_count / self.iter)

        return wrapper

    @counter
    def without_change(self):  # в начале каждой попытки случайно перемешаем массив
        random.shuffle(self.choices)
        return self.choices[random.randrange(len(self.choices))]

    @counter
    def with_change(self):  # в начале каждой попытки случайно перемешаем массив
        random.shuffle(self.choices)
        first_choice = random.randrange(len(self.choices))  # первый выбор
        for i in range(len(self.choices)):  # ведущий открывает дверь с козлом
            if i != first_choice and self.choices[i] == 'к':
                host_choice = i
                break
        for i in range(len(self.choices)):  # делаем второй выбор, меняя первое решение
            if i != first_choice and i != host_choice:
                return self.choices[i]


if __name__ == "__main__":
    counter = MontyHall()
    counter.with_change()
    counter.without_change()
