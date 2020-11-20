import requests
import os
import pandas as pd
from datetime import datetime

HISTORY_CSV_FILE = 'covid-tracking-project.csv'

r = requests.get("https://covidtracking.com/data/download/national-history.csv")
with open(HISTORY_CSV_FILE, 'w') as f:
  f.write(r.text)

df = pd.read_csv("covid-tracking-project.csv", index_col="date")
df = df.sort_index(ascending=True)

df.rename(columns={'positiveIncrease': 'dailycases'}, inplace=True)


df['7ma'] = df["dailycases"].rolling(window=7).mean()
df['7ma'] = df["7ma"].apply(lambda x: 0 if pd.isnull(x) else int(x))

print(df[['dailycases', '7ma']].tail(20))

df[['dailycases', '7ma']].tail(20).to_csv('latest.csv')

os.remove(HISTORY_CSV_FILE)

html_file_name = 'current.html'
with open(html_file_name, 'w') as html:
  html.write(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
