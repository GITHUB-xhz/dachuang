from flask import Flask, render_template, request

import db

app = Flask(__name__)


@app.route('/interact', methods=['POST', 'GET'])
def interact():
    return render_template("ro.interact.html")


# @app.route('/animation', methods=['POST', 'GET'])
# def animation():
#     if request.method == 'POST':
#         result = request.form
#     return render_template("ro.animation.html")


@app.route("/")
def show_users():
    sql = "select x,y,z from user"
    datas = db.query_data(sql)
    return render_template("ro.animation.html", datas=datas)

