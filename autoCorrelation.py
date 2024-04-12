import numpy as np

def windowcorrelation(sig1, sig2):
    return np.sum(sig1 * sig2) / len(sig1)


def coeffautocorrelation(sig, L, N, i):
    rn0 = windowcorrelation(sig[i:i+N], sig[i:i+N])
    autocorr_coeffs = []
    for l in range(44, L):
        autocorr_coeffs.append(windowcorrelation(sig[i:i+N], sig[i+l:i+l+N])/rn0)
    return (np.argmax(autocorr_coeffs)+44, np.max(autocorr_coeffs))


def computeAutoCorrelation(signal, m, N, L):
    autocorr_evolutions = []
    autocorr_coeffs = []
    for i in range(0, len(signal)-(2*max(L,N)), m):
        l, coeff = coeffautocorrelation(signal, L, N, i)
        autocorr_evolutions.append(l)
        autocorr_coeffs.append(coeff)
    return (autocorr_evolutions, autocorr_coeffs)
