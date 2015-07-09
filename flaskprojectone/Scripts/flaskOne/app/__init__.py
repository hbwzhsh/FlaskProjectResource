# -*- coding: utf-8 -*-
from flask import Flask               # 引入 flask
app = Flask(__name__)                   # 实例化一个flask 对象
from app import views                  # 导入 views 模块,必须放在后面才能正常引入否则会报引入包错误
# from app import views

