# -*- coding: utf-8 -*-
from flask import Flask, render_template

from app import Config
from app.Blueprint import config_blueprint
from app.Extensions import config_extensions

def config_errorhandler(app):
  
    # 错误页面配置
    @app.errorhandler(404)
    def page_not_found(e):
        return str(e)

def create_app():
  app = Flask(__name__, static_folder='static')

  app.config.from_object(Config)

  config_extensions(app)

  config_blueprint(app)

  config_errorhandler(app)

  @app.route('/Api接口文档说明')
  def AppDocs():
      '''
        这是一个不可用接口

        请求说明
            用户请求需要登录的接口时候 头部必须携带Token
        
        公共返回码说明
            200 成功
            201-210 自定义
            10086 用户在未登录的情况下请求需要登录的接口

      '''
      
  return app