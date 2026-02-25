import pickle
import os


class Student:
    def __init__(self, surname, name, grade, reading_speed=None, math_score=None, final_score=None):
        self.surname = surname
        self.name = name
        self.grade = grade
        self.reading_speed = reading_speed
        self.math_score = math_score
        self.final_score = final_score

    def __str__(self):
        extra_info = ""
        if self.grade == 1:
            extra_info = f"Скор. чтения: {self.reading_speed} сл/мин"
        elif self.grade in [2, 3]:
            extra_info = f"Математика: {self.math_score} балл(ов)"
        elif self.grade == 4:
            extra_info = f"Аттестация: {self.final_score} балл(ов)"
        else:
            extra_info = "Нет данных"
        return f"{self.surname:<15} | {self.name:<15} | {self.grade:^5} | {extra_info:<25}"


def input_student():
    print("\nВвод данных ученика")
    surname = input("Фамилия: ").strip()
    name = input("Имя: ").strip()

    while True:
        try:
            grade = int(input("Класс (1-4): "))
            if 1 <= grade <= 4:
                break
            else:
                print("Ошибка: Класс должен быть от 1 до 4.")
        except ValueError:
            print("Ошибка: Введите число.")

    reading_speed = None
    math_score = None
    final_score = None

    if grade == 1:
        while True:
            try:
                reading_speed = int(input("Скорость чтения (слов в минуту): "))
                if reading_speed >= 0:
                    break
                print("Ошибка: Скорость не может быть отрицательной.")
            except ValueError:
                print("Ошибка: Введите целое число.")

    elif grade in [2, 3]:
        while True:
            try:
                math_score = float(input("Оценка за контрольную по математике (1-10): "))
                if 1 <= math_score <= 10:
                    break
                print("Ошибка: Оценка должна быть от 1 до 10.")
            except ValueError:
                print("Ошибка: Введите число.")

    elif grade == 4:
        while True:
            try:
                final_score = float(input("Балл итоговой аттестации (1-100): "))
                if 1 <= final_score <= 100:
                    break
                print("Ошибка: Балл должен быть от 1 до 100.")
            except ValueError:
                print("Ошибка: Введите число.")

    return Student(surname, name, grade, reading_speed, math_score, final_score)


def save_to_binary(students, filename="students.dat"):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(students, f)
        print(f"\nДанные успешно сохранены в файл '{filename}'.")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


def load_and_print_from_binary(filename="students.dat"):
    if not os.path.exists(filename):
        print(f"\nФайл '{filename}' не найден.")
        return

    try:
        with open(filename, 'rb') as f:
            students = pickle.load(f)

        print("\n" + "=" * 70)
        print(f"{'Фамилия':<15} | {'Имя':<15} | {'Кл':^5} | {'Результат':<25}")
        print("=" * 70)

        for student in students:
            print(student)

        print("=" * 70)
        print(f"Всего учеников: {len(students)}")

    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


def main():
    while True:
        try:
            n = int(input("Введите количество учеников (N): "))
            if n > 0:
                break
            print("Количество должно быть больше 0.")
        except ValueError:
            print("Введите целое число.")

    students_list = []

    for i in range(n):
        print(f"\nУченик #{i + 1}")
        student = input_student()
        students_list.append(student)

    save_to_binary(students_list)

    load_and_print_from_binary()



main()