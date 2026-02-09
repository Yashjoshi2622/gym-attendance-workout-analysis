import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/gym_data.csv")

sns.countplot(x="gender", hue="attendance_status", data=df)
plt.title("Gender-wise Gym Attendance")
plt.show()

sns.boxplot(x="workout_type", y="calories_burned", data=df)
plt.title("Workout Type vs Calories Burned")
plt.show()

sns.scatterplot(
    x="workout_duration_minutes",
    y="calories_burned",
    hue="workout_type",
    data=df
)
plt.title("Workout Duration vs Calories Burned")
plt.show()
