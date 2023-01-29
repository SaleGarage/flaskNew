import datetime
import os
import sqlite3

import git
from flask import Flask, render_template, session, redirect, url_for, request, abort, g, flash


from fdatabase import FdataBase
from forms import LoginForm

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'fdb.db')))
app.permanent_session_lifetime = datetime.timedelta(seconds=60)

@app.route('/update_server', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/Sa1eGarage/flaskNew')
        origin = repo.remotes.origin
        origin.pull()
        return 'Сайт обновился', 200
    else:
        return 'Возникла ошибка', 400
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn
def get_db():
    if not  hasattr(g, 'link_db'):
        g.link_db = connect_db()
        return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.route('/kuku')
def hi():  # put application's code here
    return 'sdfsdf!'


@app.route('/login')
def login():  # put application's code here
    form = LoginForm()
    return render_template('login.html', title='Авторизация пользователя', form=form)

@app.route('/login5')
def login5():  # put application's code here
    form = LoginForm()
    return render_template('login.html', title='Авторизация пользователя', form=form)

@app.route('/login2',methods=['POST', 'GET'])
def login2():  # put application's code here
    if 'userlogged' in session:
        return redirect(url_for('profile', username=session['userlogged']))
    elif request.method == 'POST' and request.form['username'] == 'kolya' and request.form['psw'] == '123':
        session['userlogged'] = request.form['username']
    elif request.method == 'POST' and request.form['username'] == 'Penguin' and request.form['psw'] == 'niugneP':
        session['userlogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userlogged']))

    return render_template('login2.html', title='Авторизация пользователя')
@app.route('/profile/<username>')
def profile(username):
    if 'userloggged' not in session or session['userlogged'] == username:
        abort(401)
    return f'<h1> Пользователь {username}'
@app.route('/login3')
def login3():  # put application's code here
    form = LoginForm()
    return render_template('login3.html', title='Авторизация пользователя', form=form)



@app.route('/')
@app.route('/index')
def index():  # put application's code here
    db = get_db()
    database = FdataBase(db)
    plane = {'name': ('N90IFJ',

                    'https://econet.ru/media/covers/17419/original.jpg?1433354137')}

    return render_template('index.html', name=plane['name'][0], foto=plane['name'][1], title='1', menu=database.getMenu())

@app.route('/post', methods=['POST', 'GET'])
def post():
    db = get_db()
    database = FdataBase(db)
    if request.method == 'POST':
        if len(request.form['name']) > 3 and len(request.form['post']) > 10:
            res = database.addPost(request.form['name'], request.form['post'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template('post.html', title='Добавить статью', menu=database.getMenu())

@app.route('/allposts')
def allpost():
    db = get_db()
    database = FdataBase(db)
    return render_template('allpost.html', title='Список постов', menu=database.getMenu(),
                           posts=database.getPostAnnoce())

@app.route('/post/<int:id_post>')
def showPost(id_post):
    db = get_db()
    database = FdataBase(db)
    title, post = database.getPost(id_post)
    if not title:
        abort(404)
    return render_template('aticle.html', title='title', menu=database.getMenu(), post=post)


@app.route('/petya')
def petya():  # put application's code here
    return ''' <h2> Александр Твардовский

Василий Теркин. Сборник

Лирика

РОДНОЕ

<br>Дорог израненные спины, </br>
<br>О дальних шумных городах. </br>
    </h2> '''


# @app.route('/user/<username>')
# def user_profile(username):  # put application's code here
#     return f"<h1>Здраствуй дорогой пользователь {username}</h1>"
#
#
# @app.route('/user/<int:post_id>')
# def show_post(post_id):  # put application's code here
#     return f"<h1>Горячая и свежая новость № {post_id}</h1>"
@app.errorhandler(401)
def user_not_found(error):
    return render_template("page401.html", title="Страница не найдена")
@app.errorhandler(404)
def page_not_found(error):
    return render_template("page404.html", title="Страница не найдена")

if __name__ == '__main__':
    app.run(debug=True)


