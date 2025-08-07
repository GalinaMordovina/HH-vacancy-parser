from abc import ABC, abstractmethod
from typing import List
from src.vacancy import Vacancy  # импортируем класс вакансии

class VacancySaver(ABC):
    """
    Абстрактный класс для работы с хранилищем вакансий.
    """

    @abstractmethod
    def add(self, vacancy: Vacancy) -> None:
        """
        Добавить вакансию в хранилище.
        """
        pass

    @abstractmethod
    def get(self, criteria: dict) -> List[Vacancy]:
        """
        Получить вакансии по заданным критериям.
        """
        pass

    @abstractmethod
    def delete(self, vacancy: Vacancy) -> None:
        """
        Удалить вакансию из хранилища.
        """
        pass
