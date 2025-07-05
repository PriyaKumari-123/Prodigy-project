
# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

# Load Dataset (Change filename as needed)
data = pd.read_csv('US_Accidents_Dataset.csv')  # <-- Use your correct file here

# Display basic info
print("Sample Data:\n", data.head())
print("\nDataset Info:\n")
print(data.info())

# Extract necessary columns for analysis
data['Start_Time'] = pd.to_datetime(data['Start_Time'])
data['Hour'] = data['Start_Time'].dt.hour
data['Month'] = data['Start_Time'].dt.month
data['Year'] = data['Start_Time'].dt.year

# Accident Count by Hour
plt.figure(figsize=(10, 5))
sns.countplot(data=data, x='Hour', palette='coolwarm')
plt.title('Accident Count by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.show()

# Accident Count by Weather
plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='Weather_Condition', order=data['Weather_Condition'].value_counts().head(10).index)
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Count')
plt.ylabel('Weather Condition')
plt.show()

# Accident Count by Severity
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x='Severity', palette='mako')
plt.title('Accident Severity Distribution')
plt.show()

# Visualizing Accident Hotspots using Folium HeatMap
print("\nGenerating Accident Hotspot Map...")
accidents_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)  # Center of USA

# Prepare location points
locations = data[['Start_Lat', 'Start_Lng']].dropna().values.tolist()

# Add HeatMap
HeatMap(locations[:10000]).add_to(accidents_map)  # Limit to 10k points for speed

# Save Map
accidents_map.save("accident_hotspots_map.html")
print("Accident hotspot map saved as 'accident_hotspots_map.html'")
