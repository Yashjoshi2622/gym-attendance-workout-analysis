import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/gym_data.csv")

# Gender-wise attendance analysis
sns.countplot(x="gender", hue="attendance_status", data=df)
plt.title("Gender-wise Gym Attendance")
plt.show()

# Workout type vs calories burned
sns.boxplot(x="workout_type", y="calories_burned", data=df)
plt.title("Workout Type vs Calories Burned")
plt.show()

# Workout duration vs calories burned
sns.scatterplot(
    x="workout_duration_minutes",
    y="calories_burned",
    hue="workout_type",
    data=df
)
plt.title("Workout Duration vs Calories Burned")
plt.show()
