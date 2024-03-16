import matplotlib.pyplot as plt
# Sample student scores
scores = [10, 15, 20, 25, 85, 60, 90, 75, 95]
# Creating a histogram
plt.hist(scores, bins=2, color='lightblue', edgecolor='black')
# Adding labels and title
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.title('Student Scores Histogram')
# Displaying the plot
plt.show()
