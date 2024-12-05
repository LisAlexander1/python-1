def write_numbers_to_file(filename, numbers):
    """
    Записывает список чисел в файл.
    :param filename: Имя файла для записи.
    :param numbers: Список действительных чисел.
    """
    with open(filename, "w") as file:
        for number in numbers:
            file.write(f"{number}\n")

def calculate_difference(filename):
    """
    Читает числа из файла и возвращает разность между первым и последним числом.
    :param filename: Имя файла для чтения.
    :return: Разность первого и последнего числа.
    """
    with open(filename, "r") as file:
        numbers = [float(line.strip()) for line in file.readlines()]
    if len(numbers) < 2:
        raise ValueError("Файл должен содержать как минимум два числа.")
    return numbers[-1] - numbers[0]
