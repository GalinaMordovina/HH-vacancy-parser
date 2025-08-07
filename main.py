from src.vacancy import Vacancy
# from src.hh import HH

if __name__ == "__main__":
    # hh_api = HH(None)  # file_worker еще не реализован - передаем None
    #
    # # Проверка подключения
    # if hh_api.connect():
    #     print("Подключение к HH API успешно")
    # else:
    #     print("Ошибка подключения к HH API")
    #
    # # Получение вакансий
    # vacancies = hh_api.load_vacancies("Python")
    # print(f"Получено вакансий: {len(vacancies)}")
    # if vacancies:
    #     print("Первая вакансия:")
    #     print(vacancies[0])

        # Создаем пример вакансий
        vac1 = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", 120000, "Разработка веб-приложений")
        vac2 = Vacancy("Java Developer", "https://hh.ru/vacancy/654321", None, "Разработка на Java")

        # Выводим их
        print(vac1)
        print(vac2)

        # Проверка сравнения
        print(f"vac1 < vac2: {vac1 < vac2}")
        print(f"vac1 == vac2: {vac1 == vac2}")
