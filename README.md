# Проект NNP

## Описание
NNP — это приложение для автоматического определения роста человека по фотографии с использованием методов компьютерного зрения и нейронных сетей. Цель проекта — предоставить пользователю инструмент для точной оценки физического параметра (роста) на основе изображения. Это актуально для таких областей, как медицина, спорт и мода, где важны точные данные о параметрах тела.

В основе проекта лежат передовые технологии компьютерного зрения и машинного обучения. Нейросеть обучена на большом наборе данных с людьми, имеющими известные параметры, что позволяет системе точно анализировать и распознавать особенности человеческой фигуры. Калибровка изображений, учитывающая перспективу и расстояние, повышает точность измерений.

## Основные функции
- Определение роста человека по фотографии.
- Использование нейронных сетей для распознавания объектов и вычисления роста.
- Удобный пользовательский интерфейс.
- Для точных результатов необходима фотография с человеком в полный рост, лицом к камере.

## Участники проекта
- **Менеджер проекта**: Владислав Гришин (Email: ya.tipa.v.it@gmail.com)
- **Разработчики**:
  - Илья Крюков (Email: ilya74008@gmail.com)
  - Даниил Кузин (Email: kasvorten98342@mail.ru)
  - Кирилл Репухов (Email: kirill2003210@gmail.com)

## Зоны ответственности
- Работа с заказчиком: В. Гришин
- Пользовательский интерфейс: К. Репухов
- Работа с нейросетями: Д. Кузин
- Организационные вопросы: В. Гришин
- Бухгалтерия: И. Крюков
- Разработка: Все участники команды

## Структура проекта
- **NNP** — директория проекта.
  - `manage.py` — скрипт для управления проектом.
  - `NNP/settings.py` — настройки проекта.
  - `NNP/urls.py` — маршруты URL.
  - `NNP/wsgi.py` — взаимодействие с веб-сервером.
- **about** — приложение с информацией о проекте.
- **user_profile** — приложение для работы с пользователями (регистрация, авторизация, редактирование профиля).
- **image_history** — приложение для хранения и отображения истории изображений.
- **image_analysis** — приложение для анализа изображений и вычисления роста.
- **templates** — шаблоны страниц для каждого приложения.

## Установка и настройка

### 1. Клонирование репозитория
```
git clone https://github.com/DaniilKusin/NNP
cd NNP
```

### 2.Создание виртуального окружения
```
python3 -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate     # Для Windows
```

### 3. Установка зависимостей
```
pip install -r requirements.txt
```
### 4. Настройка конфигурации
Создайте файл .env в корне проекта и добавьте следующие строки:

```

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```
### 5. Применение миграций
```
python manage.py migrate
```
### 6. Создание суперпользователя
```
python manage.py createsuperuser
````
### 7. Запуск сервера
```
python manage.py runserver
```
Теперь проект доступен по адресу: http://127.0.0.1:8000/.




