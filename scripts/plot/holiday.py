import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

# Holiday data for Hong Kong
holidays_hk = [
    {"name": "Jan 1st", "date": "2025-01-01", "duration": 1},
    {"name": "Lunar New Year", "date": "2025-01-29", "duration": 4},
    {"name": "Ching Ming", "date": "2025-04-04", "duration": 1},
    {"name": "Good Friday", "date": "2025-04-18", "duration": 2},
    {"name": "Easter Monday", "date": "2025-04-21", "duration": 1},
    {"name": "Labor Day", "date": "2025-05-01", "duration": 1},
    {"name": "Buddha's Birthday", "date": "2025-05-20", "duration": 1},
    {"name": "Tuen Ng Festival", "date": "2025-06-06", "duration": 1},
    {"name": "HK SAR Day", "date": "2025-07-01", "duration": 1},
    {"name": "Mid-Autumn Festival", "date": "2025-09-20", "duration": 2},
    {"name": "Chung Yeung", "date": "2025-10-05", "duration": 1},
    {"name": "National Day", "date": "2025-10-06", "duration": 1},
    {"name": "Christmas", "date": "2025-12-25", "duration": 2},
]

# Holiday data for China
holidays_cn = [
    {"name": "New Year's Day", "date": "2025-01-01", "duration": 1},
    {"name": "Spring Festival", "date": "2025-01-29", "duration": 7},
    {"name": "Qingming Festival", "date": "2025-04-05", "duration": 1},
    {"name": "Labor Day", "date": "2025-05-01", "duration": 1},
    {"name": "Dragon Boat Festival", "date": "2025-06-06", "duration": 1},
    {"name": "Mid-Autumn Festival", "date": "2025-09-19", "duration": 1},
    {"name": "National Day", "date": "2025-10-01", "duration": 7},
]


# Calculate total holiday days for Hong Kong
total_days_hk = sum(holiday["duration"] for holiday in holidays_hk)
labels_hk = []
for holiday in holidays_hk:
    start_date = datetime.strptime(holiday["date"], "%Y-%m-%d")
    end_date = start_date + timedelta(days=holiday["duration"] - 1)
    end_date_str = end_date.strftime("%m-%d")
    start_date_str = start_date.strftime("%m-%d")
    labels_hk.append(f"{holiday['name']} ({start_date_str} to {end_date_str})")
sizes_hk = [holiday["duration"] for holiday in holidays_hk]


# Create the pie chart for Hong Kong
fig1, ax1 = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax1.pie(
    sizes_hk,
    labels=labels_hk,
    autopct="%1.1f%%",
    startangle=90,
    textprops={"color": "black"},
)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title(f"2025 Holiday Schedule (Hong Kong) - Total Days: {total_days_hk}")
plt.setp(autotexts, size=8, weight="bold")
plt.tight_layout()

# Save the first plot
plt.savefig(os.path.join(os.path.dirname(__file__), "holiday_schedule_hk.jpg"))


# Calculate total holiday days for China
total_days_cn = sum(holiday["duration"] for holiday in holidays_cn)
labels_cn = []
for holiday in holidays_cn:
    start_date = datetime.strptime(holiday["date"], "%Y-%m-%d")
    end_date = start_date + timedelta(days=holiday["duration"] - 1)
    end_date_str = end_date.strftime("%m-%d")
    start_date_str = start_date.strftime("%m-%d")
    labels_cn.append(f"{holiday['name']} ({start_date_str} to {end_date_str})")
sizes_cn = [holiday["duration"] for holiday in holidays_cn]

# Create the pie chart for China
fig2, ax2 = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax2.pie(
    sizes_cn,
    labels=labels_cn,
    autopct="%1.1f%%",
    startangle=90,
    textprops={"color": "black"},
)
ax2.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set_title(f"2025 Holiday Schedule (China) - Total Days: {total_days_cn}")
plt.setp(autotexts, size=8, weight="bold")
plt.tight_layout()


# Save the second plot
plt.savefig(os.path.join(os.path.dirname(__file__), "holiday_schedule_cn.jpg"))

plt.show()
