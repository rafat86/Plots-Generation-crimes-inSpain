#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

crime_rate_spain_df = pd.read_csv("crime_rate_Spain.csv")
#print(crime_rate_spain_df)

gbo3 = crime_rate_spain_df.groupby(["Year", "Crime"])
gbo4 = gbo3[["Total cases"]].sum()
print(gbo4)

years = [2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019, 2020 , 2020, 2020 , 2020
         , 2020 , 2020, 2020 , 2020, 2020 , 2020, 2020 , 2020,2021,2021,2021,2021,2021,2021,2021,2021,
         2021,2021,2021,2021,2021,2021,2021,2021]

#years = gbo4["Year"]
#crimes = gbo4["Crime"]
total_cases = gbo4["Total cases"]

plt.plot(years, total_cases, "or")
plt.show()



