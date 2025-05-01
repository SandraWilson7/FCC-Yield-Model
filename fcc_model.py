import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('fcc_data.csv')

# Print columns to verify
print("Columns in CSV:", data.columns.tolist())

# Create the graph
plt.scatter(data["Temperature"], data["Gasoline_Yield"])
plt.xlabel('Temperature (°C)')
plt.ylabel('Gasoline Yield (%)')
plt.title('FCC Yield vs. Temperature')
plt.show()