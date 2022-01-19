from distutils.log import debug
from flask import Flask # 載入Flask 
from flask import render_template
app=Flask(__name__) # 建立 Application物件

# 建立網站首頁的回應方式
@app.route('/')

def index(): #用來回應網站首頁的函式
    return render_template('index.html') # 回傳網站首頁內容

app.run(port=3000) # host,port,debug要在這邊設定

