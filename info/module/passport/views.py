from . import passport_bp
from flask import request


@passport_bp.route("/image_code")
def get_imagecode():
    # 获取图片验证码图片
    # 1获取参数
    # 1.1 获取前端传递过来的uuid
    imageCodeId = request.args.get("imageCodeId")
    # 2校验参数
    # 2.1 判断是否为空
    if not imageCodeId:
        abort(404)
    # 3逻辑处理
    # 3.1
    # 4返回值处理
