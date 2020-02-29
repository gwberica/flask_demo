from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect


# 创建项目配置类


class Config(object):
    # 开启debug模式
    DEBUG = True
    # mysql的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:qiushibaike1566@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 1


# 1.创建app对象

app = Flask(__name__)

# 2将配置注册到app中
app.config.from_object(Config)
# 3创建数据库对象
db = SQLAlchemy(app)
# 4 创建redis链接对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, decode_responses=True)

# 5 开启flask 的csrf的保护机制
csrf = CSRFProtect()


@app.route("/demo")
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=1234)
