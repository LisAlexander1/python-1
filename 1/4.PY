def diff(set1, set2, set3, symmetric=True):
    if symmetric:
        return set1 ^ set2 ^ set3  # Симметричная разность
    else:
        return set1 - set2 - set3  # Разность

# Пример
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}
print(diff(set1, set2, set3, symmetric=True))  # Симметричная разность
print(diff(set1, set2, set3, symmetric=False))  # Разность