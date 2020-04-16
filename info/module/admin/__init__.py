# 首页模块
from flask import Blueprint

# 创建蓝图
room_info_bp = Blueprint("room_info", __name__)
new_room_info_bp = Blueprint("new_room_info", __name__)
hot_room_bp = Blueprint("hot_room", __name__)
country_hp = Blueprint("country", __name__)
room_hp = Blueprint("room", __name__)
type_hp = Blueprint("type", __name__)
personal_hp = Blueprint("personal", __name__)

# 发现蓝图
from .views import *