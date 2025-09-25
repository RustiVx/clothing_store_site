# Установка и запуск (Flask + sqlite3)

## Предпосылки

-   Python 3.10+
-   Windows

## Локальный запуск
```bash
pip install flask
pip install sqlite3
```

##  Структура проекта
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
## app.py

```
from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

connection = sqlite3.connect('maindata.db', check_same_thread=False)
cursor = connection.cursor()

def product_catg(): # Импорт из БД ВСЕХ продуктов для категорий
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

def productindex(): # Импорт из БД только 12 продуктов для главной страницы 
    listDB = cursor.execute('SELECT * FROM product LIMIT 12')
    return listDB.fetchall()

def accounts(): # Импорт всех аккаунтов из БД
    cursor.execute('SELECT * FROM account')
    return cursor.fetchall()

@app.route('/') # Главная страница сайта
def index():
    shop = productindex()
    connection.close
    return render_template('index.html', shop = shop)

@app.route('/news') # Страница с новостями сайта
def news_and_blog():
    return render_template('news.html')

@app.route('/category') # Страница с выбором двух существующих категорий
def category():
    return render_template('category.html')

@app.route('/aboutus') # Страница о нас
def about_us():
    return render_template('aboutus.html')
    
@app.route('/personalacc', methods=['GET', 'POST']) # Страница с воддом имени для проверки его регистрации
def personal_account():
    user = None
    error = None
    
    if request.method == 'POST':
        name = request.form['user']
        
        all_users = accounts()
        
        user = next((u for u in all_users if u[1].lower() == name.lower()), None)
        
        if not user:
            error = 'Пользователь не найден'
    
    return render_template('personalacc.html', user=user, error=error)

@app.route('/category/girlscl') # Категория с одеждой для девочек
def girls_clothing():
    shop = product_catg()
    return render_template('category_girlscl.html', shop = shop)

@app.route('/category/boyscl') # Категория с одеждой для мальчиков
def boys_clothing():
    shop = product_catg()
    return render_template('category_boysscl.html', shop = shop)

@app.route('/shop', methods=['GET', 'POST']) # Страница оформления товара
def shop():
    product_id = request.args.get('id', type=int)
    if not product_id:
        return "Не указан ID товара", 400

    product = cursor.execute('SELECT * FROM product WHERE id = ?', (product_id,)).fetchone()
    if not product:
        return "Товар не найден", 404

    message = ''

    if request.method == 'POST':
        client = request.form.get('name')
        phone = request.form.get('phone')
        comment = request.form.get('comment')

        if not client or not phone:
            message = 'Пожалуйста, заполните имя и телефон.'
        else:
            cursor.execute(
                'INSERT INTO orders (client, phone, product_id, comment) VALUES (?, ?, ?, ?)',
                (client, phone, product_id, comment)
            )
            connection.commit()
            message = 'Спасибо! Ваш заказ успешно оформлен.'

    return render_template('shop.html', product=product, message=message)

if __name__ == "__main__": # Запуск Flask, сайта
    print('Flask исправно работает')
    app.run(debug=True)
```

## Переменные окружения

-   app - создание фабрики сайта
-   connection - подключение к базе данных
-   cursor - обработка значений из юазы данных 
-   category_map - обработка товаров по категориям
-   db_category - категория в базе данных 
-   columns - колонки
-   shop - база данных
-   category - категория
-   products - товары
-   methods - метод для заявки
-   product_id - id клиента
-   name - имя клиента
-   phone - телефон клиента