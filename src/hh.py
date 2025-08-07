import requests
from src.parser import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__()  # без аргументов

    def connect(self):
        try:
            response = requests.get(self.url, headers=self.headers, params={'text': '', 'per_page': 1})
            return response.status_code == 200
        except requests.RequestException:
            return False

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        self.vacancies = []  # Очистить список вакансий перед загрузкой
        self.params['page'] = 0
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies  # добавить return!
