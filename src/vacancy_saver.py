import json
from pathlib import Path
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from src.vacancy import Vacancy


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


class JSONSaver(VacancySaver):
    def __init__(self, filename: str = "vacancies.json"):
        self._filename = Path(filename)

    def _load_file(self) -> List[Dict[str, Any]]:
        """
        Метод для загрузки данных из JSON файла.
        """
        if not self._filename.exists():
            # Файл отсутствует возвращаем пустой список
            return []

        with open(self._filename, "r", encoding="utf-8") as f:
            try:
                # Загружаем JSON в список словарей
                data = json.load(f)
                # Проверяем, что данные - это список, иначе возвращаем пустой список
                if not isinstance(data, list):
                    return []
                return data
            except json.JSONDecodeError:
                # При ошибке чтения JSON возвращаем пустой список
                return []

    def _save_file(self, data: List[Dict[str, Any]]) -> None:
        """
        Метод для сохранения списка вакансий в JSON файл.
        """
        with open(self._filename, "w", encoding="utf-8") as f:
            # Записываем данные с отступами для удобства чтения
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в файл, если её там еще нет (по уникальному url).
        """
        data = self._load_file()

        # Проверяем наличие вакансии с таким url
        if not any(v["url"] == vacancy.url for v in data):
            # Добавляем новую вакансию как словарь
            data.append({
                "title": vacancy.title,
                "url": vacancy.url,
                "salary": vacancy.salary,
                "description": vacancy.description
            })
            # Сохраняем обновленный список в файл
            self._save_file(data)

    def get(self, criteria: Dict[str, Any]) -> List[Vacancy]:
        """
        Получение списка вакансий, соответствующих заданным критериям.
        """
        data = self._load_file()
        results = []

        for v in data:
            # Проверяем, что все критерии совпадают с данными вакансии
            if all(v.get(k) == val for k, val in criteria.items()):
                # Создаем объект Vacancy из данных словаря
                results.append(Vacancy(v["title"], v["url"], v["salary"], v["description"]))

        return results

    def delete(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии из файла по её уникальному url.
        """
        data = self._load_file()
        # Отфильтровываем список, исключая вакансию с заданным url
        data = [v for v in data if v["url"] != vacancy.url]
        self._save_file(data)
