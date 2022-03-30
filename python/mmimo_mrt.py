import params
import numpy as np

def computeBitrates(pathloss, corr_data, assignment):

    no_bs, no_ue = pathloss.shape
    rss = np.transpose(pathloss) + np.tile(params.tx_power_dbm, (no_ue, 1))
    rss_lin = np.power(10,rss/10)
    
    interference = np.zeros(no_ue)
    # Compute interference
    for bs in range(1, no_bs+1):
        tmp_corr = np.power(corr_data[bs-1],2)
        signal = rss_lin[:,bs-1]
        x = np.diag(assignment == bs).astype(int)
        K = np.sum(x) # number of users in cell
        if K == 0:
            continue
        M = params.antennas[bs-1] # number of antennas in cell
        tmp_interf = M * np.dot(np.dot(tmp_corr, x),  np.transpose(signal)) / K
        interference = interference + tmp_interf

    # add noise
    interference = interference + np.power(10, params.noise_pwr_dbm/10)

    # compute wanted signal
    bitrates = np.zeros(no_ue)
    for ue in range(0, no_ue):
        bs = int(assignment[ue])
        if bs == 0:
            continue
        K = np.sum((assignment == bs).astype(int)) # number of users in cell
        P = rss_lin[ue,bs-1]
        M = params.antennas[bs-1] # number of antennas in cell
        wanted_signal = M*P / K
        bitrates[ue] = params.bandwidth *K*np.log2(1 + wanted_signal / interference[ue]) # Mbps

    return bitrates
    