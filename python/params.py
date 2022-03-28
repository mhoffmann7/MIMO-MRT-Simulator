"""
File containing simulation parameters, to be done is to replace it
with loading parameters from json file.
"""
import numpy as np

# minimum received signal strength (RSS) necessary to serve user
min_rec_power_dbm = -120 # dBm

# number of antennas, channels were generated for 1 Macro BS of 128 antennas
# and 5 Pico BSs of 32 antennas 
antennas = np.array([128, 32, 32, 32, 32, 32])

# TX power
tx_power_dbm = np.array([46, 30, 30, 30, 30, 30]) # dBm

# Thermal noise power
noise_pwr_dbm = -174 # dBm/Hz