import numpy as np
import pandas as pd
import matplotlib as plt

crime_rate_spain_df = pd.read_csv("crime_rate_Spain.csv")
#print(crime_rate_spain_df)

df = crime_rate_spain_df[["Location", "Crime"]]
#df2 = df[df["Year"] == "96960"]
#print(df2)


df3 = df[df["Location"] == "Barcelona"]
print(df3)

df4 = df[df["Crime"] == "Theft"]
print(df4)

gb_year = crime_rate_spain_df.groupby("Location")
print(gb_year.mean())
