from cProfile import label
import matplotlib.pyplot as plt
import scipy
import numpy as np
from matplotlib.patches import Rectangle
from params import BSs, B, R

def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]

def plotSingleResults(positions, bitrates, action):

    fig, ax = plt.subplots(1, 2)

    # plot buildings
    for bs_coord in B:
        x1 = bs_coord[0] + R[0]
        y1 = bs_coord[1] + R[1]
        x2= bs_coord[2] + R[0]
        y2 = bs_coord[3] + R[1]
        width = x2 - x1
        height = y2-y1
        ax[0].add_patch(Rectangle((x1, y1), width, height,facecolor='tab:gray'))

    # plot BSs
    off_bs = [int(x)  == 0 for x in list(bin(action)[2:].zfill(len(BSs)-1))]
    off_bs = np.array([False] + off_bs)
    ax[0].scatter(BSs[:,0],BSs[:,1],s=50, label='BSs')
    ax[0].scatter(BSs[off_bs,0],BSs[off_bs,1],s=50, label='BSs',color='black')      
    
    # plot users
    ax[0].scatter(positions[:,0],positions[:,1], s=15, label='UEs')


    x, cdf = ecdf(bitrates) # calculate the cdf - also discrete
    ax[1].plot(x, cdf)
    plt.show()

def plotSeveralCellEdge(off_ce, opt_ce):
    plt.figure()
    off_x, off_cdf = ecdf(off_ce)
    opt_x, opt_cdf = ecdf(opt_ce)
    plt.plot(off_x, off_cdf, label='No DPB')
    plt.plot(opt_x, opt_cdf, label='Optimal DPB')
    plt.legend()
    plt.show()