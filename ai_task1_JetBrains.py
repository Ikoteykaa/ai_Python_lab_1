"""ai_task1_JetBrains.py

Скрипт для обчислення площі прямокутника за введеними сторонами.
"""


def calculate_rectangle_area(a: float, b: float) -> float:
    """Обчислює площу прямокутника за формулою a * b."""
    return a * b


def main() -> None:
    # Запит значень сторін у користувача з явним приведенням до float
    a = float(input("Введіть довжину сторони a: "))
    b = float(input("Введіть довжину сторони b: "))

    # Обчислення площі
    area = calculate_rectangle_area(a, b)

    # Виведення розрахованого значення на екран з поясненням
    print(f"Площа прямокутника зі сторонами a = {a} та b = {b} дорівнює: {area}")


if __name__ == "__main__":
    main()
