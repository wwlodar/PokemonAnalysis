import numpy as np
import pandas as pd
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from app import app



df = pd.read_csv('app/PokemonDatabase.csv', delimiter = ',')
df = df.drop(["Pokemon Id", "Original Pokemon ID", "Special Event Ability", "Special Event Ability Description",
                  "Primary Egg Group", "Secondary Egg Group", "Egg Cycle Count", "Health EV", "Attack EV",
                  "Defense EV", "Special Attack EV", "Special Defense EV", "Speed EV", "EV Yield Total",
                  "Evolution Details"], axis=1)
df["Legendary Type"] = df["Legendary Type"].astype(str)
df["Alternate Form Name"] = df["Alternate Form Name"].astype(str)
df["Secondary Type"] = df["Secondary Type"].astype(str)
cols_to_check = ["Pokemon Name", "Classification", "Primary Type", "Secondary Type", "Alternate Form Name",
                 "Region of Origin", "Legendary Type"]
for col in cols_to_check:
    df[col] = df[col].map(lambda x: x.replace('"', ''))


def grass_pokemon(df1):
    df1 = df1.sort_index()
    df1 = df1.loc[df1["Primary Type"] == 'Grass']
    return df1


def region_group_count(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1["count"] = 1
    df1 = df1.groupby(["Primary Type"]).count()["count"].copy()
    mask = df1 <= 3
    mask2 = df1 >= 20
    colors = np.array(['g'] * len(df1))
    colors[mask.values] = 'r'
    colors[mask2.values] = 'r'
    df1.plot(kind="bar", x="Primary Type", y="count", figsize=(9, 5), color=colors)
    plt.title("Pokemon Types in the region")
    plt.xticks(fontsize=9, rotation=40)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


def group_count(df1):
    df1["count"] = 1
    df1 = df1.groupby(["Primary Type"]).count()["count"].copy()
    df1.plot(kind="bar", x="Primary Type", y="count")
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


# region_group_count(df, region)
#print(df.loc[df["Alternate Form Name"].str.contains("Mega", na=False)])

#def group_count():
 #   df["count"] = 1
  #  print(df.groupby(["Primary Type"]).count()["count"])

##generation_group_count()


## for each generation and type show data/ for all show data:
## how many pokemons are in each type
## how many come from evolution
## which one has highest CP
## compare weakest and strongest pokemon in each group (whisker chart)
## legendary and mythical pokemon
