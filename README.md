# Met API tests

Набор автоматизированных тестов для проверки функциональности API Музея Метрополитен.

## Стек технологий

- Python
- typing, datetime, logging
- Pydantic, pytest, pytest-asyncio, httpx

## Структура проекта

```text
met-api-tests/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_departments.py
│   ├── test_object.py
│   ├── test_objects.py
│   └── test_search.py
├── .gitignore
├── LICENSE
├── logger.py
├── pytest.ini
├── README.md
├── requirements.txt
└── schemas.py
```

## Установка и запуск

```bash
git clone <URL_репозитория>

cd <папка_проекта>

python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

pytest
```
