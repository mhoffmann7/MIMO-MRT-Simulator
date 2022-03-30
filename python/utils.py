import matplotlib.pyplot as plt
import scipy
import numpy as np
from matplotlib.patches import Rectangle

def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]

def plotSingleResults(positions, bitrates):

    fig, ax = plt.subplots(1, 2)

    # plot buildings
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

    for bs_coord in B:
        x1 = bs_coord[0] + R[0]
        y1 = bs_coord[1] + R[1]
        x2= bs_coord[2] + R[0]
        y2 = bs_coord[3] + R[1]
        width = x2 - x1
        height = y2-y1
        ax[0].add_patch(Rectangle((x1, y1), width, height,facecolor='tab:gray'))

    # plot BSs
    BSs = np.array([[594, 975],
        [717, 1035],
        [732, 897],
        [717, 759],
        [732, 621],
        [518, 697]])
    ax[0].scatter(BSs[:,0],BSs[:,1],s=50)    
    
    # plot users
    ax[0].scatter(positions[:,0],positions[:,1], s=15)


    x, cdf = ecdf(bitrates) # calculate the cdf - also discrete
    ax[1].plot(x, cdf)
    plt.show()