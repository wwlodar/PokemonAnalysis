from flask import render_template, request
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
    pokemon_number = models.number_of_pokemon(df, region)
    best = models.best_pokemon(df, region)
    most_common_pokemon = models.most_common_pokemon(df)
    least_common_pokemon = models.least_common_pokemon(df)
    worst = models.worst_pokemon(df, region)
    total_number_of_legendary_pokemon = models.total_number_of_legendary_pokemon(df)
    number_of_legendary_pokemon = models.number_of_legendary_pokemon(df, region)
    legendary_evolved = models.legendary_evolved(df)
    legendary_table = models.legendary_pokemon(df, region)
    titles = ' '
    return render_template('regional.html', data=data, region=region, CP_data=CP_data, evolution_data=evolution_data,
                           pokemon_number=pokemon_number,
                           total_number_of_legendary_pokemon=total_number_of_legendary_pokemon,
                           number_of_legendary_pokemon=number_of_legendary_pokemon,
                           legendary_evolved=legendary_evolved,
                           most_common_pokemon=most_common_pokemon,
                           least_common_pokemon=least_common_pokemon,
                           tables=[best.to_html(index=False, classes="mystyle")],
                           table2=[worst.to_html(index=False, classes="mystyle")],
                           table3=[legendary_table.to_html(index=False, classes="mystyle")],
                           titles=titles)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
