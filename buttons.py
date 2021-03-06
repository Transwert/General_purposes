"""
Constructing a simple button GUI to modify a straight laser's path

The `up` and `down` button widget helps visualize the laser, i.e. moving the laser to required position 
using Electro-magnetic coil
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import Button

Lspot_displ = np.array([-4, -3, -2, -1, 0, 1, 2, 3, 4])

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
plt.xlim(0.0, 1.0)
plt.ylim(-4.0, 4.0)
t = np.arange(0.0, 1.0, 0.001)

coil_l = np.arange(0, 0.2, 0.1)
coil_up = [0.5 for item in coil_l]
coil_down = [-0.5 for item in coil_l]
# print(coil_l,coil_up,coil_down)
plt.plot(coil_l, coil_up, lw=2, label = 'Electromagnetic Coil', color = "red")
plt.plot(coil_l, coil_down, lw=2, color = "red")

Rectangle((0,0.1),0.75,0.2,angle = 0.0,fill = True)

s = Lspot_displ[4] * t
l, = plt.plot(t, s, linestyle= ':', lw=4, label = 'laser being emitted')
plt.title('Laser_simulation')
plt.legend()

class Index(object):
    ind = 4

    def up(self, event):
        self.ind += 1
        i = self.ind % len(Lspot_displ)
        ydata = Lspot_displ[i] * t
        l.set_ydata(ydata)
        plt.plot(coil_l, coil_up, lw=2)
        plt.plot(coil_l, coil_down, lw=2)
        plt.draw()
        

    def down(self, event):
        self.ind -= 1
        i = self.ind % len(Lspot_displ)
        ydata = Lspot_displ[i] * t
        l.set_ydata(ydata)
        plt.plot(coil_l, coil_up, lw=2)
        plt.plot(coil_l, coil_down, lw=2)
        plt.draw()

# Below part for buttons:
callback = Index()

axdown = plt.axes([0.7, 0.05, 0.1, 0.075])

axup = plt.axes([0.81, 0.05, 0.1, 0.075])

bup = Button(axup, 'up')
bup.on_clicked(callback.up)

bdown = Button(axdown, 'down')
bdown.on_clicked(callback.down)

plt.show()
