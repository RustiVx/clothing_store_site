from flask import Flask
from flask import render_template
import sqlite3


app = Flask(__name__)

connection = sqlite3.connect('maindata.db', check_same_thread=False)
cursor = connection.cursor()

def product():
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

def productindex():
    listDB = cursor.execute('SELECT * FROM product LIMIT 12')
    return listDB.fetchall()

@app.route('/')
def index():
    shop = productindex()
    connection.close
    return render_template('index.html', shop = shop)

@app.route('/news')
def news_and_blog():
    return render_template('news.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

@app.route('/personalacc')
def personal_account():
    return render_template('personalacc.html')

@app.route('/personalacc/<username>')
def personal_account_user(username):
    return render_template('personalacc.html', name=username)

@app.route('/category/girlscl')
def girls_clothing():
    return render_template('category_girlscl.html')

@app.route('/category/boyscl')
def boys_clothing():
    return render_template('category_boysscl.html')

@app.route('/category/girls.shoes')
def  girls_shoes():
    return render_template('category_girls_shoes.html')

@app.route('/category/boys.shoes')
def boys_shoes():
    return render_template('category_boys_shoes.html')

if __name__ == "__main__":
    print('Flask исправно работает')
    app.run(debug=True)