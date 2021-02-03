import numpy as np
import pandas as pd
import base64
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

region = "Sinnoh"
df = pd.read_csv(r'C:\Users\Weronika\PycharmProjects\PokemonAnalysis\app\PokemonDatabase.csv', delimiter = ',')
df = df.drop(["Pokemon Id", "Original Pokemon ID", "Special Event Ability", "Special Event Ability Description",
                  "Primary Egg Group", "Secondary Egg Group", "Egg Cycle Count", "Health EV", "Attack EV",
                  "Defense EV", "Special Attack EV", "Special Defense EV", "Speed EV", "EV Yield Total",
                  "Evolution Details"], axis=1)
df["Legendary Type"] = df["Legendary Type"].astype(str)
df["Alternate Form Name"] = df["Alternate Form Name"].astype(str)
df["Secondary Type"] = df["Secondary Type"].astype(str)
df["Pre-Evolution Pokemon Id"] = df["Pre-Evolution Pokemon Id"].astype(str)
cols_to_check = ["Pokemon Name", "Classification", "Primary Type", "Secondary Type", "Alternate Form Name",
                 "Region of Origin", "Legendary Type"]
for col in cols_to_check:
    df[col] = df[col].map(lambda x: x.replace('"', ''))


def region_group_count(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1["count"] = 1
    df1 = df1.groupby(["Primary Type"]).count()["count"].copy()
    df1.plot(kind="bar", x="Primary Type", y="count")
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

region = "Kanto"
def pokemon_evolution_ratio(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    no_evolutions = df1.loc[df1["Pre-Evolution Pokemon Id"] == "nan"].count()[0]
    two_evolutions = df1.loc[df1["Pre-Evolution Pokemon Id"] != "nan"].count()[0]
    plt.pie([no_evolutions, two_evolutions])
    plt.show()


pokemon_evolution_ratio(df,region)


#print(df.loc[df["Alternate Form Name"].str.contains("Mega", na=False)])
#fig = Figure()
#ax = fig.subplots()
#ax.plot(df_array)
#figx.show()
# Generate the figure **without using pyplot**.