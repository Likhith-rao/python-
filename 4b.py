# Import the necessary library (Matplotlib.pyplot) for data visualization.
import matplotlib.pyplot as plt
# Sample student data - study hours and exam scores.
study_hours = [2, 4, 5, 6, 8, 10]
exam_scores = [60, 65, 75, 80, 90, 95]
# Create a scatter plot using the 'plot' function from Matplotlib.
plt.scatter(study_hours, exam_scores, color='blue', marker='o', 
label='Students')
# Customize the plot with labels and a title.
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.title('Scatter Plot of Study Hours vs Exam Scores')
# Add a legend to identify the data points.
plt.legend()
# Display the scatter plot.
plt.show()
