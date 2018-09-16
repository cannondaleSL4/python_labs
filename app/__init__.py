from flask import Flask
from flask_bootstrap import Bootstrap
import os


template_dir = os.path.abspath('./templates')
static_dir = os.path.abspath('./static')

def create_app():
  print(template_dir)
  app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
  Bootstrap(app)

  return app

app = create_app()

from app import routes
