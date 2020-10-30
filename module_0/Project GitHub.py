import numpy as np


def game_core_v3(number):
    """Берем за первый вариант ответ 50, затем сокращаем диапазон, содержащий верный ответ,
    путем смещения крайних возможных вариантов и берем среднее целое между ними.
    Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = 50
    low_point = 1  # минимальный возможный вариант ответа
    high_point = 100  # максимальный возможный вариант ответа
    while number != predict:
        count += 1
        if number > predict:
            low_point = predict + 1
            predict = (low_point + high_point)//2
        elif number < predict:
            high_point = predict - 1
            predict = (low_point + high_point)//2
    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)
