from urllib.request import urlopen
import csv

data = [['Name']]
unwanted = []

url = 'file:///C:/Users/Ishant/Desktop/Python/Imp/local.html'
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find('<main class="main content-page" role="main">') + len('<main class="main content-page" role="main">')
end_index = html.find("</main>")
title = html[start_index:end_index]
contents = title.replace(">","<").split("<")

for x in contents:
  if 'Health' in x:
    data.append([x])
  elif 'Center' in x:
    data.append([x])
  elif 'Service' in x:
    data.append([x])
  elif 'Hospital' in x:
    data.append([x])
    
i = 0

for x in contents:
  if 'Health' in x and i < 14:
    unwanted.append([x])
    i += 1
  elif 'Center' in x and i < 14:
    unwanted.append([x])
    i += 1
  elif 'Service' in x and i < 14:
    unwanted.append([x])
    i += 1
  elif 'Hospital' in x and i < 14:
    unwanted.append([x])
    i += 1
    
for x in unwanted:
  data.remove(x)

with open('healthcenters.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)