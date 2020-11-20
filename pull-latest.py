import requests
from datetime import datetime

print('requesting new csv file')
r = requests.get("https://covidtracking.com/data/download/national-history.csv")
with open('covid-tracking-project.csv', 'w') as f:
  f.write(r.text)

html_file_name = 'current.html'
with open(html_file_name, 'w') as html:
  html.write(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
