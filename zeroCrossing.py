import numpy as np

def sign(val):
    res = -1
    if(val > 0):
        res=1
    return res

def zeroCrossing(partie_du_signal):
    tab = np.int32(partie_du_signal)

    sum = 0
    for i in range(1,len(tab)):
        sum += abs(sign(tab[i]) - sign(tab[i-1]))

    return sum/(2*len(tab))

def computeZeroCrossing(signal, m, N):
    pasageZero = []

    for i in range(0, len(signal)-N, m): 
        pasageZero.append(zeroCrossing(signal[i:i+N+1]))

    return pasageZero