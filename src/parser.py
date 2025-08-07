from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный класс для работы с API сервисов вакансий.
    (все что с API наследуем от него)
    """

    def __init__(self, file_worker=None):
        # Можно сохранить file_worker, если потребуется
        self.file_worker = file_worker

    @abstractmethod
    def connect(self):
        """
        Метод для подключения к API сервиса.
        (для дочерних классов)
        """
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        """
        Метод для получения вакансий по ключевому слову.
        (для дочерних классов:
        :param keyword: Ключевое слово для поиска вакансий
        :return: Список словарей с вакансиями)
        """
        pass
