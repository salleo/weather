from flask import Flask

app = Flask(__name__, template_folder='../templates')
app.config.from_object('config')


class Town(object):

    def __init__(self):
        self.name = ''
        self.temperature = '-5C'

town = Town()

from bin import views
