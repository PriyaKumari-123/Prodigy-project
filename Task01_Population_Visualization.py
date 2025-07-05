
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Population Dataset based on World Bank 2022 estimates
data = {
    'Country': ['India', 'China', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico'],
    'Population': [1417173173, 1425887337, 339996563, 277534123, 235824862, 215353593, 223804632, 172954319, 144713314, 126705138]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Population Dataset:")
print(df)

# Bar Chart for Population Distribution
plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='Population', data=df, palette='viridis')
plt.title('Population Distribution by Country (2022 Estimates)', fontsize=14)
plt.xlabel('Country')
plt.ylabel('Total Population')
plt.xticks(rotation=45)
plt.show()

# Histogram Example with Random Age Data
# Generating random age data for 1000 people
ages = np.random.randint(0, 100, 1000)

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution in a Sample Population')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
