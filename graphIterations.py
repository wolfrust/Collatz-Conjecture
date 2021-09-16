import matplotlib.pyplot as plt
from ast import literal_eval
from sys import argv

iterations = literal_eval(open(argv[1], 'r').read())

plt.bar(range(len(iterations)), list(iterations.values()), align='center')
plt.xticks(range(len(iterations)), list(iterations.keys()))

plt.show()
