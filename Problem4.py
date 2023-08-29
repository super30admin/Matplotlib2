import matplotlib.pyplot as plt
import numpy as np

labels = 'Mats', 'Bats', 'Rats', 'Cats', 'Hats', 'Pats', 'Kats', 'Lats', 'Sats', 'Tats'
sizes = [10,10,20,20,5,5,5,5,10,10]

# 1. Basic Pie Chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
plt.show()


# 2. Exploring options of pie chart

# Exploding the Rats out of the pie chart
explodes = [ 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0]

# Creating color parameters
colors = ( "orange", "cyan", "brown", "grey", "indigo", "beige", "yellow", "green", "blue", "violet")

# Wedge properties
wp = { 'linewidth' : 1, 'edgecolor' : "yellow" }

# Creating autocpt arguments

def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)

# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(sizes,
                                  autopct = lambda pct: func(pct, sizes),
                                  explode = explodes,
                                  labels = labels,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 45,
                                  wedgeprops = wp,
                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, labels, title ="Random", loc ="center left", bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Customizing pie chart")
 
# show plot
plt.show()

# 3. Creating a nested pie chart
# Creating dataset
size = 6
cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']

data = np.array([[1, 50], [17, 23],
				[35, 11], [29, 33],
				[12, 27], [41, 42]])

# normalizing data to 2 pi
norm = data / np.sum(data)*2 * np.pi
print(norm)
# obtaining ordinates of bar edges
left = np.cumsum(np.append(0, norm.flatten()[:-1])).reshape(data.shape)

# Creating color scale
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(6)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9,
							10, 12, 13, 15,
							17, 18, 20 ]))

# Creating plot
fig, ax = plt.subplots(figsize =(10, 7),
					subplot_kw = dict(polar = True))

ax.bar(x = left[:, 0],
	width = norm.sum(axis = 1),
	bottom = 1-size,
	height = size,
	color = outer_colors,
	edgecolor ='w',
	linewidth = 1,
	align ="edge")

ax.bar(x = left.flatten(),
	width = norm.flatten(),
	bottom = 1-2 * size,
	height = size,
	color = inner_colors,
	edgecolor ='w',
	linewidth = 1,
	align ="edge")

ax.set(title ="Nested pie chart")
ax.set_axis_off()

# show plot
plt.show()

