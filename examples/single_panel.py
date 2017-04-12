'''
Example using improve_maplot for a single panel plot.
'''
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from improve_matplot.panel import Panel
from improve_matplot import plot

# generate some dummy data
minx, maxx = 0., 1.
miny, maxy = 0., 1.
numx, numy = 25, 25

x1d = np.linspace(minx, maxx, numx)
y1d = np.linspace(miny, maxy, numy)
x2d, y2d = np.meshgrid(x1d, y1d, indexing='ij')
z2d = np.sin(x2d*np.pi)*np.cos(y2d*np.pi)

# set font
plot.adjust_fonts(mpl)

# create plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.pcolormesh(x2d, y2d, z2d, cmap='gist_rainbow')
cb = plt.colorbar()

# create panel object
panel = Panel(fig, ax, plt, cb)
panel.set_xbounds([minx, maxx])
panel.set_ybounds([miny, maxy])
#panel.set_txscale(30.)
#panel.set_lbscale(45.)
panel.beautify_axis('Panel title', 'X', 'Y')
panel.beautify_colorbar('Colorbar label')
panel.make_ticks()

# save plot as image
plt.savefig('single_panel.png')
