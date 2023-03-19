from flask import Flask, render_template
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

# 基本结构，一个函数，绑定一个装饰器
# 为函数绑定 url ；戴上装饰器
@app.route("/")
# 请求处理函数
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# 使用 escape 获取变量值
# 用户输入的数据会包含恶意代码，所以不能作为响应返回，需要使用 markupsafe 提供的 escape 函数 对 name 变量进行转译
# 比如 把 < 转换成 &lt；这样在响应时浏览器就不会把他们当作代码执行
@app.route("/user/<name>")
def user_page(name):
    return f'User: {escape(name)}'

'''
最后一个可以修改的部分就是视图函数的名称了。首先，视图函数的名字是自由定义的，和 URL 规则无关。
和定义其他函数或变量一样，只需要让它表达出所要处理页面的含义即可。
除此之外，它还有一个重要的作用：作为代表某个路由的端点（endpoint），同时用来生成视图函数对应的 URL。
对于程序内的 URL，为了避免手写，Flask 提供了一个 url_for 函数来生成 URL，它接受的第一个参数就是端点值，默认为视图函数的名称：
'''
@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route("/index")
def index():
    return render_template("index.html", name = name, movies = movies)
