import time
import random
import matplotlib.pyplot as plt


# --- Заглушки для функций поиска (замените на ваши реальные реализации) ---
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# -------------------------------------------------------------------------


def run_benchmark():
    sizes = [1000, 5000, 10000, 20000, 50000, 100000]
    linear_times = []
    binary_times = []

    # Количество повторений для усреднения (чем меньше N, тем больше нужно повторений)
    # Для N=1000 даже 1000 повторений может быть мало, но это даст стабильный график
    repetitions = 1000

    for n in sizes:
        # 1. Генерируем данные
        data = list(range(n))  # [0, 1, 2, ..., n-1]

        # 2. Готовим данные для линейного поиска (НЕСОРТИРОВАННЫЕ или просто исходные)
        # Важно: не сортируем data перед линейным поиском, чтобы не тратить время на O(N log N)
        linear_data = data[:]
        target_linear = linear_data[-1]  # Худший случай: элемент в конце

        # 3. Готовим данные для бинарного поиска (СОРТИРОВАННЫЕ)
        binary_data = sorted(data)  # Или просто data, так как range уже отсортирован
        target_binary = binary_data[-1]  # Худший случай для бинарного тоже берем с края

        # --- Замер линейного поиска ---
        start = time.perf_counter()
        for _ in range(repetitions):
            linear_search(linear_data, target_linear)
        elapsed_linear = (time.perf_counter() - start) / repetitions
        linear_times.append(elapsed_linear)

        # --- Замер бинарного поиска ---
        start = time.perf_counter()
        for _ in range(repetitions):
            binary_search(binary_data, target_binary)
        elapsed_binary = (time.perf_counter() - start) / repetitions
        binary_times.append(elapsed_binary)

    # --- Построение графика ---
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, "ro-", label="Линейный поиск")
    plt.plot(sizes, binary_times, "g^-", label="Бинарный поиск")

    plt.title("Сравнение времени выполнения поиска")
    plt.xlabel("Размер списка (N)")

    plt.ylabel("Время (сек)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()

    plt.savefig("graph_comparison.png")
    print("График сохранен как 'graph_comparison.png'")
    plt.show()


if __name__ == "__main__":
    run_benchmark()
