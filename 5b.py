import matplotlib.pyplot as plt
# Data to be visualized in the pie chart
slice_labels = ['Academic Studies', 'Skill Development', 'Networking', 
'Projects','PersonalityDevelopment']
time_allocation = [35, 30, 5, 20,10] 
# Values representing the percentage of time for each category
# Colors for each category slice
slice_colors = ['gold', 'orchid', 'yellow','green','royalblue']
# Exploding the slices with the highest time allocation 
explode_values= (0.1,0.1, 0.0, 0,0)
# Creating the pie chart
plt.pie(time_allocation, explode=explode_values, labels=slice_labels, 
colors=slice_colors, autopct='%1.1f%%', startangle=45)
# Aspect ratio ensures that the pie chart is a circle, not an ellipse
plt.axis('equal')
# Title for the pie chart
plt.title('Recommended Time Allocation for Academic and Career Preparation')
# Displaying the pie chart
plt.show()
