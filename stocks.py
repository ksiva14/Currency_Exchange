import requests
import json
import pandas as pd
import csv
import matplotlib.pyplot as plt

print("Here is the Country Code List\n\n")

count = 0
with open("physical_currency_list.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if count != 0:
            spaces = "      "
        else:
            spaces = " "
        print(spaces.join(row))
        count += 1

print()

country_one = input("Enter First Country Code From List Above: ")

print()

country_two = input("Enter Second Country Code From List Above: ")

print()

apikey = '432Y4FERICA71E7O'

url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={country_one.upper().strip()}&to_symbol={country_two.upper().strip()}&apikey={apikey}'
r = requests.get(url)
data = r.json()

data_json = json.dumps(data, indent=4)
print(data_json)

time_series = 'Time Series FX (Daily)'
open_value = '1. open'
prices = []
dates = []
days = 0
for date in data[time_series].keys():
    if days > 15:
        break
    dates.insert(0, date)
    prices.insert(0, float(data[time_series][date][open_value]))
    days += 1


plt.plot(dates,prices)
plt.title(f'Currency Exchange Prices Across Days From {country_one} to {country_two}')
plt.xlabel('Date')
plt.ylabel('Currency Value')
plt.show()

