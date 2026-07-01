def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


if __name__ == "__main__":
    # Пример данных
    data = [10, 23, 45, 70, 11, 15]
    target = 70

    # Вызов функции
    result = linear_search(data, target)

    # Вывод результата
    if result != -1:
        print(f"Элемент {target} найден на индексе {result}")
    else:
        print(f"Элемент {target} не найден")
