def number_of_pokemon(df1, region1):
    return df1.loc[df1["Region of Origin"] == region1].count()[0]


def most_common_pokemon(df1):
    df1["count"] = 1
    df2 = df1.groupby(["Primary Type"]).count()["count"].copy()
    df2 = df2.sort_values(ascending=False)
    return df2[0:1].to_string().replace("Primary Type", " "), \
        df2[1:2].to_string().replace("Primary Type", " "), \
        df2[2:3].to_string().replace("Primary Type", " ")


def least_common_pokemon(df1):
    df1["count"] = 1
    df2 = df1.groupby(["Primary Type"]).count()["count"].copy()
    df2 = df2.sort_values(ascending=True)
    return df2[0:1].to_string().replace("Primary Type", " "), \
        df2[1:2].to_string().replace("Primary Type", " "), \
        df2[2:3].to_string().replace("Primary Type", " ")


def worst_pokemon(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1.sort_values(by="Base Stat Total", inplace=True)
    df1 = df1.rename(columns={"Primary Type": "Type"})
    df1 = df1.rename(columns={"Base Stat Total": "Combat Power"})
    df2 = df1[["Pokemon Name", "Type", "Combat Power"]]
    df2 = df2.iloc[0:4, 0:3]
    return df2


def best_pokemon(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1.sort_values(by="Base Stat Total", inplace=True, ascending=False)
    df1 = df1.rename(columns={"Primary Type": "Type"})
    df1 = df1.rename(columns={"Base Stat Total": "Combat Power"})
    df2 = df1[["Pokemon Name", "Type", "Combat Power"]]
    df2 = df2.iloc[0:4, 0:3]
    return df2


def legendary_pokemon(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    df1 = df1.loc[df1["Legendary Type"] != "nan"]
    df1 = df1[["Pokemon Name", "Legendary Type"]]
    return df1


def total_number_of_legendary_pokemon(df1):
    return df1.loc[df1["Legendary Type"] != "nan"].count()[0]


def number_of_legendary_pokemon(df1, region1):
    df1 = df1.loc[df1["Region of Origin"] == region1]
    return df1.loc[df1["Legendary Type"] != "nan"].count()[0]


def legendary_evolved(df1):
    return df1.loc[(df1["Legendary Type"] != "nan") & (df1["Pre-Evolution Pokemon Id"] != "nan")].count()[0]
