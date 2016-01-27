# coding: utf-8

import requests
import lxml.html
from datetime import datetime
from flask import render_template, redirect, url_for

from bin import app, town, town_table, TownList
from forms import EnterTown


def get_town_data():

    town_list = get_town_list()
    url = 'https://www.gismeteo.ru/city/'

    # doc = requests.get(url)
    # res = lxml.html.document_fromstring(doc.text)
    # town.temperature = res.xpath('//*[@class="current-weather__thermometer current-weather__thermometer_type_now"]')[0].text
    # town.comment = res.xpath('//*[@class="current-weather__comment"]')[0].text


def get_town_list():
    doc = request_town_page()
    res = lxml.html.document_fromstring(doc)
    towns = get_town_elements(res)
    town_list = [extract_town(element) for element in towns]
    return town_list


def request_town_page():
    url = 'https://www.gismeteo.ru/city/'
    date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    param = 'gis' + date + '00'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    }
    res = requests.get(url, params={
        param: town.name,
        'searchQueryData': '',
    }, headers=headers)
    return res.text


def get_town_elements(doc):
    return doc.xpath(u'//*[contains(text(), "пункты")]/following-sibling::div[1]/div/ul/li')


def extract_town(town_element):

    item = TownList()
    item.reference = str(town_element.xpath('./a[1]/@href')[0])
    item.region = town_element.xpath('./a[2]')[0].text
    item.area = town_element.xpath('./a[3]')[0].text
    item.country = town_element.xpath('./a[4]')[0].text
    return item


@app.route('/')
def index():
    if town.name:
        get_town_data()
        return render_template('showtown.html', name=town_table[town.name.lower()][1], temp=town.temperature, comment=town.comment)
    return redirect(url_for('select_town'))


@app.route('/show_townlist')
def show_townlist():
    town_list = get_town_list()
    return render_template('show_townlist.html', town_list=town_list)


@app.route('/select_town/', methods=['GET', 'POST'])
def select_town():
    form = EnterTown()
    if form.validate_on_submit():
        town.name = form.name.data
        return redirect(url_for('index'))
    return render_template('selecttown.html', form=form)
