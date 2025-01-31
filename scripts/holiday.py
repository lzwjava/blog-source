import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Holiday data for China and Hong Kong
holidays = {
    "China": [
        {"name": "New Year's Day", "date": "2025-01-01", "duration": 1},
        {"name": "Spring Festival", "date": "2025-01-29", "duration": 7},
        {"name": "Qingming Festival", "date": "2025-04-05", "duration": 1},
        {"name": "Labor Day", "date": "2025-05-01", "duration": 1},
        {"name": "Dragon Boat Festival", "date": "2025-06-06", "duration": 1},
        {"name": "Mid-Autumn Festival", "date": "2025-09-19", "duration": 1},
        {"name": "National Day", "date": "2025-10-01", "duration": 7},
    ],
    "Hong Kong": [
        {"name": "The first day of January", "date": "2025-01-01", "duration": 1},
        {"name": "Lunar New Year", "date": "2025-01-29", "duration": 4},
        {"name": "Ching Ming Festival", "date": "2025-04-04", "duration": 1},
        {"name": "Good Friday", "date": "2025-04-18", "duration": 1},
        {"name": "The day following Good Friday", "date": "2025-04-19", "duration": 1},
        {"name": "Easter Monday", "date": "2025-04-21", "duration": 1},
        {"name": "Labor Day", "date": "2025-05-01", "duration": 1},
        {"name": "Buddha's Birthday", "date": "2025-05-20", "duration": 1},
        {"name": "Tuen Ng Festival", "date": "2025-06-06", "duration": 1},
        {"name": "Hong Kong Special Administrative Region Establishment Day", "date": "2025-07-01", "duration": 1},
        {"name": "The day following the Chinese Mid-Autumn Festival", "date": "2025-09-20", "duration": 1},
        {"name": "Chinese Mid-Autumn Festival", "date": "2025-09-21", "duration": 1},
        {"name": "Chung Yeung Festival", "date": "2025-10-05", "duration": 1},
        {"name": "Chinese National Day", "date": "2025-10-06", "duration": 1},
        {"name": "Christmas Day", "date": "2025-12-25", "duration": 1},
        {"name": "The first weekday after Christmas Day", "date": "2025-12-26", "duration": 1},
    ],
}

# Create the plot
fig, ax = plt.subplots(figsize=(15, 6))

# Plot each country's holidays
for country, country_holidays in holidays.items():
    for holiday in country_holidays:
        date = datetime.strptime(holiday["date"], "%Y-%m-%d")
        duration = holiday["duration"]
        ax.barh(country, duration, left=date, height=0.5, label=holiday["name"])

# Format the plot
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax.set_xlabel("Date")
ax.set_ylabel("Country")
ax.set_title("2025 Holiday Schedule (China & Hong Kong)")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
