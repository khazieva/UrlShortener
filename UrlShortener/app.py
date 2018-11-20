import os
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
        g.db_connection = storage.init_db()
    return g.db_connection
