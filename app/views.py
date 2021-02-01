from flask import Flask, render_template, request
import requests
from app import app
from app import plotss


from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

df = plotss.df
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/regional')
def regionals():
    region = request.args.get('region')
    data = plotss.region_group_count(df, region)
    return render_template('regional.html', data = data, region=region)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
