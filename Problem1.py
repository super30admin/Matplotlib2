import matplotlib.pyplot as plt
import numpy as np

# 1. Simple Line Plot
x = np.array([1, 2, 3, 4]) 
y = x*2 
x1 = [1, 3, 2, 9]
y1 = [3, 5, 7, 9]

plt.plot(x, y) 
plt.show() 

# 2. Adding the x,y labels and title
plt.plot(x, y)
plt.xlabel("X-axis")  
plt.ylabel("Y-axis")  
plt.title("Simple Line Plot")  
plt.show()

# 3. Multiple charts in one figure
plt.plot(x, y)
plt.xlabel("X-axis")  
plt.ylabel("Y-axis")  
plt.title("Simple Line Plot")  
plt.show()
  
# figure() function helps in creating a new figure that can hold a new chart in it.
plt.figure()
plt.plot(x1, y1, '-*')
  
# Show another chart with '-' dotted line
plt.show()

# 4. Multiple plots on same axis
plt.plot(x, y)
plt.plot(x1, y1, '-.')
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.show()

# 5. Fill area between two plots
plt.plot(x, y)
plt.plot(x, y1, '-.')
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.fill_between(x, y, y1, color='red', alpha=0.9)
plt.show()