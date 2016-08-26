import numpy as np
import matplotlib.pyplot as plt

time, Qin, Pin = np.loadtxt('/home/cmerl/Desktop/AllData.txt', usecols=(0, 5, 6), unpack=True)
	    
fig, ax1 = plt.subplots()
ax1.plot(time, Pin)
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Pressure')

ax2 = ax1.twinx()
ax2.plot(time, Qin)
ax2.set_ylabel('Flow')

plt.show()
