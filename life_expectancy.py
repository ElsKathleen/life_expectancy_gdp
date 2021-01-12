# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:14:25 2021

@author: ejans
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

all_data = pd.read_csv('all_data.csv')

#print(all_data.head())
#print(all_data.info())

uniques = all_data.Country.unique()
#print(uniques)

chile = all_data[all_data.Country == 'Chile']
china = all_data[all_data.Country == 'China']
germany = all_data[all_data.Country == 'Germany']
mexico = all_data[all_data.Country == 'Mexico']
usa = all_data[all_data.Country == 'United States of America']
zimbabwe = all_data[all_data.Country == 'Zimbabwe']


x_chile = chile['Year']
y_chile = chile['Life expectancy at birth (years)']

x_china = china['Year']
y_china = china['Life expectancy at birth (years)']

x_germany = germany['Year']
y_germany = germany['Life expectancy at birth (years)']

x_mexico = mexico['Year']
y_mexico = mexico['Life expectancy at birth (years)']

x_usa = usa['Year']
y_usa = usa['Life expectancy at birth (years)']

# Life expectancy of all countries together
x_zimbabwe = zimbabwe['Year']
y_zimbabwe = zimbabwe['Life expectancy at birth (years)']
plt.figure(figsize=(10,8))
plt.plot(x_chile, y_chile, color='blue')
plt.plot(x_china, y_china, color='orange')
plt.plot(x_germany, y_germany, color='black')
plt.plot(x_mexico, y_mexico, color='green')
plt.plot(x_usa, y_usa, color='red')
plt.plot(x_zimbabwe, y_zimbabwe, color='yellow')
plt.xlabel('Years')
plt.ylabel('Life expectancy at birth')
plt.title('Life expectancy different countries')
plt.legend(['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe'], loc=4)
plt.show()
plt.savefig('life_exp_all_countries.png')



gdp_chile = chile['GDP']
gdp_china = china['GDP']
gdp_germany = germany['GDP']
gdp_mexico = mexico['GDP']
gdp_usa = usa['GDP']
gdp_zimbabwe = zimbabwe['GDP']

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

chile_x = create_x(2, 0.8, 1, 16)
zimbabwe_x = create_x(2, 0.8, 2, 16)

# Difference in life expectancy between two countries
plt.figure(figsize=(10,8))
ax=plt.subplot()
plt.bar(chile_x, y_chile)
plt.bar(zimbabwe_x, y_zimbabwe)
middle_x = [(a + b) / 2.0 for a, b in zip(chile_x, zimbabwe_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(x_chile)
plt.legend(['Chile', 'Zimbabwe'])
plt.title('Difference in life expectancy between Chile and Zimbabwe')
plt.xlabel('Year')
plt.ylabel('Age')
plt.show()
plt.savefig('difference_life_exp_2_countries.png')


# Difference in GDP between 2 countries
plt.figure(figsize=(10,8))
ax=plt.subplot()
plt.bar(chile_x, gdp_chile)
plt.bar(zimbabwe_x, gdp_zimbabwe)
middle_x = [(a + b) / 2.0 for a, b in zip(chile_x, zimbabwe_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(x_chile)
plt.legend(['Chile', 'Zimbabwe'])
plt.title('Difference in GDP between Chile and Zimbabwe')
plt.xlabel('Year')
plt.ylabel('GDP x 10.000.000.000.000')
plt.show()
plt.savefig('difference_gdp_2_countries.png')


# GDP in China
plt.figure(figsize=(10,8))
plt.bar(x_china, gdp_china, width=0.4)
ax = plt.subplot()
ax.set_xticks(x_china)
ax.set_xticklabels(x_china, rotation=40)
plt.ylabel('GDP x 10.000.000.000.000')
plt.xlabel('Year')
plt.title('GDP China over time')
plt.show()
plt.savefig('gdp_china_over_time.png')





