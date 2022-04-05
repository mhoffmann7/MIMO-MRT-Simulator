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
tx_power_dbm = np.array([46, 33, 33, 33, 33, 33]) # dBm

# Thermal noise power
noise_pwr_dbm = -174 # dBm/Hz

# Bandwidth 
bandwidth = 10 # MHz

# coordinates of BSs
BSs = np.array([[594, 975],
        [717, 1035],
        [732, 897],
        [717, 759],
        [732, 621],
        [518, 697]])

# coordinates of buildings
B = [[9, 423, 129, 543],
    [9, 285, 129, 405],
    [9, 147, 129, 267],
    [9, 9, 129, 129],
    [147, 423,  267, 543],
    [147, 147, 267, 267],
    [147, 9, 267, 129 ],
    [297, 423, 327, 543],
    [297, 285, 327, 405],
    [297, 147, 327, 267],
    [297, 9, 327, 129],
    [348, 423, 378, 543],
    [348, 285, 378, 405],
    [348, 147, 378, 267],
    [348, 9, 378, 129]]
R = [387,552]