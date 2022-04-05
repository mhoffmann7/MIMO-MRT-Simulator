import numpy as np
from user_association import userAssociation
from mmimo_mrt import computeBitrates
import copy


class Dpb:

    def __init__ (self, dpb_agent_path):
        self.dpb_agent_path = dpb_agent_path
        # load NN weights

    def dpb(self, algorithm, assignment_method, pathloss, corr_data):

        no_bs, no_ue = pathloss.shape
        if algorithm == 'optimal':
            action = self.optimalDPB(assignment_method, pathloss, corr_data)
        else: # By default switch on all BSs
            action = 2 ** (no_bs-1) -1

        return self.setActiveBSsConfiguration(action, no_bs,pathloss), action


    def setActiveBSsConfiguration(self, action, no_bs,pathloss):
            active_bs = [int(x)  == 0 for x in list(bin(action)[2:].zfill(no_bs-1))]
            active_bs = np.array([False] + active_bs)
            pathloss_tmp = copy.deepcopy(pathloss)
            pathloss_tmp[active_bs, :] = -2000
            return pathloss_tmp

    def optimalDPB(self, assignment_method, pathloss, corr_data):
        no_bs, no_ue = pathloss.shape
        actions = np.zeros(2 ** (no_bs-1))

        for a in range(0, len(actions)):
            pathloss_tmp = self.setActiveBSsConfiguration(a, no_bs,pathloss)
            assignment = userAssociation(assignment_method,pathloss_tmp)
            bitrates = computeBitrates(pathloss_tmp, corr_data, assignment)
            actions[a] = np.quantile(bitrates, 0.1) # cell_edge users 10-th percentile
        return np.argmax(actions)
    