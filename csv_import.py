import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from pprint import pprint

with open(os.path.dirname(os.path.realpath(__file__)) + '\\Datenimport.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=';'))

years = data[1][1:]

prices = dict()
average = {}
for row in data[2:]:
    prices[str(row[0]).strip(' ')] = list(float(p.replace(',', '.')) for p in row[1:])
    average[str(row[0]).strip(' ')] = np.mean(prices[str(row[0]).strip(' ')])

#colormap = plt.cm.gist_ncar
#plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, len(prices))])


for price in prices:
#    print (years)
#    print(price)
    plt.plot(years, prices[price], '--', label=price)
#    break

leg = plt.legend(loc="upper right", bbox_to_anchor=(1.7, 1.0))
plt.draw()
#bb = leg.get_bbox_to_anchor().inverse_transformed(plt)
#print(bb)
plt.show()

# pprint(average)




