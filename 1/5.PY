def calculate_heights(n, relationships):
    from collections import defaultdict

    # Создаем словарь для хранения родителя каждого элемента
    parent = {}
    for child, parent_name in relationships:
        parent[child] = parent_name

    # Функция для вычисления высоты элемента
    def get_height(name, cache):
        if name not in parent:  # Родоначальник
            return 0
        if name in cache:
            return cache[name]
        cache[name] = get_height(parent[name], cache) + 1
        return cache[name]

    # Вычисляем высоты для всех элементов
    cache = {}
    all_elements = set(parent.keys()) | set(parent.values())
    heights = {name: get_height(name, cache) for name in all_elements}

    # Возвращаем элементы в лексикографическом порядке с высотами
    return sorted(heights.items())

# Пример
n = 5
relationships = [
    ("B", "A"),
    ("C", "A"),
    ("D", "B"),
    ("E", "B")
]
for name, height in calculate_heights(n, relationships):
    print(name, height)