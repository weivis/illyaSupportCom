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

  app.debug=True

  config_extensions(app)

  config_blueprint(app)

  config_errorhandler(app)

  return app
