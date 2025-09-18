from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Главная страница'

@app.route('/news')
def news_and_blog():
    return 'Новости/Блоги'

@app.route('/category')
def category():
    return 'Категории'

@app.route('/aboutus')
def about_us():
    return 'О нас'

@app.route('/personalacc')
def personal_account():
    return 'Аккаунт'

@app.route('/category/girlscl')
def girls_clothing():
    return 'Одежда для девочек'

@app.route('/category/boyscl')
def boys_clothing():
    return 'Одежда для мальчиков'

@app.route('/category/girls.shoes')
def  girls_shoes():
    return 'Обувь для девочек'

@app.route('/category/boys.shoes')
def boys_shoes():
    return 'Обувь для мальчиков'

if __name__ == "__main__":
    print('Flask исправно работает')
    app.run(debug=True)