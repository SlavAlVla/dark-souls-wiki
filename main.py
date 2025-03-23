from flask import Flask, render_template, request, url_for, redirect
import json
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)

# app.config.update(
#     SECRET_KEY = 'WOW SUCH SECRET'
# )

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/titanite')
def titanite():
    return render_template('titanite.html')

@app.route('/weapon')
def weapon():
    return render_template('weapon.html')

@app.route('/bosses')
def bosses():
    return render_template('bosses.html')

@app.route('/ornstein_and_smough')
def ornstein_and_smough():
    return render_template('ornstein_and_smough.html')

@app.route('/artorias')
def artorias():
    return render_template('artorias.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/lore')
def lore():
    return render_template('lore.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/anor_londo')
def anor_londo():
    return render_template('anor_londo.html')

@app.route('/pages')
def pages():
    with open('static/json/data.json', 'r', encoding="utf-8") as d:
        data = json.load(d)
        d.close()
    return render_template('pages.html', pages = data["pages"], pages_len = len(list(data["pages"].keys())), pages_items=list(data["pages"].keys()))

# @app.route('/cart')
# def cart():
#     return render_template('cart.html')

# @app.route('/contacts')
# def contacts():
#     return render_template('contacts.html')

# @app.route('/order', methods=['GET', 'POST'])
# def order():
#     # c = {"яблоко":100}
#     # print(c["яблоко"])
#     if request.method == 'POST':
#         for key in request.form:
#             if request.form[key] == "":
#                 return render_template('order.html', error = "Ошибка, не все поля заполнены")
#         print(request.form)
#     return render_template('order.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/product1')
# def product1():
#     date = datetime.strptime('2022.12.03', '%Y.%m.%d')
#     diff = date - datetime.now()
#     end_date = diff.days
#     return render_template('product1.html',
#                            action_name = "Осенние скидки",
#                            end_date = end_date,
#                            lucky_num = 1)

# @app.route('/product2')
# def product2():
#     return render_template('product2.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     login = 'admin'
#     password = 'admin'
#     if request.method == 'POST':
#         if request.form['login'] == login and request.form['password'] == password:
#             return redirect(url_for('index'))
#         else:
#             return render_template('login.html', error='Неверные данные')
#     return render_template('login.html')

if __name__ == "__main__":
    app.run()
