class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)


# --- Задание 03: Функция хеширования ---
def simple_hash(s: str) -> int:
    """Возвращает хеш-значение строки как сумму ASCII-кодов всех её символов."""
    return sum(ord(c) for c in s)


# --- Задание 04: Словарь на основе хеш-функции ---
class StringHashDict:
    def __init__(self):  # ИСПРАВЛЕНО: было _init_, стало __init__
        self.data = {}

    def add(self, key: str) -> None:
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть строкой")
        self.data[key] = simple_hash(key)

    def get_hash(self, key: str):
        return self.data.get(key)


# --- Блок тестирования (запускает всё сразу) ---
if __name__ == "__main__":
    print("=== Тесты для HashTable (задания 01, 02) ===")
    ht = HashTable(size=5)
    for i in range(10):
        ht.insert(f"key{i}", i)

    ht.resize()
    print(f"Размер таблицы после resize: {ht.size}")

    all_found = True
    for i in range(10):
        if ht.search(f"key{i}") != i:
            all_found = False

    if all_found:
        print("✅ Тест HashTable пройден.")
    else:
        print("❌ Тест HashTable не пройден.")

    print("\n=== Тесты для simple_hash (задание 03) ===")
    test_strings = ["a", "ab", "abc", "hello"]
    for s in test_strings:
        print(f"Строка: '{s}' -> Хеш: {simple_hash(s)}")

    print("\n=== Тесты для StringHashDict (задание 04) ===")
    d = StringHashDict()
    d.add("apple")
    d.add("banana")
    d.add("cherry")

    print(f"Хеш для 'apple': {d.get_hash('apple')}")
    print(f"Хеш для 'banana': {d.get_hash('banana')}")
    print(f"Хеш для 'cherry': {d.get_hash('cherry')}")
    print(f"Хеш для несуществующего ключа: {d.get_hash('missing')}")

    assert d.get_hash("apple") == simple_hash("apple"), "Ошибка: хеш не совпадает!"
    assert d.get_hash("banana") == simple_hash("banana"), "Ошибка: хеш не совпадает!"
    print("✅ Все тесты пройдены!")
