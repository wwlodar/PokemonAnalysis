import numpy as np
import pandas as pd
import matplotlib as plt
region = "Kanto"


df = pd.read_csv('PokemonDatabase.csv', delimiter= ',')
df = df.drop(["Pokemon Id", "Original Pokemon ID", "Special Event Ability", "Special Event Ability Description",
                  "Primary Egg Group", "Secondary Egg Group", "Egg Cycle Count", "Health EV", "Attack EV",
                  "Defense EV", "Special Attack EV", "Special Defense EV", "Speed EV", "EV Yield Total",
                  "Evolution Details"], axis=1)

cols_to_check = ["Pokemon Name","Classification", "Alternate Form Name", "Primary Type", "Secondary Type"]
for col in cols_to_check:
    df[col] = df[col].map(lambda x: x.replace('"',''))

df = df.sort_index()
df = df.loc[df["Classification"] == 'Seed Pokemon']
df.reset_index(drop=True,inplace = True)
print(df)

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
