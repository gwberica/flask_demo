import datetime

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from config import config_dict

# 1.创建app对象
app = Flask(__name__)
config_class = config_dict["dev"]
# 2将配置注册到app中
app.config.from_object(config_class)
# 3创建数据库对象
db = SQLAlchemy(app)
# 4 创建redis链接对象
redis_store = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, db=config_class.REDIS_DB, decode_responses=True)

# 5 开启flask后端的csrf的保护机制
csrf = CSRFProtect(app)

# 6借用第三方session类 修改session的存储位置
Session(app)
# 7创建manage管理类
manage = Manager(app)


@app.route("/")
def index():
    session["name"] = "curry"
    return "hello world"


if __name__ == '__main__':
    manage.run()
