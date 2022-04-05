from get_users_channels import getUsers
from user_association import userAssociation
from mmimo_mrt import computeBitrates
from dpb import Dpb
import numpy as np




def singleUESetSimulation(no_ue, scenario, dpb_algorithm, dpb, assignment_method):

    pathloss, position, corr_data = getUsers(scenario,no_ue)
    pathloss, action = dpb.dpb(dpb_algorithm,assignment_method, pathloss, corr_data)
    assignment = userAssociation(assignment_method,pathloss)
    bitrates = computeBitrates(pathloss, corr_data, assignment)
    cell_edge = np.quantile(bitrates, 0.1) # cell_edge users 10-th percentile

    return bitrates, position, cell_edge, action


def multipleSimulations(no_sets, no_ue, scenario, dpb_algorithm, assignment_method, seed):
    dpb = Dpb('')
    np.random.seed(seed)
    cell_edges = np.zeros(no_sets)
    actions = np.zeros(no_sets)
    bitrates_per_set = []
    positions_per_set = []

    for set in range(0,no_sets):
        bitrates, positions,cell_edges[set], actions[set] = singleUESetSimulation(no_ue, scenario, dpb_algorithm, dpb, assignment_method)
        bitrates_per_set.append(bitrates)
        positions_per_set.append(positions)
    return cell_edges, actions, bitrates_per_set, positions_per_set


