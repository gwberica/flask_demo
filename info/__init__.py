from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config_dict
import logging
from logging.handlers import RotatingFileHandler
from config import config_dict

# 3创建数据库对象
db = SQLAlchemy()
redis_store = None  # type:StrictRedis


def create_log(environ):
    # 设置日志级别
    logging.basicConfig(level=config_dict[environ].LOG_LEVER)
    # 创建日志记录器，设置日志保存位置，每个日志大小，保存日志数量
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式，日志等级，输入日志文件名 ，行数，日志内容等
    formatter = logging.Formatter('%(levelname)s %(filename)s: %(lineno)s %(message)s')
    # 设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 设置全局的日志工作对象
    logging.getLogger().addHandler(file_log_handler)


def create_app(environ):
    # create_log(environ)
    # 1.创建app对象

    app = Flask(__name__)
    config_class = config_dict[environ]
    # 2将配置注册到app中
    app.config.from_object(config_class)
    db.init_app(app)
    # 4 创建redis链接对象
    global redis_store
    redis_store = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, db=config_class.REDIS_DB,
                              decode_responses=True)
    # 5 开启flask后端的csrf的保护机制
    csrf = CSRFProtect(app)

    # 6借用第三方session类 修改session的存储位置
    Session(app)
    # 注册蓝图
    from info.module.index import index_bp
    app.register_blueprint(index_bp)
    return app
