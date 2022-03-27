"""
This file is responsible for loading radio channels
from files and obtaining random users. The channel is
pregenerated for N users function can select random 
topology of K users.
"""
import hdf5storage
import numpy as np

def getUsers(scenario, no_active_users):

    # Get radio channel associated with given scenario
    if scenario == 'day':

        data_path = '../channel_data/'
        pathloss = getPathloss(data_path+'pathloss.mat')
        position = getPosition(data_path+'position.mat')
        corr_data = getCorrData(data_path+'corr_data.mat')
    else:
        raise ValueError("non existing scenario is chosen")

    # Randomly obtain of group of UEs
    no_bs, no_ue = pathloss.shape
    ue_indices = range(0,no_ue)
    active_ue_indices = np.random.choice(ue_indices, no_active_users)

    # Process pathloss, positions and correlation coefficients 
    # to select only subset of users
    pathloss = pathloss[:,active_ue_indices]
    position = position[active_ue_indices,:]

    tmp_corr_data = corr_data
    corr_data = []
    for bs in range(0, no_bs):
        
        tmp = tmp_corr_data[:,:,bs]
        tmp = tmp[active_ue_indices,:]
        tmp = tmp[:,active_ue_indices]
        tmp = np.array(tmp)
        corr_data.append(tmp)
   

    return pathloss, position, corr_data

def getPathloss(path):
    mat = hdf5storage.loadmat(path)
    return mat['pathloss'] 

def getPosition(path):
    mat = hdf5storage.loadmat(path)
    position = mat['position'][:,0:2]
    return position

def getCorrData(path):
    mat = hdf5storage.loadmat(path)

    return mat['corr_data']
    