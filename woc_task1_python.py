# Task 1
import numpy as np
import matplotlib.pyplot as plot

x = np.arange(0,10,0.01)
y = np.cos(x);

plot.plot(x,y)
plot.xlabel('time')
plot.ylabel('amplitude')
plot.grid(True)
