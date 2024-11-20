import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.system("cls")

# 1 get data
df = pd.read_csv(r"C:\Users\TheGirlo\Desktop\ConservationLabDataFixed.csv")

# 2 simplify/clean data
df = df[['Latest: Time (s)', 'Latest: Position (m)', 'Latest: Velocity (m/s)', 'Latest: Acceleration (m/s²)']]
df = df.rename(columns = {
    'Latest: Time (s)': 'T', 
    'Latest: Position (m)': 'P', 
    'Latest: Velocity (m/s)': 'V', 
    'Latest: Acceleration (m/s²)': 'A'
})

# 3 constants and calculations
max_height = 0.115  # y in the lab instructions (height of wooden block)
track_length = max_pos = df['P'].max()  # r in the lab instructions
cart_mass = 0.3224  # kg
g = 9.80  # m/s²

# Calculate sine of angle directly (no np.sin needed as this IS the sine)
sin_theta = max_height / track_length

# Calculate x (distance up the track)
df['x'] = max_pos - df['P']

# Calculate height using correct relationship
df['y'] = df['x'] * sin_theta

# Calculate energies
df['K'] = 0.5 * cart_mass * df['V']**2  # Kinetic energy
df['U'] = cart_mass * g * df['y']       # Potential energy
df['E'] = df['K'] + df['U']             # Total energy

# Rename columns for plotting
df = df[['T','U','E','K']]
df = df.rename(columns = {
    'T': 'Time (S)', 
    'U': 'Potential Energy (U)', 
    'E': 'Total Energy (TE)', 
    'K': 'Kinetic Energy (K)'
})

# Create plots
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10,12))

# Plot 1: Potential Energy
ax1.plot(df['Time (S)'], df['Potential Energy (U)'], label="Potential Energy (U)", color='blue')
ax1.set_ylabel('Potential Energy (J)')
ax1.set_xlabel('Time (S)')
ax1.legend()

# Plot 2: Kinetic Energy
ax2.plot(df['Time (S)'], df['Kinetic Energy (K)'], label="Kinetic Energy (K)", color='red')
ax2.set_ylabel('Kinetic Energy (J)')
ax2.set_xlabel('Time (S)')
ax2.legend()

# Plot 3: Total Energy
ax3.plot(df['Time (S)'], df['Total Energy (TE)'], label="Total Energy (TE)", color='purple')
ax3.set_ylabel('Total Energy (J)')
ax3.set_xlabel('Time (S)')
ax3.legend()

# Plot 4: All Energies
ax4.plot(df['Time (S)'], df['Total Energy (TE)'], label="Total Energy (TE)", color='purple')
ax4.plot(df['Time (S)'], df['Potential Energy (U)'], label="Potential Energy (U)", color='blue')
ax4.plot(df['Time (S)'], df['Kinetic Energy (K)'], label="Kinetic Energy (K)", color='red')
ax4.set_ylabel('Energy (Joules)')
ax4.set_xlabel('Time (S)')
ax4.legend()

plt.tight_layout(pad=3.0)
plt.show()