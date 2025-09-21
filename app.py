from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_page.html')

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