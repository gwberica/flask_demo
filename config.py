# 创建项目配置类
import datetime

from redis import StrictRedis


class Config(object):
    # mysql的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:qiushibaike1566@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 1
    # session 配置
    SECRET_KEY = "yjwhdusyshaonhouehjkdhfuidjhjxgjshnkhgfhdj"
    # 选择存储位置
    SESSION_TYPE = "redis"
    # 创建数据库对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    # 签名认证
    SESSION_USE_SIGNER = True
    # 是否永久存储
    SESSION_PERMANENT = False
    # 设置过期时长 秒数
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)


class DevelopmentConfig(Config):
    # 开发模式
    # 开启debug模式
    DEBUG = True


class ProductionConfig(Config):
    # 线上模式配置
    # 关闭debug模式
    DEBUG = False


config_dict = {
    "dev": DevelopmentConfig,
    "rel": ProductionConfig
}
