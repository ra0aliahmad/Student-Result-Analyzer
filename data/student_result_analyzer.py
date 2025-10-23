# Student Result Analyzer
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("data/marks.csv")

# Calculate total and average
df["Total"] = df.iloc[:, 1:].sum(axis=1)
df["Average"] = df["Total"] / (df.shape[1] - 1)

# Assign grades
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(assign_grade)

# Print analyzed data
print("📊 Student Results:\n")
print(df)
print("\nClass Average:", round(df["Average"].mean(), 2))

# Bar chart - Total Marks
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Total"], color='skyblue')
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Pie chart - Grade Distribution
grade_counts = df["Grade"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    grade_counts,
    labels=grade_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['#66b3ff','#99ff99','#ffcc99','#ff9999','#c2c2f0']
)
plt.title("Grade Distribution")
plt.show()
