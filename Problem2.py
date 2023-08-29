import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

np.random.seed(23685752)
N_points = 10000
n_bins = 20

# Creating distribution
x = np.random.randn(N_points)
y = .8 ** x + np.random.randn(10000) + 25*x

# 1. Creating histogram
fig, axs = plt.subplots(1, 1, figsize =(10, 7),tight_layout = True)
axs.hist(x, bins = n_bins)
plt.show()

# Improving the histogram for better visualization
legend = ['distribution']
fig, axs = plt.subplots(1, 1,figsize =(10, 7), tight_layout = True)
# Remove axes spines
for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)

# Remove x, y ticks
axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')
   
# Add padding between axes and labels
axs.xaxis.set_tick_params(pad = 5)
axs.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
axs.grid(which = 'both', visible=True, color ='grey', linestyle ='-.', linewidth = 0.5,  alpha = 0.6)
 
# Add Text watermark
fig.text(0.9, 0.15, 'KD',
         fontsize = 12,
         color ='red',
         ha ='right',
         va ='bottom',
         alpha = 0.7)
 
# 2. Better histogram 
# Creating histogram
N, bins, patches = axs.hist(x, bins = n_bins)
 
# Setting color
fracs = ((N**(1 / 5)) / N.max())
# print(fracs)
norm = colors.Normalize(fracs.min(), fracs.max())
 
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
 
# Adding extra features   
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend(legend)
plt.title('Customized histogram')
 
# Show plot
plt.show()
