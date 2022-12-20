import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

crime_rate_spain_df = pd.read_csv("crime_rate_Spain.csv")
#print(crime_rate_spain_df)

''''
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
'''
'''
labels = crime_rate_spain_df["Location"]
Crimes_count = crime_rate_spain_df["Total cases"]

x = np.arange(len(labels))
width = 0.25
fig, ax = plt.subplots()
ax.bar(x-width/2, male_count, width, label='Male', color = "red")
ax.bar(x+width/2, female_count, width, label='Female', color = "blue")
ax.set_ylabel('PPU Students')
ax.set_title('Students per College')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()
fig.tight_layout()
plt.show()
'''

crime_rate_df = crime_rate_spain_df[["Year", "Location", "Crime", "Total cases"]]
city_df0 = crime_rate_df[crime_rate_df["Location"] == "Barcelona"]
city_df01 = city_df0[city_df0["Year"] == 2020]
#city_df = city_df01.iloc[0:6:1]

labels = city_df01["Crime"]
crime_nu_of_cases = np.array(city_df01[["Total cases"]])

aggregated_student_count = crime_nu_of_cases.sum(axis=1)
flattened_student_count = crime_nu_of_cases.flatten()

fig, ax = plt.subplots()
ax.pie(aggregated_student_count, radius=1, labels=labels)
#ax.legend(loc='best')
ax.set_title('Crime Distribution per total crime in the city')
plt.show()
