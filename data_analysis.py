import pandas as pd

# Read the CSV file
data = pd.read_csv("students.csv")

# Display the data
print("Student Data:")
print(data)

# Total number of students
print("\nTotal Students:", len(data))

# Average marks
print("Average Marks:", data["Marks"].mean())

# Highest marks
print("Highest Marks:", data["Marks"].max())

# Lowest marks
print("Lowest Marks:", data["Marks"].min())

# Students scoring above 80
print("\nStudents Scoring Above 80:")
print(data[data["Marks"] > 80])