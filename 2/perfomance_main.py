from performance import Performance
from play_performance import PlayPerformance

def main():
    # Работа с классом 1-го уровня
    try:
        performance = Performance("Ромео и Джульетта", 100, 150)
        print("Класс 1-го уровня:")
        print(performance)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Работа с классом 2-го уровня
    try:
        play_performance = PlayPerformance("Гамлет", 80, 120, 1601)
        print("\nКласс 2-го уровня:")
        print(play_performance)
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
