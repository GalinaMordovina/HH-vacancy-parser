import pytest
from src.vacancy_saver import VacancySaver, JSONSaver
from src.vacancy import Vacancy


def test_cannot_instantiate_abstract_class():
    with pytest.raises(TypeError):
        VacancySaver()  # Попытка создать экземпляр абстрактного класса должна вызвать TypeError


def test_abstract_methods_signature():
    # Проверяем, что у VacancySaver есть требуемые абстрактные методы
    methods = ['add', 'get', 'delete']
    for method in methods:
        assert callable(getattr(VacancySaver, method))


@pytest.fixture
def temp_filename(tmp_path):
    return tmp_path / "vacancies.json"


def test_add_and_get_vacancy(temp_filename):
    saver = JSONSaver(str(temp_filename))
    vacancy = Vacancy("Python Dev", "https://hh.ru/vacancy/1", 100000, "Desc")
    saver.add(vacancy)

    results = saver.get({"title": "Python Dev"})
    assert len(results) == 1
    assert results[0].title == "Python Dev"
    assert results[0].url == "https://hh.ru/vacancy/1"


def test_add_duplicates(temp_filename):
    saver = JSONSaver(str(temp_filename))
    vacancy = Vacancy("Python Dev", "https://hh.ru/vacancy/1", 100000, "Desc")
    saver.add(vacancy)
    saver.add(vacancy)  # попытка добавить дубликат

    results = saver.get({})
    assert len(results) == 1


def test_delete_vacancy(temp_filename):
    saver = JSONSaver(str(temp_filename))
    vacancy1 = Vacancy("Python Dev", "https://hh.ru/vacancy/1", 100000, "Desc")
    vacancy2 = Vacancy("Java Dev", "https://hh.ru/vacancy/2", 120000, "Desc")
    saver.add(vacancy1)
    saver.add(vacancy2)

    saver.delete(vacancy1)
    results = saver.get({})
    assert len(results) == 1
    assert results[0].title == "Java Dev"
