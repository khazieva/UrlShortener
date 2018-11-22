import os
import base62
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import storage


# Конфигурация.
DATABASE = '/tmp/url_shortener.sqlite'
DEBUG = True
SECRET_KEY = 'development key'


# Создаем приложение.
app = Flask(__name__)
app.config.from_object(__name__)


# Загружаем конфиг по умолчанию и переопределяем в конфигурации часть значений через переменную окружения.
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'url_shortener.sqlite'),
    DEBUG=True,
    SECRET_KEY='development key'
    ))
app.config.from_envvar('APP_SETTINGS', silent=True)


def get_db():
    """ Если еще нет соединения с БД, открыть новое - для текущего контекста приложения. """
    if not hasattr(g, 'db_connection'):
        g.db_connection = storage.init_db(app.config['DATABASE'])
        g.current_index = len(g.db_connection)
    return g.db_connection


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_link', methods=['POST'])
def generate_link():
    link = request.form['inputlink']
    if len(link) == 0:
        return redirect(url_for('index'))
    db = get_db()
    db[g.current_index] = link
    result_link = url_for('open_link', short_link=base62.encode(g.current_index), _external=True)
    g.current_index += 1
    return render_template('result.html', result_link=result_link)


@app.route('/<short_link>')
def open_link(short_link):
    index = base62.decode(short_link)
    db = get_db()
    open_link = db[index]
    return redirect(open_link)


if __name__ == '__main__':
    app.run()
