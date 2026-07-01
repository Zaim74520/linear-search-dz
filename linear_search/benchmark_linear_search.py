import time
import matplotlib.pyplot as plt


def linear_search(arr, target):
    """Линейный поиск: возвращает индекс элемента или -1, если не найден."""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


# Размеры списков для тестирования
sizes = [10, 100, 1000]
times = []

for n in sizes:
    # Создаем список из n элементов: [0, 1, 2, ..., n-1]
    arr = list(range(n))
    # Ищем элемент, которого нет в списке (худший случай — полный проход)
    target = -1

    # Замеряем время (используем perf_counter для высокой точности)
    start = time.perf_counter()
    linear_search(arr, target)
    end = time.perf_counter()

    elapsed = end - start
    times.append(elapsed)
    print(f"Размер списка: {n}, время выполнения: {elapsed:.8f} сек.")

# Построение графика
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker="o", linestyle="-")
plt.title("Зависимость времени выполнения линейного поиска от размера списка")
plt.xlabel("Размер списка (n)")
plt.ylabel("Время выполнения (сек)")
plt.grid(True)
plt.xticks(sizes)  # Чтобы на оси X были именно 10, 100, 1000
plt.show()
