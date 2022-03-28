"""
File that will contain procedure of user to BSs
association, three algorithms will be supported:
- RX    - based on received signal strength
- NO_UE - aimed at balancing the load between cells
- SE    - aimed at spectral efficiency maximization 
"""
import numpy as np
import params

def userAssociation(method,pathloss):
    no_bs, no_ue = pathloss.shape
    rss = np.transpose(pathloss) + np.tile(params.tx_power_dbm, (no_ue, 1))
    
    if method == 'RX':
        assignment = RX(rss, no_ue)

    return assignment


def RX(rss, no_ue):
    assignment = np.zeros((no_ue))
    max_rss = np.max(rss,axis=1)
    assignment[max_rss > params.min_rec_power_dbm] =\
         np.argmax(rss[max_rss > params.min_rec_power_dbm,:],axis=1)+1
    return assignment