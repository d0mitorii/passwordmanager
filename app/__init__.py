from flask import Flask

app = Flask(__name__)
app.config.from_json('config.json')

from .routes import *

app.register_error_handler(404, page_not_found)