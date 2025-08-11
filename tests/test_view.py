from src.view import user_interaction

class DummyAPI:
    @staticmethod
    def load_vacancies(keyword):
        _ = keyword  # Явно игнорируем параметр, чтобы подавить предупреждение
        # Возвращаем фиктивные данные, имитируя API
        return [
            {"name": "Python Developer", "alternate_url": "http://example.com/1", "salary": 100000, "snippet": {"requirement": "Python, Django"}},
            {"name": "Junior Python Developer", "alternate_url": "http://example.com/2", "salary": 50000, "snippet": {"requirement": "Python"}},
        ]

class DummySaver:
    def __init__(self):
        self.saved = []
    def add(self, vacancy):
        self.saved.append(vacancy)

def test_user_interaction(monkeypatch):
    inputs = iter([
        "Python",     # keyword
        "1",          # top_n
        "Django",      # filter words
        "json"        # экспорт формата
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    api = DummyAPI()
    saver = DummySaver()

    user_interaction(api, saver)

    # Проверяем, что из всех сохраненных вакансий, для показа будет одна, прошедшая фильтр
    filtered = [v for v in saver.saved if "django" in v.description.lower()]
    assert len(filtered) == 1  # только первая вакансия должна соответствовать фильтру


def test_user_interaction_empty_keyword(monkeypatch, capsys):
    inputs = iter([
        "",  # пустой keyword
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    api = DummyAPI()
    saver = DummySaver()

    user_interaction(api, saver)

    captured = capsys.readouterr()
    assert "Ключевое слово не может быть пустым." in captured.out


def test_user_interaction_invalid_top_n(monkeypatch):
    inputs = iter([
        "Python",       # keyword
        "abc",          # invalid top_n, не число
        "",             # пустой фильтр (без фильтрации)
        "нет"           # пропуск экспорта
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    api = DummyAPI()
    saver = DummySaver()

    user_interaction(api, saver)

    # Проверяем, что все вакансии были сохранены
    assert len(saver.saved) == 2


def test_user_interaction_no_filter_words(monkeypatch):
    inputs = iter([
        "Python",       # keyword
        "2",            # top_n
        "",             # пустой фильтр
        "нет"           # пропуск экспорта
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    api = DummyAPI()
    saver = DummySaver()

    user_interaction(api, saver)

    # Должны сохранить 2 вакансии без фильтрации
    assert len(saver.saved) == 2
