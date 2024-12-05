def extract_above_secondary_diagonal(matrix):
    n = len(matrix)
    result = []
    for i in range(n):
        for j in range(n - i - 1):
            result.append(matrix[i][j])
    return result

# Пример
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(extract_above_secondary_diagonal(matrix))