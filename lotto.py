import random
import numpy
import matplotlib.pyplot as plt


def lotto():
    zahlen = list(range(1,46))
    gezogen = random.sample(zahlen, 6)
    return gezogen;

def histogram(n = 10000):
    histogram = [0] * 45
    for i in range(0,n):
        for gezogen in lotto():
            histogram[gezogen -1 ] += 1

    return histogram

def test():
    assert 30 < numpy.std(histogram()) < 40

histogramm = histogram(20000)
plt.plot(histogramm)
plt.grid(True)
plt.ylim(0, max(histogramm)* 1.2)
plt.show()
