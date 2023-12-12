# LAB 12-1
import csv
import urllib
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/dongupak/DataSciPy/master/data/csv/weather.csv'
response = urllib.request.urlopen(url)
lines = [l.decode('cp949') for l in response.readlines()]
data = csv.reader(lines)
header = next(data)

monthly_wind = [ 0 for x in range(12) ]
days_counted = [ 0 for x in range(12) ]

for row in data:
    month = int(row[0][5:7])
    if row[3] !=  '' :
        wind = float(row[3])
        monthly_wind[month-1] += wind
        days_counted[month-1] += 1

for i in range(12) :
      monthly_wind[i] /= days_counted[i]

plt.plot(monthly_wind, 'blue')
plt.show()

f.close()
