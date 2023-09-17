#Problem 1
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = x*2
  
plt.plot(x, y,'-.')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Dixita's First Line chart")
plt.show()

#Problem 2
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2500000)
N_points = 10000
n_bins = 20

x = np.random.randn(N_points)
y = .8 ** x + np.random.randn(10000) + 25
legend = ['distribution']

fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)

for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)
axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')
axs.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.6)
N, bins, patches = axs.hist(x, bins = n_bins)

plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend(legend)
plt.title('Customized histogram')

plt.show()

#Problem 3 
import matplotlib.pyplot as plt
import numpy as np

x1 = [10,20,30,40,50]
 
y1 = [15,25,35,45,55]
 
# dataset2
x2 = [1,2,3,4,5]
 
y2 = [1,4,9,16,25]
 
plt.scatter(x1, y1, c ="pink",
            linewidths = 2,
            marker ="s",
            edgecolor ="green",
            s = 50)
 
plt.scatter(x2, y2, c ="yellow",
            linewidths = 2,
            marker ="^",
            edgecolor ="red",
            s = 200)
 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

#Problem 4 
import matplotlib.pyplot as plt
import numpy as np

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR']
 
data = [7,10,23,20,40]

explode = (0.1, 0.1, 0.2, 0.3, 0.0)

colors = ( "orange", "cyan", "brown",
          "grey", "indigo")

wp = { 'linewidth' : 1, 'edgecolor' : "green" }

def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)

fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  explode = explode,
                                  labels = cars,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="magenta"))

ax.legend(wedges, cars,
          title ="Cars",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Customizing pie chart")

plt.show()
