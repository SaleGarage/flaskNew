from flask import Flask

app = Flask(__name__)


@app.route('/')
def hi():  # put application's code here
    return 'sdfsdf!'


@app.route('/index/')
def index():  # put application's code here
    car = {'name': ('bugatty',

                        'https://libertycity.ru/uploads/download/gta5_bugatti/fulls/j4q9k776k31rt5p2jnd2823s63/15043684584016_f61541-1.jpg')}
    return ''' <html>
    <head>
    <title> Самые крутые машины </title>
    </head>
    <body> 
    <h1> Вот самая красивая машина ''' + car['name'][0] + ''' </h1>
    <img src=''' + car['name'][1] + '''>
    </body>
    </html>
    
    '''


@app.route('/petya/')
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


if __name__ == '__main__':
    app.run(debug=True)
