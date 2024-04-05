import numpy as np

def windowenergy(partie_du_signal):
    tab = np.float32(partie_du_signal)

    energie = 0
    for s in tab:
        energie += s**2
    return energie


def computeEnergy(signal, m, N):
    energie = []

    for i in range(0, len(signal)-N, m): 
        energie.append(windowenergy(signal[i:i+N+1]))

    return 10*np.log10(energie)