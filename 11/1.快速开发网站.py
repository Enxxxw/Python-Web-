from flask import Flask, render_template

app = Flask(__name__)

@app.route("/show/info")
def show_info():
    # Flask内部会自动打开这个文件，并读取内容，将内容给用户返回。
    # 默认：去当前项目目录的templates文件夹中找。
    return render_template("show_info.html")


@app.route("/get/news")
def get_news():
    return render_template("get_news.html")


@app.route("/show/pic")
def show_pic():
    return render_template("show_pic.html")


@app.route("/goods/list")
def goods_list():
    return render_template("goods_list.html")


@app.route("/user/list")
def user_list():
    return render_template("user_list.html")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run()