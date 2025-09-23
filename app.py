from flask import Flask
from flask import render_template
from flask import request
import sqlite3


app = Flask(__name__)

connection = sqlite3.connect('maindata.db', check_same_thread=False)
cursor = connection.cursor()

def product_catg():
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

def productindex():
    listDB = cursor.execute('SELECT * FROM product LIMIT 12')
    return listDB.fetchall()

def accounts():
    cursor.execute('SELECT * FROM account')
    return cursor.fetchall()

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
    
@app.route('/personalacc', methods=['GET', 'POST'])
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

@app.route('/category/girlscl')
def girls_clothing():
    shop = product_catg()
    return render_template('category_girlscl.html', shop = shop)

@app.route('/category/boyscl')
def boys_clothing():
    shop = product_catg()
    return render_template('category_boysscl.html', shop = shop)

@app.route('/category/girls.shoes')
def  girls_shoes():
    return render_template('category_girls_shoes.html')

@app.route('/category/boys.shoes')
def boys_shoes():
    return render_template('category_boys_shoes.html')

if __name__ == "__main__":
    print('Flask исправно работает')
    app.run(debug=True)