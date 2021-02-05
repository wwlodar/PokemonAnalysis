from flask import Flask, render_template, request
from app import app
from app import regional_plots
from app import models

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
    pokemon_number = models.number_of_pokemon(df,region)
    biggest_group = models.biggest_pokemon_group(df,region)
    best = models.best_pokemon(df,region)
    worst = models.worst_pokemon(df, region)
    titles = ' '
    return render_template('regional.html', data=data, region=region, CP_data=CP_data, evolution_data=evolution_data,
                           pokemon_number=pokemon_number, biggest_group=biggest_group,
                           tables=[best.to_html(index=False)], table2=[worst.to_html(index=False)], titles=titles)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
