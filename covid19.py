# Import necessary libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/mac/Desktop/Python/src/datascience/corona/country_wise_latest.csv")
df.head()

df.shape
df.isna().sum()
df.info
df.describe().T

column_names = ["Confirmed", "Deaths", "Recovered", "Active"]

df[column_names].sum().plot(kind="bar")

country_deaths = df[['Country/Region', 'Deaths']]


country_deaths = country_deaths.sort_values(by='Deaths', ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(country_deaths['Country/Region'].head(10), country_deaths['Deaths'].head(10))
plt.xticks(rotation=80)
plt.show()

# Top 10 countries with the highest number of confirmed cases

country_confirmed = df[['Country/Region', 'Deaths']]
country_confirmed = country_confirmed.sort_values(by='Deaths', ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(country_confirmed['Country/Region'].head(10), country_confirmed['Deaths'].head(10))
plt.xticks(rotation=80)
plt.show()

country_recovered = df[['Country/Region', 'Deaths']]


country_recovered = country_recovered.sort_values(by='Deaths', ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(country_recovered['Country/Region'].head(10), country_recovered['Deaths'].head(10))
plt.xticks(rotation=80)
plt.show()

sns.displot(df["1 week change"])
plt.xlim(xmin=6000, xmax=18000)
plt.ylim(ymin=0, ymax=15)

# Import another dataset

df2 = pd.read_csv("/Users/mac/Desktop/Python/src/datascience/corona/full_grouped.csv")
df2.head()
df2.tail()

sorted_df2 = df2.sort_values(by="Deaths")
sorted_df2 = sorted_df2[:15]
plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(sorted_df2["Country/Region"], sorted_df2["Confirmed"], label='Confirmed', color='green')  # Plot total recovered
plt.bar(sorted_df2["Country/Region"], sorted_df2["Active"], label='Active', color='red')  # Plot total deaths
plt.legend()
plt.xlabel('Country')  # X-axis label
plt.ylabel('The number of cases')  # Y-axis label
plt.xlim()
plt.ylim()
plt.title('Comparison of Confirmed and Active cases')
plt.xticks(rotation=45) 
plt.show()


recovered = df2["Recovered"].sum()
death = df2["Deaths"].sum()

data = [recovered, death]
labels = ["Recovered cases", "Deaths"]

plt.pie(data, labels=labels, autopct="%.2f%%")


# Import other dataset

df3 = pd.read_csv('/Users/mac/Desktop/Python/src/datascience/corona/worldometer_data.csv')
df3.head()

ratio = round(df3['TotalDeaths'] / df3["TotalCases"] * 100, 2)
data = {
    "Country": df3["Country/Region"],
    "Death percent": ratio
}

pd.DataFrame(data)

x = df3["Serious,Critical"].sum(), (df3["ActiveCases"] - df3["Serious,Critical"]).sum()
labels = ["Serious/Critical cases", "Not serious cases"]

plt.pie(x, labels=labels, autopct="%2.f%%", shadow=True)

continental_active = df3[["Continent", "ActiveCases"]]
continental_active = df3.groupby("Continent").sum()

continental_active
plt.pie(continental_active["ActiveCases"], labels=continental_active.index, autopct="%.2f%%",
        pctdistance=0.85, explode=[0, 0, 0.35, 0, 0, 0], shadow=True, counterclock=False)


# another data
df4 = pd.read_csv("/Users/mac/Desktop/Python/src/datascience/corona/country_wise_latest.csv")
df4.head()

import pandas as pd
import plotly.express as px


import pandas as pd
import plotly.express as px

# Example data
data = {
    "Country/Region": df4["Country/Region"],
    "NewDeaths": df4["New deaths"]
}
df = pd.DataFrame(data)
world = px.data.gapminder()
merged = world.merge(df, left_on='country', right_on='Country/Region', how='left')
fig = px.choropleth(merged, locations='iso_alpha', color='NewDeaths',
                    color_continuous_scale="RdPu", range_color=(0, df['NewDeaths'].max()),
                    labels={'NewDeaths': 'New Deaths'}, hover_name='country')

fig.update_geos(showcountries=True, countrycolor="darkgrey", showcoastlines=True, coastlinecolor="lightgrey",
                showland=True, landcolor="white", showocean=True, oceancolor="lightblue", showlakes=True,
                lakecolor="lightblue")

fig.update_layout(title_text='New Deaths by Country', title_x=0.5)
fig.show()
