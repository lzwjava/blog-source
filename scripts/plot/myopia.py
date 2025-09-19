import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Step 1: Create the data
data = {
    "Date": ["2022-03-05", "2022-11-13", "2023-04-20", "2024-01-07", "2024-11-28"],
    "Left Eye Myopia": [-3.50, -3.25, -3.00, -3.00, -2.50],
    "Left Eye Astigmatism": [-2.25, -2.00, -1.25, -1.00, -1.00],
    "Right Eye Myopia": [-5.75, -5.50, -5.00, -4.75, -4.25],
    "Right Eye Astigmatism": [-1.75, -1.75, -1.25, -1.25, -1.25],
    # 'Correct Vision' column is omitted as per your previous request
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Step 3: Plotting
plt.figure(figsize=(12, 8))

# Plot Left Eye Myopia
plt.plot(
    df["Date"], df["Left Eye Myopia"], marker="o", label="Left Eye Myopia", color="blue"
)

# Plot Right Eye Myopia
plt.plot(
    df["Date"],
    df["Right Eye Myopia"],
    marker="o",
    label="Right Eye Myopia",
    color="red",
)

# Plot Left Eye Astigmatism
plt.plot(
    df["Date"],
    df["Left Eye Astigmatism"],
    marker="s",
    label="Left Eye Astigmatism",
    color="green",
)

# Plot Right Eye Astigmatism
plt.plot(
    df["Date"],
    df["Right Eye Astigmatism"],
    marker="s",
    label="Right Eye Astigmatism",
    color="purple",
)

# Adding annotations for Correct Vision
# Since Correct Vision is either 0.9 or 1.0, we can annotate these points on the graph
# These annotations are placed below the minimum astigmatism value
correct_vision = [1.0, 0.9, 1.0, 0.9, 0.9]
min_astigmatism = df[["Left Eye Astigmatism", "Right Eye Astigmatism"]].min().min()

for idx, (date, vision) in enumerate(zip(df["Date"], correct_vision)):
    plt.annotate(
        f"CV: {vision}",
        (date, min_astigmatism - 0.5),
        textcoords="offset points",
        xytext=(0, -10),
        ha="center",
        fontsize=8,
        color="black",
    )

# Invert the Y-axis to make improvement downward
plt.gca().invert_yaxis()

# Formatting the plot with a personalized title
plt.title(
    "Zhiwei Li's Progress in Reversing Myopia and Astigmatism Naturally",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Diopters", fontsize=12)
plt.legend()
plt.grid(True)

# Improve date formatting on the x-axis
date_form = DateFormatter("%Y-%m")
plt.gca().xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
