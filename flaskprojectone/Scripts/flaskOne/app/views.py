# -*- coding: utf-8 -*-
from app import app
from flask import Flask, request, make_response, redirect, abort,render_template


@app.route('/')                                                                              #根目录 初始化路径
def login():
    return render_template("login.html")

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/setcookies')                                                                    #设置Cookies
def setcookies():
    response = make_response('<h1>settings,Cookies!</h1>')
    response.set_cookie('hellokitty', '22')
    return response

# @app.route('/getcookies')                                                                  #获取cookies
# def getusercookies():
# 	getcookies()


@app.route('/user/<name>')                                                                     #传递字符参数
def username(name):
    return '<h1>hello,%s</h1>' % name

@app.route('/user/id/<int:id>')                                                                #传递整形参数
def userid(id):
    return '<h1> userid ,%s</h1>' %id

@app.route('/redirect')                                                                       #重定向
def userredirect():
    return redirect("https://www.baidu.com")

@app.route('/user/abort/<id>')                                                                 #触发404
def userabort(id):
	if id:
		abort(404)
	return '<h1>user,%s</h1>' % id

@app.route('/templates')
def index_template():
    return render_template('index.html')

@app.route('/templates/key/<values>')
def index_keyv_alues(value):
    #uaer = {'title':'home', 'name':'alice'}
    return render_template('index.html', user=value)