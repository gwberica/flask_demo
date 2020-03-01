from flask import session, render_template, current_app

from . import index_bp
from info import models, create_app
# 使用蓝图
from info import redis_store

import pymysql

pymysql.install_as_MySQLdb()


@index_bp.route("/")
def index():
    return render_template("index.html")


@index_bp.route("/favicon.ico")
def favicon():
    return current_app.send_static_file("news/favicon.ico")
