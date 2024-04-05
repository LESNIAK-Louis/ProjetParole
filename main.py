import sys
from scipy.io.wavfile import read

from plotInfos import plotValues

from energy import computeEnergy
from zeroCrossing import computeZeroCrossing
from autoCorrelation import computeAutoCorrelation
from f0 import computeF0
from evalutation import writeFile, compareFiles


def signalMean(signal):
    sum = 0
    for s in signal:
        sum += s 
    moyenne = sum/len(signal)

    return moyenne


# MAIN
freqsampling, signalTab = read(sys.argv[1])

signalTab = signalTab - signalMean(signalTab)

M = int(8*freqsampling/1000)
N = int(16*freqsampling/1000)
L = int(25*freqsampling/1000)

energyTab = computeEnergy(signalTab, M, N)
zeroTab = computeZeroCrossing(signalTab, M, N)

N = int(25*freqsampling/1000)

autoCorrelTabL, autoCorrelTabCoeffs  = computeAutoCorrelation(signalTab, M, N, L)

f0Passage0, f0Energy, decisions = computeF0(freqsampling, autoCorrelTabL, zeroTab, energyTab)

plotValues(sys.argv[1], signalTab, energyTab, zeroTab, autoCorrelTabL, decisions, f0Passage0, f0Energy)

"""
OUTPUT_FILE = "output.txt"

writeFile(OUTPUT_FILE, f0Passage0, decisions, autoCorrelTabCoeffs)
compareFiles(OUTPUT_FILE, nameFileRef=OUTPUT_FILE)
"""

