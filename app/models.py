from collections import Counter
import pandas as pd
from heapq import nlargest


def number_of_pokemon(df1, region1):
    return(df1.loc[df1["Region of Origin"] == region1].count()[0])

def biggest_pokemon_group(df1,region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    dict_pokemon = df1["Primary Type"].value_counts().to_dict()
    three_largest = nlargest(1, dict_pokemon.items(), key=lambda x: x[1])
    return list(three_largest)

def worst_pokemon(df1,region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1.sort_values(by="Base Stat Total", inplace=True)
    df1 = df1.rename(columns={"Primary Type": "Type"})
    df1 = df1.rename(columns={"Base Stat Total":"Combat Power"})
    df2= df1[["Pokemon Name", "Type", "Combat Power"]]
    df2 = df2.iloc[0:4, 0:3]
    return df2

def best_pokemon(df1,region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1.sort_values(by="Base Stat Total", inplace=True, ascending=False)
    df1 = df1.rename(columns={"Primary Type": "Type"})
    df1 = df1.rename(columns={"Base Stat Total":"Combat Power"})
    df2= df1[["Pokemon Name", "Type", "Combat Power"]]
    df2 = df2.iloc[0:4, 0:3]
    return df2