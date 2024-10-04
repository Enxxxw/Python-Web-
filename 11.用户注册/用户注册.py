from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/register', methods=['GET', "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')

    else:
        # 1.接收用户通过POST形式发送过来的数据
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobby")
        city = request.form.get("city")
        skill_list = request.form.getlist("skill")
        more = request.form.get("more")
        print(user, pwd, gender, hobby_list, city, skill_list, more)
        # 将用户信息写入文件中实现注册、写入到excel中实现注册、写入数据库中实现注册

        # 2.给用户再返回结果
        return "注册成功"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        print(request.form)
        return "登陆成功"


@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


# @app.route("/do/reg", methods=["GET"])
# def do_register():
#     # 1.接收用户通过GET形式发送过来的数据
#     print(request.args)
#     # 2.给用户再返回结果
#     return "注册成功"
#
#
# @app.route("/post/reg", methods=["POST"])
# def post_register():
#     # 1.接收用户通过POST形式发送过来的数据
#     print(request.form)
#     # 2.给用户再返回结果
#     return "注册成功"


if __name__ == '__main__':
    app.run()