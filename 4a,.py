# Importing the Matplotlib library with the alias plt
import matplotlib.pyplot as plt
# Defining the subjects and corresponding scores
subjects = ['Math', 'CO', 'OS', 'DS']
scores = [55, 75, 58, 88]
# Creating a bar plot using plt.bar() with customization options
plt.bar(subjects, scores, color='green', width=0.5, edgecolor='black', 
linewidth=1.2, label='Student Scores')
# Adding labels to the x and y axes
plt.xlabel('Subjects')
plt.ylabel('Scores')
# Adding a title to the plot
plt.title('Student Performance in Different Subjects')
# Adding a legend to the plot, and placing it at the best location
plt.legend(loc='best')
# Displaying the plot
plt.show()
