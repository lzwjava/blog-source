import matplotlib.pyplot as plt
import os

# Data for the plot
network_types = ["Modem -> TP-LINK Router -> Phone", "Modem -> Cable -> Phone"]
download_speeds = [2.90, 84.9]
upload_speeds = [4.82, 59.7]
line_info = ["Guangzhou -> Macao", "Guangzhou -> Macao"]


# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.35

# Positions of the bars on the x-axis
r1 = range(len(network_types))
r2 = [x + bar_width for x in r1]

# Create bars for download speeds
ax.bar(
    r1,
    download_speeds,
    color="skyblue",
    width=bar_width,
    edgecolor="grey",
    label="Download Speed (MBPS)",
)

# Create bars for upload speeds
ax.bar(
    r2,
    upload_speeds,
    color="coral",
    width=bar_width,
    edgecolor="grey",
    label="Upload Speed (MBPS)",
)

# Add labels and title
ax.set_xlabel("Network Type", fontweight="bold")
ax.set_ylabel("Speed (MBPS)", fontweight="bold")
ax.set_title("Network Speed Comparison", fontweight="bold")
ax.set_xticks([r + bar_width / 2 for r in range(len(network_types))])
ax.set_xticklabels(
    [f"{net}\n({line})" for net, line in zip(network_types, line_info)],
    rotation=10,
    ha="right",
)


# Add legend
ax.legend()

# Add grid
plt.grid(axis="y", linestyle="--")

# Adjust layout to prevent labels from overlapping
plt.tight_layout()

# Save the chart as a JPG file in the current directory
plt.savefig(os.path.join(os.path.dirname(__file__), "network_speed_chart.jpg"))

# Show the plot
plt.show()
