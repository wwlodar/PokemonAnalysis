import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
region = "Galar"


df = pd.read_csv('PokemonDatabase.csv', delimiter = ',')
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

def grass_pokemon(df):
    df = df.sort_index()
    df = df.loc[df["Primary Type"] == 'Grass']
    df.reset_index(drop=True, inplace = True)
    print(df)

# grass_pokemon(df)

def region_group_count(df, region):
    df = df.loc[df["Region of Origin"] == region]
    df["count"] = 1
    df = df.groupby(["Primary Type"]).count()["count"].copy()
    df.plot( kind = 'bar', x = "Primary Type", y = "count")
    plt.show()

def group_count(df):
    df["count"] = 1
    df = df.groupby(["Primary Type"]).count()["count"].copy()
    df.plot( kind = 'bar', x = "Primary Type", y = "count")
    plt.show()

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
