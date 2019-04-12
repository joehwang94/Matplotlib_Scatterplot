#Please install numpy and matplotlib onto your drive if you haven't done so already. This will not run without it.
#To install them, type in "pip install numpy", wait for the installation to complete, then type in "pip install matplotlib" (without the quotes) in your command prompt before running this script.


import numpy as np
import matplotlib.pyplot as plt

plt.title ('Random Dispersion in Size vs. Frequency')

plt.xlabel('Size')
plt.ylabel('Frequency')

info = {'a': np.arange(75),
        'c': np.random.randint(75, 150, 75),
        'd': np.random.randn(75)}
info['b'] = info['a'] + 100 * np.random.randn(75)
info['d'] = np.abs(info['d']) * 100

plt.scatter(x = 'a', y = 'b', s='d', c='c', data=info)

plt.grid(True)

plt.show()
