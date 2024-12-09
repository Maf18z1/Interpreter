# 1. Клонирование репозитория
Склонируйте репозиторий с исходным кодом и тестами:
```
git clone <URL репозитория>
cd <директория проекта>
```

# 2. Запуск окружения
#Активируйте виртуальное окружение
```
python -m venv venv
#Для Windows:
venv\Scripts\activate
#Для MacOS/Linux:
source venv/bin/activate
pip install pytest

python __main__.py
```

# 3. Структура проекта
```
Confmg4.py           # Файл с реализацией ассемблера и интерпретатора
Test.py      # Файл с тестами для команд
Test.txt # Файл с тестовой программой
```

# 4. Запуск тестов
Мы будем использовать модуль Python pytest для тестирования.
```
pytest Test.py
```
