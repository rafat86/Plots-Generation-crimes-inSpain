import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime_spain_df = pd.read_csv("crime_rate_spain.csv")

df2 = crime_spain_df[["Year", "Crime", "Location", "Total cases"]].groupby(["Year", "Crime"])
df3 = crime_spain_df[["Year", "Crime", "Location", "Total cases"]].groupby("Crime")
df4 = df2[["Total cases"]].sum()
crime = df3["Crime"]


def trend_chart(crime_case):
    year = list(set(crime_spain_df["Year"]))
    total_cases = (df4.iloc[crime_case-1, 0], df4.iloc[13 + crime_case, 0], df4.iloc[27 + crime_case, 0])
    plt.plot(year, total_cases)
    plt.xlabel('Years')
    plt.ylabel('Total cases')
    plt.title(crime_spain_df.iloc[i, 2])
    return plt.show()


print(" 1-Tender plot", "\n", "2-Pie Chart", "\n", "3-Bar Chart")
reader_plot = int(input("Please select the type of chart you want to plot: "))

if reader_plot == 1:
    i = 0
    for crime in crime:
        if i in range(0, 15):
            print(i+1, "-", crime_spain_df.iloc[i, 2])
        i = i + 1
    crime_case = int(input("Please select the type of crime you want to plot: "))
    if crime_case <= 14:
        print(trend_chart(crime_case))
    else:
        print("Wrong case number")

elif reader_plot == 2:
    print("plot 2")
elif reader_plot == 3:
    print("plot 3")
else:
    reader_plot = int(input("Please select the type of chart you want to plot: "))





crime_rate_df = crime_spain_df[["Year", "Location", "Crime", "Total cases"]]
city_df0 = crime_rate_df[crime_rate_df["Location"] == "Barcelona"]
city_df01 = city_df0[city_df0["Year"] == 2020]

labels = city_df01["Crime"]
crime_nu_of_cases = np.array(city_df01[["Total cases"]])

aggregated_student_count = crime_nu_of_cases.sum(axis=1)
flattened_student_count = crime_nu_of_cases.flatten()

fig, ax = plt.subplots()
ax.pie(aggregated_student_count, radius=1, labels=labels)
ax.legend(loc='best')
ax.set_title('Crime Distribution per total crime in the city')
plt.show()
