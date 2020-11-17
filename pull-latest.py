from datetime import datetime

html_file_name = 'current.html'
with open(html_file_name, 'w') as html:
  html.write(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
