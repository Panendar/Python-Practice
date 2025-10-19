from statistics import mean
import pandas as pd
# import os
# import kaggle
# from kaggle.api.kaggle_api_extended import KaggleApi

# pd.options.display.max_rows = 15
# print(pd.options.display.max_rows) 

# api = KaggleApi()
# api.authenticate()

# dataset = api.dataset_list(search ="Pokemon")

# top_downloaded = sorted(dataset, key = lambda x: x.download_count, reverse = True)[0]
# print(f"{top_downloaded.id} --> {top_downloaded.title} --> {top_downloaded.total_bytes} --> {top_downloaded.download_count}")
# print(f"\n The dataset of the {top_downloaded.title} is downloading...........")
# api.dataset_download_files(top_downloaded.ref, path =os.getcwd(), unzip = True)

# # pandas operations

# # pandas read csv
data = pd.read_csv("Pokemon.csv", index_col = "Name")
# print(data.to_string())
# print(data.head(5))


# Displaying the information about a specific pokemon
# print(data.info())
# pokemon = input("Enter the name of the pokemon: ").capitalize()
# try:
#     print(data.loc[pokemon])
# except KeyError as e:
#     print(f"{pokemon} not found in the data")

# printing the specific attributes of a pokemon
# print(data.loc["Pikachu", ["Type 1", "Type 2", "HP", "Attack"]].to_string())

# filtering the pokemons based on a  attribute condition

# legendary = data[data["Legendary"] == True]
# # print(legendary.to_string())
# print(legendary.shape)
# fire_fly = data[(data["Type 1"].isin(["Fire", "Flying"])) & (data["Type 2"].isin(["Fire", "Flying"]))]
# print(fire_fly.to_string())
# powerful_pokemon = data[data["Attack"]>150]
# print(data.loc[powerful_pokemon.index, ["Type 1", "Type 2", "Attack"]].to_string())

# min_attack = min(data["Attack"])
# print(data[data["Attack"] == min_attack])
# print(data.loc[data["Attack"] == min_attack, ["HP", "Attack", "Defense"]])


# AGGREGATE FUNCTIONS
# finding the mean, median, mode for the only attributes which are numerical only
# print(data.mean(numeric_only=True))
# print(data.median(numeric_only=True))
# print(data.mode(numeric_only=True).to_string())
# print(mean(data["Attack"]), mean(data["Defense"]), mean(data["HP"]))  # since attack have the value of nan it will give the mean as nan as the output
# print(sum(data["Legendary"] == True))
# print(data.min(numeric_only=True))
# print(data["Type 2"].count())

# group = data.groupby("Type 1")
# print(group["Attack"].mean().round(2))
# print(group["Defense"].min().round(2))

# CLEANING THE DATA
# data = data.drop(columns = ["#"])
# df = data.dropna()        # dropping with specific attributes,  subset = ["Type 1", "Attack"]
# for col in data.columns:
#     if not data[col].equals(df[col]):
#         print(f"Column {col} has been changed")

# replacing the NAN values with the None of that column for Type 2
# df = data.fillna({"Type 2": "None"})
# print(df[df["Type 2"] == "None"])

# FIX INCONSISTENT DATA
# data["Type 2"] = data["Type 2"].replace({"Fire" : "Flame"})
# print(data[data["Type 2"] == "Flame"])

# STANDARDIZE THE DATA
# data["Legendary"] = data["Legendary"].astype(str).str.upper()
# print((data["Legendary"] == "TRUE").value_counts())

# FIX DATA TYPES
# data["Legendary"] = data["Legendary"].astype(int)
# print(data["Legendary"].value_counts())

# REMOVE DUPLICATES
# df = data.drop_duplicates()
# print(df.shape, data.shape)

# Return a new Data Frame with no empty cells: using dropna()

# no_empty = data.dropna()
# print(no_empty.head(5))
# print(data.shape, no_empty.shape)
# print("================================")

# print(data.info())
# print(data.head(5))

#replacing the empty cells with the mean of that column: using fillna()
# attack_mean = int(data["Attack"].mean())
# print(attack_mean)
# missing_attack_rows = data[data["Attack"].isnull()]
# print(missing_attack_rows)
# data.fillna({"Attack": attack_mean}, inplace = True)
# print(data.head(5))