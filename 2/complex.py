import math

class ComplexNumber:
    # Конструктор по умолчанию
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"ComplexNumber created: {self}")

    # Деструктор
    def __del__(self):
        print(f"ComplexNumber destroyed: {self}")

    # Вычисление модуля комплексного числа
    def modulus(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    # Найти обратное комплексное число
    def reciprocal(self):
        modulus_squared = self.real ** 2 + self.imag ** 2
        if modulus_squared == 0:
            raise ValueError("Cannot find reciprocal of zero.")
        return ComplexNumber(self.real / modulus_squared, -self.imag / modulus_squared)

    # Формирование строки информации об объекте
    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return f"{self.real}{sign}{self.imag}i"

# Демонстрация работы
if __name__ == "__main__":
    # Создание объекта через конструктор с параметрами
    c1 = ComplexNumber(3, 4)

    # Вывод информации об объекте
    print("Комплексное число:", c1)

    # Вычисление модуля
    print("Модуль:", c1.modulus())

    # Нахождение обратного числа
    try:
        reciprocal = c1.reciprocal()
        print("Обратное число:", reciprocal)
    except ValueError as e:
        print(e)

    # Создание объекта по умолчанию
    c2 = ComplexNumber()
    print("Комплексное число (по умолчанию):", c2)
