from src.hh import HH

if __name__ == "__main__":
    hh_api = HH(None)  # file_worker еще не реализован - передаем None

    # Проверка подключения
    if hh_api.connect():
        print("Подключение к HH API успешно")
    else:
        print("Ошибка подключения к HH API")

    # Получение вакансий
    vacancies = hh_api.load_vacancies("Python")
    print(f"Получено вакансий: {len(vacancies)}")
    if vacancies:
        print("Первая вакансия:")
        print(vacancies[0])
