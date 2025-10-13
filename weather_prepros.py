#!/usr/bin/env python3

import pandas
import numpy
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

weather = pandas.read_csv("/Users/anay/Desktop/RoboManipal/Data_Preprocessing/weatherAUS.csv")

weather["date_obj"] = pandas.to_datetime(weather["Date"], errors = "coerce")
weather["Day"] = weather["date_obj"].dt.day
weather["Month"] = weather["date_obj"].dt.month
weather["Year"] = weather["date_obj"].dt.year
weather.drop(columns= ["Date", "date_obj"])

excluded_columns = ["date_obj"]
weather_dateless = pandas.get_dummies(weather, columns=filter(lambda x: x not in excluded_columns, weather.columns))

#weather = pandas.get_dummies(weather, drop_first=True)
weather[weather.select_dtypes(include=['bool']).columns] = weather[weather.select_dtypes(include=['bool']).columns].astype(int)

weather = weather.fillna(weather.mean(numeric_only=True))
        
print(weather.dtypes)

non_numeric = weather.select_dtypes(exclude=['number']).columns
print("Non-numeric columns:", non_numeric)

#weather_scaled = StandardScaler().fit_transform(weather)
#weather = pandas.DataFrame(weather_scaled, columns=weather.columns, index=weather.index)

print("Shape:", weather.shape)
print("Columns:", len(weather.columns))
print("Example columns:", list(weather.columns[:50]))

#weather.to_csv("/Users/anay/Desktop/RoboManipal/Data_Preprocessing/weather_preprosd.csv", index=False)