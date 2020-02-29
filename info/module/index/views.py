from flask import session

from . import index_bp

# 使用蓝图
from info import redis_store


@index_bp.route("/")
def index():
    print(redis_store)
    redis_store.set("name", "laowang")
    session["name"] = "curry"
    return "hello world"
