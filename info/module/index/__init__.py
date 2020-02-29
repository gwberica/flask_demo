# 首页模块
from flask import Blueprint

# 创建蓝图
index_bp = Blueprint("index", __name__)

# 发现蓝图
from .views import *
