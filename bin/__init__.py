# coding: utf-8

from flask import Flask


app = Flask(__name__, template_folder='../templates')
app.config.from_object('config')


class Town(object):

    def __init__(self):
        self.name = ''
        self.temperature = ''
        self.comment = ''


class TownList(object):

    def __init__(self):
        self.reference = ''
        self.region = ''
        self.area = ''
        self.country = ''

town_table = {'dzerzhinsk': ['972', u'Дзержинск'], 'moscow': ['moscow', u'Москва']}

town = Town()

from bin import views
