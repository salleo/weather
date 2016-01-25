from flask import render_template, redirect, request, url_for

from bin import app, town
from forms import EnterTown


def gettowndata():


@app.route('/')
def index():
    if town.name:
        return render_template('showtown.html', name=town.name, temp=town.temperature)
    return redirect(url_for('select_town'))


@app.route('/select_town/', methods=['GET', 'POST'])
def select_town():
    form = EnterTown()
    if form.validate_on_submit():
        town.name = form.name.data
        return redirect(url_for('index'))
    return render_template('selecttown.html', form=form)
