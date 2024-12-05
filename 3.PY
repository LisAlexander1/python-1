def remove_element(arr, k):
    for i in range(k, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()

# Пример
lst = [10, 20, 30, 40, 50]
index_to_remove = 2
remove_element(lst, index_to_remove)
print(lst)