import numpy as np
from user_association import userAssociation
from mmimo_mrt import computeBitrates
import copy

def dpb(algorithm, assignment_method, pathloss, corr_data):
    
    no_bs, no_ue = pathloss.shape
    if algorithm == 'optimal':
        action = optimalDPB(assignment_method, pathloss, corr_data)
    else: # By default switch on all BSs
        action = 2 ** (no_bs-1) -1


    return setActiveBSsConfiguration(action, no_bs,pathloss), action


def setActiveBSsConfiguration(action, no_bs,pathloss):
        active_bs = [int(x)  == 0 for x in list(bin(action)[2:].zfill(no_bs-1))]
        active_bs = np.array([False] + active_bs)
        pathloss_tmp = copy.deepcopy(pathloss)
        pathloss_tmp[active_bs, :] = -2000
        return pathloss_tmp

def optimalDPB(assignment_method, pathloss, corr_data):
    no_bs, no_ue = pathloss.shape
    actions = np.zeros(2 ** (no_bs-1))

    for a in range(0, len(actions)):
        pathloss_tmp = setActiveBSsConfiguration(a, no_bs,pathloss)
        assignment = userAssociation(assignment_method,pathloss_tmp)
        bitrates = computeBitrates(pathloss_tmp, corr_data, assignment)
        actions[a] = np.quantile(bitrates, 0.1) # cell_edge users 10-th percentile
    return np.argmax(actions)
    