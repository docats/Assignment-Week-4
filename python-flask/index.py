from distutils.log import debug
from flask import Flask # 載入Flask 
from flask import request # 載入Request物件
from flask import render_template

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
    # print("請求方法",request.method)
    # print("通訊協定",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整的網址",request.url)
    print("瀏覽器和作業系統",request.headers.get("user-agent"))
    print("語言偏好",request.headers.get("accept-language"))
    print("引薦網址",request.headers.get("referrer"))
    return render_template('index.html') # 回傳網站首頁內容

# 建立路徑 /member對應的處理函式
@app.route("/member")
def member():
    return  render_template('member.html')

# 建立路徑 /error對應的處理函式
@app.route("/error")
def error():
    return render_template('error.html')

# 請求物件的觀察和使用


# 動態路由:建立路徑 /user/使用者名稱，對應的處理函式
# @app.route("/user/<username>")
# def handleUser(username):
#     if username == "Iris":
#         return "你好 "+username
#     else:
#         return "Hello "+username

# (啟動網站伺服器)host,port,debug等參數，要在這邊設定
app.run(port=3000) 

