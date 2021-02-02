from flask import Flask, render_template, request
from app import app
from app import plotss


df = plotss.df
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/regional')
def regionals():
    region = request.args.get('region')
    data = plotss.region_group_count(df, region)
    CP_data = plotss.region_cp_count(df,region)
    return render_template('regional.html', data=data, region=region, CP_data=CP_data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
