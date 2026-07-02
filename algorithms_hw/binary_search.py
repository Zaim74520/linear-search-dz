import random


def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"Поиск 7: индекс {binary_search(test_list, 7)}")
    print(f"Поиск 2: индекс {binary_search(test_list, 2)}")
    print(f"Поиск 19: индекс {binary_search(test_list, 19)}")

print("\n--- Пункт 03: Список из 100 случайных чисел ---")

# Создаём 100 случайных чисел от 1 до 1000
data = [random.randint(1, 1000) for _ in range(100)]
# Обязательно сортируем — бинарный поиск работает только на отсортированных данных
data.sort()

print(f"Первые 10 чисел списка: {data[:10]}")
print(f"Всего чисел в списке: {len(data)}")

# Выбираем три разных значения для поиска
# 1. То, что точно есть в списке (берём случайный элемент из самого списка)
target_exists = random.choice(data)
# 2. То, чего точно нет (число больше максимума)
target_missing = 9999
# 3. Случайное число, которое может быть или не быть
target_maybe = random.randint(1, 1000)

# Запускаем бинарный поиск
index_exists = binary_search(data, target_exists)
index_missing = binary_search(data, target_missing)
index_maybe = binary_search(data, target_maybe)

# Выводим результаты
print(f"Поиск {target_exists}: индекс {index_exists}")
print(f"Поиск {target_missing}: индекс {index_missing}")
print(f"Поиск {target_maybe}: индекс {index_maybe}")
