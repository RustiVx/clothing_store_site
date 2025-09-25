# Архитекутура

## Обзор
Простой сайт для покупки одежды, включает в себя:

-   каталог товаров
-   кнопка "Купить" ведёт на страницу с оформлением заявки
-   оформление заказа, который вносится в БД

## Компоненты
```text
app/
├── app.py            # Основной файл с логикой приложения
├── maindata.db       # База данных
├── readme.md         # Документация проекта
├── static/
│   └── img/          # Папка для изображений
├── templates/
│   ├── base_search_styles_img.html     # Базовый шаблон (для использования в других шаблонах)
│   ├── aboutsus.html                   # Шаблон о нас
│   ├── category.html                   # Шаблон выбора категории
│   ├── category_girlscl.html           # Шаблнон категории для девочек
│   ├── category_boyscl.htmlё           # Шаблон категории для мальчиков
│   ├── index.html                      # Шаблон главной страницы
│   ├── news.html                       # Шаблон новостей
│   ├── personalacc.html                # Шаблон аккаунта пользователя
│   └── shop.html                       # Шаблон оформления товара
```
## Схема базы данных

```sql
-- Таблица аккаунтов клиентов
CREATE TABLE IF NOT EXISTS account (
  id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор аккаунта
  name TEXT NOT NULL,                    -- Имя клиента
  age INTEGER NOT NULL,                  -- Возраст клиента
  phone TEXT NOT NULL UNIQUE             -- Телефон клиента (с уникальностью)
);

-- Таблица товаров (продуктов)
CREATE TABLE IF NOT EXISTS product (
  id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор товара
  name TEXT NOT NULL,                    -- Название товара
  desc TEXT,                             -- Описание товара
  price INTEGER NOT NULL,                -- Цена товара в копейках (в целых числах)
  pict TEXT,                             -- Путь или URL к изображению товара
  quantity INTEGER NOT NULL              -- Количество товара на складе
);

-- Таблица заказов
CREATE TABLE IF NOT EXISTS orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор заказа
  client_id INTEGER REFERENCES account(id),  -- Ссылка на аккаунт клиента
  phone TEXT NOT NULL,                   -- Телефон клиента (для контакта при заказе)
  total_cents INTEGER NOT NULL,          -- Общая сумма заказа в копейках
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Дата и время создания заказа
);
```

## Ошибки и валидация

404 - страница не найдена