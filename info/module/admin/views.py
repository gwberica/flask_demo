import datetime
import time

from . import room_info_bp, new_room_info_bp, hot_room_bp, country_hp, room_hp, type_hp, personal_hp
from flask import request, render_template

from ...utils.mysql_db import db
from ...utils.util import unix_time


@room_info_bp.route("/room_info")
def room_info():
    try:
        page = int(request.args.get("p", 1))
    except:
        page = 1
    sort_str = request.args.get("sort")

    skip_num = (page - 1) * 15
    sql = "select * from room_info limit {} ,15".format(skip_num)
    if sort_str:
        sql = "select * from room_info  order by {} desc,day_sumamount desc limit {} ,15".format(sort_str, skip_num)
    result_tuple = db.fetchall(sql)
    data = []
    for result in result_tuple:
        value_dict = {}
        barid = result[0]
        barlevel = result[3]
        onlinenum = result[4]
        heatnow = result[5]
        name = result[6]
        isofficial = result[7]
        labelname = result[8]
        data_time = result[9]
        day_sumamount = result[11]
        week_sumamount = result[12]
        membernum = result[13]
        value_dict["barid"] = barid
        value_dict["barlevel"] = barlevel
        value_dict["onlinenum"] = onlinenum
        value_dict["heatnow"] = heatnow
        value_dict["name"] = name
        value_dict["isofficial"] = isofficial
        value_dict["labelname"] = labelname
        value_dict["data_time"] = data_time
        value_dict["day_sumamount"] = day_sumamount
        value_dict["week_sumamount"] = week_sumamount
        value_dict["membernum"] = membernum
        data.append(value_dict)

    return render_template("room_info.html", data=data)


@new_room_info_bp.route("/new_room_info")
def new_room_info():
    try:
        page = int(request.args.get("p", 1))
    except:
        page = 1
    sort_str = request.args.get("sort")

    skip_num = (page - 1) * 15
    sql = "select * from new_room_info limit {} ,15".format(skip_num)
    if sort_str:
        sql = "select * from new_room_info  order by {} desc  limit {} ,15".format(sort_str, skip_num)
    result_tuple = db.fetchall(sql)
    data = []
    for result in result_tuple:
        value_dict = {}
        barid = result[0]
        barlevel = result[4]
        onlinenum = result[5]
        heatnow = result[6]
        name = result[7]
        isofficial = result[8]
        labelname = result[9]
        data_time = result[10]
        day_sumamount = result[12]
        week_sumamount = result[13]
        membernum = result[14]
        value_dict["barid"] = barid
        value_dict["barlevel"] = barlevel
        value_dict["onlinenum"] = onlinenum
        value_dict["heatnow"] = heatnow
        value_dict["name"] = name
        value_dict["isofficial"] = isofficial
        value_dict["labelname"] = labelname
        value_dict["data_time"] = data_time
        value_dict["day_sumamount"] = day_sumamount
        value_dict["week_sumamount"] = week_sumamount
        value_dict["membernum"] = membernum
        data.append(value_dict)

    return render_template("new_room_info.html", data=data)


@hot_room_bp.route("/hot_room")
def new_room_info():
    try:
        page = int(request.args.get("p", 1))
    except:
        page = 1
    sort_str = request.args.get("sort")

    skip_num = (page - 1) * 15
    sql = "select * from hot_room_info limit {} ,15".format(skip_num)
    if sort_str:
        sql = "select * from hot_room_info  order by {} desc  limit {} ,15".format(sort_str, skip_num)
    result_tuple = db.fetchall(sql)
    data = []
    for result in result_tuple:
        value_dict = {}
        barid = result[0]
        barlevel = result[4]
        onlinenum = result[5]
        heatnow = result[6]
        name = result[7]
        isofficial = result[8]
        labelname = result[9]
        data_time = result[10]
        value_dict["barid"] = barid
        value_dict["barlevel"] = barlevel
        value_dict["onlinenum"] = onlinenum
        value_dict["heatnow"] = heatnow
        value_dict["name"] = name
        value_dict["isofficial"] = isofficial
        value_dict["labelname"] = labelname
        value_dict["data_time"] = data_time
        data.append(value_dict)

    return render_template("hot_room.html", data=data)


