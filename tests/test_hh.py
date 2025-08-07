import sys
from src.hh import HH
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))


def test_connect():
    hh = HH(None)  # передаем None или заглушку, если file_worker не нужен
    assert hh.connect() is True or hh.connect() is False  # проверяем, что метод не падает

def test_load_vacancies():
    hh = HH(None)
    vacancies = hh.load_vacancies("Python")
    assert isinstance(vacancies, list)
    if vacancies:  # если список не пустой
        assert "name" in vacancies[0] or "id" in vacancies[0]  # пример проверки ключей в словаре вакансии
