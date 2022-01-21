from distutils.log import debug
from flask import Flask # 載入Flask 
from flask import request # 載入Request物件(要取得POST參數值)
from flask import redirect # 載入redirect函式
from flask import render_template
from markupsafe import re #使用樣板引擎

# 建立 Application物件，可以設定靜態檔案的路徑處理
# 所有在 static 資料夾底下的檔案，都對應到網址路徑 /static/ 檔案名稱
app=Flask(
    __name__,
    static_folder="static", # 靜態檔案的資料夾名稱
    static_url_path="/static" #靜態檔案對應的網址路徑
    ) 


# 建立路徑 / 對應的處理函式
@app.route('/')
def index(): #用來回應路徑 / 的處理函式
    # 網址的導向
    # return redirect("/en/") # 導向到路徑 /en/

    return render_template('index.html') # 回傳網站首頁內容

#建立路徑 /sigin對應的處理函式
@app.route("/sigin",methods=['POST'])
def sigin():
    # username = request.values['uname']
    # password = request.values['psw']
    username = request.form['uname']
    password = request.form['psw']
    print("長度",len(username))
    if username == "test" and password == "test":
        return redirect('/member')
    elif len(username)==0 or len(password)==0:
        return redirect('/empty/?message=帳號或密碼不能為空')
    else:
        # input=request.args.get("uname","")
        return redirect('/error/?message=帳號或密碼錯誤')

# 建立路徑 /member對應的處理函式
@app.route("/member")
def member():
    
    return  render_template('member.html')

# 建立路徑 /error對應的處理函式
@app.route("/error/",methods=['GET'])
def error():
    message=request.args.get("message")
    return render_template('error.html',message=message)

# 建立路徑 /empty對應的處理函式
@app.route("/empty/",methods=['GET'])
def empty():
    message=request.args.get("message")
    return render_template('empty.html')


# 動態路由:建立路徑 /user/使用者名稱，對應的處理函式
# @app.route("/user/<username>")
# def handleUser(username):
#     if username == "Iris":
#         return "你好 "+username
#     else:
#         return "Hello "+username

# (啟動網站伺服器)host,port,debug等參數，要在這邊設定
app.run(port=3000) 