@country_hp.route("/country")
def country():
    data_time = request.args.get("data_time", '')
    if not data_time:
        data_time = (datetime.date.today()).strftime("%Y-%m-%d")
        if int(time.time()) - 64800 < unix_time(dt=data_time):
            data_time = (datetime.datetime.now() + datetime.timedelta(days=-1)).date().strftime('%Y-%m-%d')
    sql = "select * from country_aggregate_info where data_time='{}' ORDER BY room_num DESC".format(data_time)
    result_tuple = db.fetchall(sql)
    data = []
    for result in result_tuple:
        value_dict = {}
        value_dict["date_time"] = result[0]
        value_dict["name"] = result[1]
        value_dict["room_num"] = result[2]
        value_dict["day_sumamount"] = result[3]
        value_dict["avg_day_sumamount"] = result[4]
        value_dict["week_sumamount"] = result[5]
        value_dict["avg_week_sumamount"] = result[6]
        value_dict["onlinenum"] = result[7]
        value_dict["avg_onlinenum"] = result[8]
        data.append(value_dict)
    data = sorted(data, key=lambda x: x['room_num'], reverse=True)
    return render_template("country.html", data=data)


@room_hp.route("/room")
def room():
    sql = "select * from room_aggregate_info  ORDER BY data_time DESC"
    result_tuple = db.fetchall(sql)
    data = []
    for result in result_tuple:
        value_dict = {}
        value_dict["date_time"] = result[0]
        value_dict["room_num"] = result[1]
        value_dict["day_sumamount"] = result[2]
        value_dict["avg_day_sumamount"] = result[3]
        value_dict["onlinenum"] = result[4]
        value_dict["avg_onlinenum"] = result[5]
        value_dict["week_sumamount"] = result[6]
        value_dict["avg_week_sumamount"] = result[7]

        data.append(value_dict)
    return render_template("room.html", data=data)


@type_hp.route("/type")
def type_demo():
    date_time = request.args.get("date_time", '')
    if not date_time:
        date_time = (datetime.date.today()).strftime("%Y-%m-%d")
        if int(time.time()) - 64800 < unix_time(dt=date_time):
            date_time = (datetime.datetime.now() + datetime.timedelta(days=-1)).date().strftime('%Y-%m-%d')

    sql_data_time = "select data_time from type_aggregate_info GROUP BY data_time desc limit 7"
    date_time_list = []
    date_time_lists = db.fetchall(sql_data_time)
    for i in date_time_lists:
        date_time_list.append(i[0])
    sql = "select * from type_aggregate_info where data_time='{}' ORDER BY room_num DESC".format(date_time)
    result_tuple = db.fetchall(sql)
    data = []
    for result in result_tuple:
        value_dict = {}
        value_dict["date_time"] = result[0]
        value_dict["name"] = result[1]
        value_dict["room_num"] = result[2]
        value_dict["day_sumamount"] = result[3]
        value_dict["avg_day_sumamount"] = result[4]
        value_dict["week_sumamount"] = result[5]
        value_dict["avg_week_sumamount"] = result[6]
        value_dict["onlinenum"] = result[7]
        value_dict["avg_onlinenum"] = result[8]

        data.append(value_dict)
    data = sorted(data, key=lambda x: x['room_num'], reverse=True)
    return render_template("type.html", data=data, datatime=date_time_list)


@personal_hp.route("/personal")
def personal():
    barid = request.args.get("barid")
    sql = "select * from room_info where barid= {} order by data_time desc ".format(barid)
    result_tuple = db.fetchall(sql)
    data = []
    for result in result_tuple:
        value_dict = {}
        barid = result[0]
        barlevel = result[3]
        onlinenum = result[4]
        heatnow = result[5]
        name = result[6]
        isofficial = result[7]
        labelname = result[8]
        data_time = result[9]
        day_sumamount = result[11]
        week_sumamount = result[12]
        membernum = result[13]
        value_dict["barid"] = barid
        value_dict["barlevel"] = barlevel
        value_dict["onlinenum"] = onlinenum
        value_dict["heatnow"] = heatnow
        value_dict["name"] = name
        value_dict["isofficial"] = isofficial
        value_dict["labelname"] = labelname
        value_dict["data_time"] = data_time
        value_dict["day_sumamount"] = day_sumamount
        value_dict["week_sumamount"] = week_sumamount
        value_dict["membernum"] = membernum
        data.append(value_dict)

    return render_template("personal.html", data=data)
