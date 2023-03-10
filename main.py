import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime_spain_df = pd.read_csv("crime_rate_spain.csv")
sorted_crime_df = crime_spain_df.sort_values(["Location", "Year", "Crime"])
df2 = crime_spain_df[["Year", "Crime", "Location", "Total cases"]].groupby(["Year", "Crime"])
df3 = crime_spain_df[["Year", "Crime", "Location", "Total cases"]].groupby("Crime")
df4 = df2[["Total cases"]].sum()
crime = df3["Crime"]


def trend_chart(case):
    year = list(set(crime_spain_df["Year"]))
    total_cases = (df4.iloc[case - 1, 0], df4.iloc[13 + case, 0], df4.iloc[27 + case, 0])
    fig_tend, ax_tend = plt.subplots()
    ax_tend.set_xticks([2019, 2020, 2021])
    ax_tend.set_yticks(total_cases)
    ax_tend.set(xlabel='Years', ylabel='Total Cases', title=sorted_crime_df.iloc[case-1, 2] + ' Crime Trend')
    ax_tend.plot(year, total_cases)
    return plt.show()


def pie_chart(location):
    crime_rate_df = crime_spain_df[["Year", "Location", "Crime", "Total cases"]]
    city_df0 = crime_rate_df[crime_rate_df["Location"] == location]
    city_df01 = city_df0[city_df0["Year"] == user_year]
    labels = city_df01["Crime"]
    crime_nu_of_cases = np.array(city_df01[["Total cases"]])
    selected_crime = crime_nu_of_cases.sum(axis=1)
    fig_pie, ax_ch = plt.subplots()
    ax_ch.pie(selected_crime, radius=1, labels=None, autopct='%1.2f%%')
    ax_ch.legend(labels=labels, prop={'size': 10}, bbox_to_anchor=(1, .5, .07, .06))
    ax_ch.set_title('Crime Distribution per total crime in ' + location + " in " + str(user_year))
    return plt.show()


def crime_count(year, city, crime_no):
    crime_df00 = crime_spain_df.loc[crime_spain_df["Year"] == year]
    crime_df01 = crime_df00.loc[crime_df00["Location"] == city]
    crime_df02 = crime_df01.loc[crime_df01["Crime"] == crime_no]
    count_crime = crime_df02.iloc[0, 3]
    return count_crime


print(" 1-Trend plot", "\n", "2-Pie Chart", "\n", "3-Bar Chart")
reader_plot = int(input("Please select the type of chart you want to plot: "))

if reader_plot == 1:
    i = 0
    for crime in crime:
        if i in range(0, 15):
            print(i+1, "-", sorted_crime_df.iloc[i, 2])
        i = i + 1
    crime_case = int(input("Please select the type of crime you want to plot: "))
    if crime_case <= 14:
        print(trend_chart(crime_case))
    else:
        print("Wrong case number")

elif reader_plot == 2:
    user_selection = input("type a name pf spanish city beginning with capital letter:  ")
    user_year = int(input("Please select a year from (2019 , 2020 or 2021):  "))
    if user_year not in range(2019, 2022):
        print("not available year statistics")
    else:
        print(pie_chart(user_selection))

elif reader_plot == 3:
    i = 0
    for crime in crime:
        if i in range(0, 15):
            print(i+1, "-", sorted_crime_df.iloc[i, 2])
        i = i + 1

    reader_crime_1 = int(input("select first crime in bar plot:  "))
    reader_crime_2 = int(input("select Second crime in bar plot:  "))
    reader_crime_3 = int(input("select third crime in bar plot:  "))

    print("Names of the cities:", "\n", "Madrid", "Barcelona", "Valencia", "Murcia", "\n",
          "Seville", "Zaragoza", "Malaga", "Alicante", "\n", "Cordoba", "Granada", "Rioja", "Salamanca",
          "\n", "Segovia", "Ceuta", "Melilla", "Spain")

    reader_city_1 = input("Type a name of first city in capital letter:  ")
    reader_city_2 = input("Type a name of second city in capital letter:  ")
    reader_city_3 = input("Type a name of third city in capital letter:  ")
    reader_city_4 = input("Type a name of fourth city in capital letter:  ")
    reader_city_5 = input("Type a name of fifth city in capital letter:  ")

    first_crime = sorted_crime_df.iloc[reader_crime_1-1, 2]
    second_crime = sorted_crime_df.iloc[reader_crime_2-1, 2]
    third_crime = sorted_crime_df.iloc[reader_crime_3-1, 2]

    reader_year = int(input("select a year (2019, 2020, 2021):  "))

    city_labels = [reader_city_1, reader_city_2, reader_city_3, reader_city_4, reader_city_5]

    first_crime_count = [crime_count(reader_year, reader_city_1, first_crime),
                         crime_count(reader_year, reader_city_2, first_crime),
                         crime_count(reader_year, reader_city_3, first_crime),
                         crime_count(reader_year, reader_city_4, first_crime),
                         crime_count(reader_year, reader_city_5, first_crime)]

    second_crime_count = [crime_count(reader_year, reader_city_1, second_crime),
                          crime_count(reader_year, reader_city_2, second_crime),
                          crime_count(reader_year, reader_city_3, second_crime),
                          crime_count(reader_year, reader_city_4, second_crime),
                          crime_count(reader_year, reader_city_5, second_crime)]

    third_crime_count = [crime_count(reader_year, reader_city_1, third_crime),
                         crime_count(reader_year, reader_city_2, third_crime),
                         crime_count(reader_year, reader_city_3, third_crime),
                         crime_count(reader_year, reader_city_4, third_crime),
                         crime_count(reader_year, reader_city_5, third_crime)]

    first_crime_count_array = np.array(first_crime_count)
    second_crime_count_array = np.array(second_crime_count)
    aux_crime_count_array = first_crime_count_array + second_crime_count_array
    aux_crime_count_list = aux_crime_count_array.tolist()

    print(" 1-Three Separated column bar chart", "\n", "2-One column bar chart")
    reader_bar_choice = int(input("Please select bar chart type:  "))

    if reader_bar_choice == 1:
        x = np.arange(len(city_labels))
        width = 0.2
        fig, ax = plt.subplots()
        ax.bar(x-width, first_crime_count, width, label=first_crime, color="red")
        ax.bar(x+width, second_crime_count, width, label=second_crime, color="blue")
        ax.bar(x, third_crime_count, width, label=third_crime, color="green")
        ax.set_ylabel('Number of crimes per city')
        ax.set_title('Crimes in Spain in ' + str(reader_year))
        ax.set_xticks(x)
        ax.set_xticklabels(city_labels, rotation='horizontal')
        ax.legend()
        fig.tight_layout()
        plt.show()
    if reader_bar_choice == 2:
        x = np.arange(len(city_labels))
        width = 0.25
        fig, ax = plt.subplots()
        ax.bar(x, first_crime_count, width, label=first_crime, color="red")
        ax.bar(x, second_crime_count, width, label=second_crime, bottom=first_crime_count, color="blue")
        ax.bar(x, third_crime_count, width, label=third_crime, bottom=aux_crime_count_list, color="green")
        ax.set_ylabel('Number of crimes per city')
        ax.set_title('Crimes in Spain in ' + str(reader_year))
        ax.set_xticks(x)
        ax.set_xticklabels(city_labels, rotation='horizontal')
        ax.legend()
        fig.tight_layout()
        plt.show()
