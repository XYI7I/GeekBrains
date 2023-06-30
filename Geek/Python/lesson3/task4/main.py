"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""


def find_items_for_backpack(items, max_weight):
    # Инициализация матрицы для хранения результатов
    dp = [[0] * (max_weight + 1) for _ in range(len(items) + 1)]

    # Заполнение матрицы значениями
    for i in range(1, len(items) + 1):
        item_weight = items[i - 1]["weight"]
        item_value = items[i - 1]["value"]
        for j in range(1, max_weight + 1):
            if item_weight <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_weight] + item_value)
            else:
                dp[i][j] = dp[i - 1][j]

    # Восстановление выбранных предметов
    selected_items = []
    i, j = len(items), max_weight
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1]["weight"]
        i -= 1

    return selected_items


# Пример использования
items = [
    {"name": "Sleeping Bag", "weight": 3, "value": 8},
    {"name": "Tent", "weight": 4, "value": 10},
    {"name": "Water Bottle", "weight": 1, "value": 4},
    {"name": "Food", "weight": 2, "value": 6},
]

max_weight = 6

selected_items = find_items_for_backpack(items, max_weight)

print("Вещи, которые поместятся в рюкзак:")
for item in selected_items:
    print(item["name"])