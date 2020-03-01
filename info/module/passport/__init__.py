# 首页模块
from flask import Blueprint

# 创建蓝图
passport_bp = Blueprint("index", __name__,url_prefix="/passport")

# 发现蓝图
from .views import *
