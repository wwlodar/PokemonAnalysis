from collections import Counter
import pandas as pd
from heapq import nlargest

def number_of_pokemon(df1, region1):
    return(df1.loc[df1["Region of Origin"] == region1].count()[0])

def biggest_pokemon_group(df1,region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    dict_pokemon = df1["Primary Type"].value_counts().to_dict()
    three_largest = nlargest(3, dict_pokemon.items(), key=lambda x: x[1])
    return list(three_largest)

def best_pokemon(df1,region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    maxClm = df1.max().["Base Stat Total"]
    print(maxClm)



