from flask import Flask, render_template, request
from app import app
from app import regional_plots


df = regional_plots.df
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/regional')
def regionals():
    region = request.args.get('region')
    data = regional_plots.region_group_count(df, region)
    CP_data = regional_plots.region_cp_count(df, region)
    evolution_data = regional_plots.pokemon_evolution_ratio(df, region)
    return render_template('regional.html', data=data, region=region, CP_data=CP_data, evolution_data=evolution_data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
