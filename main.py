# пример начального main.py
print("Student Branching App")
print("Проект для тренировки веток Git")

from profile import print_profile

print("Student Branching App")
print_profile()

SUBJECTS = [
    "Основы программирования",
    "Git и системы контроля версий",
    "Базы данных",
    "Веб-разработка"
]


def print_subjects():
    print("\nДисциплины:")
    for number, subject in enumerate(SUBJECTS, start=1):
        print(f"{number}. {subject}")
