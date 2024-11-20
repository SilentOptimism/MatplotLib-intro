import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.signal import argrelextrema

os.system("cls")

#1 get data
df = pd.read_csv(r"C:\Users\TheGirlo\Desktop\ConservationLabDataFixed.csv") #use rawstrings for paths

#2 print data
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False) # removes that weird line break

#3 simplfy/clean data
df = df[['Latest: Time (s)', 'Latest: Position (m)', 'Latest: Velocity (m/s)', 'Latest: Acceleration (m/s²)']]
df = df.rename(columns = {'Latest: Time (s)': 'T', 'Latest: Position (m)': 'P', 'Latest: Velocity (m/s)' : 'V', 'Latest: Acceleration (m/s²)': 'A'})

#5 manipulate the data
max_height = 0.115
cartWeightKilograms = 0.3224
g = 9.80

#Calculates the values for X
max_pos = df['P'].max()
df['x'] = max_pos - df.P# The distance of the ball

#Calcuates the Values for H
angle = np.arcsin(max_height/max_pos) # angle between ramp and table
df['y'] = np.sin(angle)*df.x # The height of the ball

#Calculates the values for the Kinetic energy
df['K'] = 0.5*cartWeightKilograms*(pow(df.V,2))

#Calculates the values for the Potential Energy
df['U'] = (cartWeightKilograms*g*df.y)

#Calculates the values for the Total Energy
df['E'] = df.K + df.U


df = df[['T','U','E','K', 'V']]
df = df.rename(columns = {'T':'Time (S)', 'U': 'Potential Energy (U)', 'E': 'Total Energy (TE)', 'K': 'Kinetic Energy (K)'})

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5,1, figsize=(10,12))

ax1.plot(df['Time (S)'], df['Potential Energy (U)'], label = "Potential Energy (U)", color = 'blue')
ax1.set_ylabel('Potential Energy (U)')
ax1.set_xlabel('Time (S)')
ax1.legend()
ax1.grid(True, which = 'Both')

ax2.plot(df['Time (S)'], df['Kinetic Energy (K)'], label = "Kinetic Energy (K)", color = 'red')
ax2.set_ylabel('Kinetic Energy (K)')
ax2.set_xlabel('Time (S)')
ax2.legend()
ax2.grid(True, which = 'Both')

ax3.plot(df['Time (S)'], df['Total Energy (TE)'], label = "Total Energy (TE)", color = 'purple')
ax3.set_ylabel('Total Energy (TE)')
ax3.set_xlabel('Time (S)')
ax3.legend()
ax3.grid(True, which = 'Both')

ax4.plot(df['Time (S)'], df['Total Energy (TE)'], label = "Total Energy (TE)", color = 'purple')
ax4.plot(df['Time (S)'], df['Potential Energy (U)'], label = "Potential Energy (U)", color = 'blue')
ax4.plot(df['Time (S)'], df['Kinetic Energy (K)'], label = "Kinetic Energy (K)", color = 'red')
ax4.set_ylabel('Energy (Joules)')
ax4.set_xlabel('Time (S)')
ax4.legend()
ax4.grid(True, which = 'Both')

ax5.plot(df['Time (S)'], df['V'], label = "Velocity (m/s)", color = 'orange')
ax5.set_ylabel('Velocity (m/s)')
ax5.set_xlabel('Time (S)')
ax5.legend()
ax5.grid(True, which = 'Both')

# Find local maxima and minima
for col in ['V']:
    data = df[col].values
    maxima = df['Time (S)'][argrelextrema(data, np.greater)[0]]
    minima = df['Time (S)'][argrelextrema(data, np.less)[0]]

    for x, y in zip(maxima, df.loc[df['Time (S)'].isin(maxima), col]):
        ax5.plot(x, y, 'ro', markersize=10, label=f'{col} Maxima')
        ax5.annotate(f'({x:.2f}, {y:.2f})', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    for x, y in zip(minima, df.loc[df['Time (S)'].isin(minima), col]):
        ax5.plot(x, y, 'bv', markersize=10, label=f'{col} Minima')
        ax5.annotate(f'({x:.2f}, {y:.2f})', (x, y), textcoords="offset points", xytext=(0, -30), ha='center')

plt.tight_layout(pad = 3.0)
plt.show()
