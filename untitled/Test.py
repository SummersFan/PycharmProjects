import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import string
import matplotlib.pyplot as plt

df_news = pd.read_table('ex1data1.txt',header=None)

df = df_news[0].head()
x1 = []
y1 = []
for i in df:
    x1.append(i.split(',')[0])
    y1.append(i.split(',')[1])

plt.figure(1)
plt.subplot(211)

plt.ylim(-1, 10,1)
plt.plot(x1,y1,'rx', 'MarkerSize', 10)
plt.show()


