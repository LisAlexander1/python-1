from performance import Performance
from datetime import datetime

class PlayPerformance(Performance):
    def __init__(self, title, n1, n2, year_written):
        """
        Конструктор класса PlayPerformance.
        :param title: Название спектакля
        :param n1: Число зрителей в начале
        :param n2: Число зрителей в конце
        :param year_written: Год написания пьесы
        """
        super().__init__(title, n1, n2)
        self.year_written = year_written

    def quality(self):
        """
        Перекрытая функция для вычисления качества спектакля Qp.
        :return: Qp = Q * (T - Р + 1)
        """
        current_year = datetime.now().year
        base_quality = super().quality()
        return base_quality * (current_year - self.year_written + 1)

    def __str__(self):
        """
        Вывод информации об объекте.
        """
        return (f"Спектакль: {self.title}, Зрители: начало={self.n1}, конец={self.n2}, "
                f"Год написания={self.year_written}, Качество (Qp)={self.quality():.2f}")
