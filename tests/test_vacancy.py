from src.vacancy import Vacancy  # поправь путь, если по-другому

def test_validate_salary():
    # Проверка на разные варианты зарплаты
    assert Vacancy._validate_salary(None) == 0
    assert Vacancy._validate_salary('') == 0
    assert Vacancy._validate_salary('зарплата не указана') == 0
    assert Vacancy._validate_salary('100000') == 100000
    assert Vacancy._validate_salary(50000) == 50000
    assert Vacancy._validate_salary('invalid') == 0

def test_vacancy_comparison():
    v1 = Vacancy("Job1", "url1", 50000, "desc1")
    v2 = Vacancy("Job2", "url2", 70000, "desc2")
    v3 = Vacancy("Job1", "url3", 50000, "desc3")

    assert v1 < v2
    assert not v2 < v1
    assert v1 == v3
    assert v1 != v2

def test_repr():
    v = Vacancy("Job1", "url1", 100000, "desc")
    repr_str = repr(v)
    assert "Job1" in repr_str
    assert "url1" in repr_str
    assert "100000" in repr_str
    assert "desc" in repr_str
