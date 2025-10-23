import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
DATA_FILE_PATH = "data/marks.csv"
IMAGE_DIR = "images/"

# --- DATA LOADING & CLEANING ---
try:
    df = pd.read_csv(DATA_FILE_PATH)
except FileNotFoundError:
    print(f"Error: Data file not found at {DATA_FILE_PATH}")
    exit()

# --- DATA ANALYSIS ---
# Calculate Total and Average Marks
# iloc[:, 1:] selects columns starting from the second one (assuming the first is 'Name')
NUM_SUBJECTS = df.shape[1] - 1
df['total_marks'] = df.iloc[:, 1:].sum(axis=1)
df['average_mark'] = df['total_marks'] / NUM_SUBJECTS

# Function to assign grades based on average mark
def assign_grade(average):
    """Assigns a letter grade based on the student's average mark."""
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

# Apply grade assignment
df['grade'] = df['average_mark'].apply(assign_grade)

# --- RESULTS SUMMARY ---
print("--- Student Result Analysis ---")
print("\nAnalyzed Data:")
print(df)
print("\nClass Average Mark:", round(df['average_mark'].mean(), 2))
print("-----------------------------\n")

# --- VISUALIZATION ---

# 1. Bar Chart: Total Marks of Students
def plot_total_marks_bar_chart(data_frame):
    """Generates and saves a bar chart for students' total marks."""
    plt.figure(figsize=(10, 6))
    
    # Use standard column names from the data frame
    plt.bar(data_frame['Name'], data_frame['total_marks'], color="#1f77b4")
    
    plt.title("Total Marks Distribution Across Students", fontsize=14)
    plt.xlabel("Student Name", fontsize=12)
    plt.ylabel("Total Marks", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Save the figure to the specified directory
    plt.tight_layout() # Adjusts plot to prevent labels from being cut off
    plt.savefig(f'{IMAGE_DIR}bar_chart_total_marks.png') 
    plt.close() # Close the figure to free up memory

# 2. Pie Chart: Grade Distribution
def plot_grade_distribution_pie_chart(data_frame):
    """Generates and saves a pie chart for the grade distribution."""
    grade_counts = data_frame['grade'].value_counts()
    
    plt.figure(figsize=(7, 7))
    
    # Custom color palette for consistency
    colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0'][:len(grade_counts)]
    
    plt.pie(
        grade_counts,
        labels=grade_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
        wedgeprops={'edgecolor': 'black'} # Adds a border for clarity
    )
    plt.title("Grade Distribution Across Class", fontsize=14)
    
    # Save the figure to the specified directory
    plt.tight_layout()
    plt.savefig(f'{IMAGE_DIR}pie_chart_grade_distribution.png')
    plt.close() # Close the figure

# Execute the plotting functions
if __name__ == "__main__":
    plot_total_marks_bar_chart(df)
    plot_grade_distribution_pie_chart(df)
    print(f"Charts saved successfully to the '{IMAGE_DIR}' directory.")
    
 