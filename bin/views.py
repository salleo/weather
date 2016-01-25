from flask import render_template, redirect, url_for
import requests
import lxml.html

from bin import app, town, towntable
from forms import EnterTown


def gettowndata():
    url = 'https://pogoda.yandex.ru/' + towntable[town.name.lower()][0]
    doc = requests.get(url)
    res = lxml.html.document_fromstring(doc.text)
    town.temperature = res.xpath('//*[@class="current-weather__thermometer current-weather__thermometer_type_now"]')[0].text
    town.comment = res.xpath('//*[@class="current-weather__comment"]')[0].text
    return


@app.route('/')
def index():
    if town.name:
        gettowndata()
        return render_template('showtown.html', name=town.name, temp=town.temperature, comment=town.comment)
    return redirect(url_for('select_town'))


@app.route('/select_town/', methods=['GET', 'POST'])
def select_town():
    form = EnterTown()
    if form.validate_on_submit():
        town.name = form.name.data
        return redirect(url_for('index'))
    return render_template('selecttown.html', form=form)
