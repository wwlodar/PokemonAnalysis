import numpy as np
import pandas as pd
import base64
from io import BytesIO
import matplotlib.pyplot as plt


df = pd.read_csv('app/PokemonDatabase.csv', delimiter=',')
df = df.drop(["Pokemon Id", "Original Pokemon ID", "Special Event Ability", "Special Event Ability Description",
              "Primary Egg Group", "Secondary Egg Group", "Egg Cycle Count", "Health EV", "Attack EV",
              "Defense EV", "Special Attack EV", "Special Defense EV", "Speed EV", "EV Yield Total",
              "Evolution Details"], axis=1)
df["Legendary Type"] = df["Legendary Type"].astype(str)
df["Alternate Form Name"] = df["Alternate Form Name"].astype(str)
df["Secondary Type"] = df["Secondary Type"].astype(str)
df["Legendary Type"] = df["Legendary Type"].astype(str)
df["Pre-Evolution Pokemon Id"] = df["Pre-Evolution Pokemon Id"].astype(str)
cols_to_check = ["Pokemon Name", "Classification", "Primary Type", "Secondary Type", "Alternate Form Name",
                 "Region of Origin", "Legendary Type"]
for col in cols_to_check:
    df[col] = df[col].map(lambda x: x.replace('"', ''))
df.loc[df["Alternate Form Name"] == 'nan', ["Pokemon Name"]] = df["Pokemon Name"]
df.loc[df["Alternate Form Name"] != 'nan', ["Pokemon Name"]] = df["Pokemon Name"] + str(" ") + \
                                                               (df["Alternate Form Name"])


def region_group_count(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1["count"] = 1
    df1 = df1.groupby(["Primary Type"]).count()["count"].copy()
    mask = df1 <= 3
    mask2 = df1 >= 20
    colors = np.array(['g'] * len(df1))
    colors[mask.values] = 'm'
    colors[mask2.values] = 'y'
    df1.plot(kind="bar", x="Primary Type", y="count", figsize=(8, 5), color=colors)
    plt.title("Pokemon Types in the region")
    plt.ylabel("Quantity")
    plt.xticks(fontsize=9, rotation=40)
    buf = BytesIO()
    plt.savefig(buf, format="png", transparent=True)
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


def region_cp_count(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1.boxplot(by="Primary Type", column="Base Stat Total", figsize=(8, 5), grid=False, labels=None,
                color={'medians': 'purple',
                       "boxes": "green",
                       "whiskers": "black",
                       }, medianprops={'linewidth': 3}, capprops={'linewidth': 3}, boxprops={'linewidth': 2.5})
    title_boxplot = 'Combat Power by Pokemon Type'
    plt.title(title_boxplot)
    ax1 = plt.axes()
    ax1.xaxis.set_label_text('foo')
    ax1.xaxis.label.set_visible(False)
    plt.suptitle('')
    plt.xticks(fontsize=9, rotation=40)
    plt.ylabel("Combat Power")
    buf = BytesIO()
    plt.savefig(buf, format="png", transparent=True)
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


def pokemon_evolution_ratio(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    no_evolutions = df1.loc[(df1["Pre-Evolution Pokemon Id"] == "nan") & (df1["Legendary Type"] == "nan")].count()[0]
    legendary_pokemon = df1.loc[(df1["Legendary Type"] != "nan") &
                                (df1["Pre-Evolution Pokemon Id"] == "nan")].count()[0]
    two_evolutions = df1.loc[df1["Pre-Evolution Pokemon Id"] != "nan"].count()[0]
    colors = ["#59d813", "#3e970d", "#870b37"]
    lables = ["Primary Pokemon", "Legendary Pokemon", "Evolved Pokemon"]
    plt.pie([no_evolutions, legendary_pokemon, two_evolutions], colors=colors, labels=lables, autopct="%.1f %%",
            pctdistance=0.6)
    plt.title("Evolved vs Primary Pokemon in the region")
    buf = BytesIO()
    plt.savefig(buf, format="png", transparent=True)
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data
