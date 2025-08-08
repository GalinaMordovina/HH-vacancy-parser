from src.vacancy import Vacancy
from src.vacancy_saver import JSONSaver


def main():
    filename = "data/vacancies.json"  # файл для хранения вакансий
    saver = JSONSaver(filename)

    # Создаем несколько вакансий
    vacancy1 = Vacancy("Python Developer", "https://hh.ru/vacancy/1", 100000, "Разработка на Python")
    vacancy2 = Vacancy("Java Developer", "https://hh.ru/vacancy/2", 120000, "Разработка на Java")

    # Добавляем вакансии
    saver.add(vacancy1)
    saver.add(vacancy2)

    print("Все вакансии после добавления:")
    all_vacancies = saver.get({})
    for vac in all_vacancies:
        print(vac)

    # Удаляем одну вакансию
    saver.delete(vacancy1)

    print("\nВсе вакансии после удаления Python Developer:")
    remaining = saver.get({})
    for vac in remaining:
        print(vac)


if __name__ == "__main__":
    main()
