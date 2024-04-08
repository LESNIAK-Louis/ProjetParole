import sys, os, argparse 
from scipy.io.wavfile import read

from plotInfos import plotValues

from energy import computeEnergy
from zeroCrossing import computeZeroCrossing
from autoCorrelation import computeAutoCorrelation
from f0 import computeF0
from evaluation import writeFile, compareFiles

def signalMean(signal):
    sum = 0
    for s in signal:
        sum += s 
    moyenne = sum/len(signal)

    return moyenne

def main(args):
    filename = args.f
    ref_file = args.r
    plot_graph = args.p

    output_file = os.path.splitext(filename)[0] + ".f0"

    freqsampling, signalTab = read(filename)

    signalTab = signalTab - signalMean(signalTab)

    M = int(8*freqsampling/1000)
    N = int(16*freqsampling/1000)
    L = int(25*freqsampling/1000)

    energyTab = computeEnergy(signalTab, M, N)
    zeroTab = computeZeroCrossing(signalTab, M, N)

    N = int(25*freqsampling/1000)

    autoCorrelTabL, autoCorrelTabCoeffs  = computeAutoCorrelation(signalTab, M, N, L)

    f0, decisions = computeF0(freqsampling, autoCorrelTabL, zeroTab, energyTab)

    if plot_graph:
        plotValues(filename, signalTab, energyTab, zeroTab, autoCorrelTabL, decisions, f0)

    writeFile(output_file, f0, decisions, autoCorrelTabCoeffs)
    compareFiles(output_file, ref_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", help="Entrez le chemin du fichier .wav à analyser")
    parser.add_argument("r", help="Entrez le fichier de référence à comparer (.f0)")
    parser.add_argument("-p", help="Afficher ou non les graphiques correspondants", action='store_true')
    args = parser.parse_args()
    main(args)