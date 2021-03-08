# 视频上区分get和post方法用到这个代码
# 终端输入以下命令（=后面是文件名）    export    WWindows系统使用set
# set FLASK_APP=flaskdemo.py
# flask run
# 出现网址，使用网址。    后面拼接request加参数：http://127.0.0.1:5000/request?a=1&b=2


from flask import Flask, sessions, request, Request, make_response

app = Flask(__name__)
request: Request
app.secret_key = "key"

@app.route("/request", methods= ['POST', 'GET'])
def hello():
    # query接参数
    query = request.args
    post = request.form
    # 相当于打印query
    return f"query: {query}\n" \
        f"post: {post}"

@app.route("/session")
def session_handle():
    for k, v in request.args.items():
        # 和截图不一样。截图上是session
        sessions[k] = v
    # 和截图不一样。截图上是session
    resp = make_response({k: v for k, v in sessions.items()})
    for k, v in request.args.items():
        resp.set_cookie(f"cookie_{k}", v)
    return resp
