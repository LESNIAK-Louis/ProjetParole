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

    path, ext = os.path.splitext(filename)

    output_file = ""
    if(ext == ".wav"): # Analyse du fichier son
        output_file = path + ".f0"

        freqsampling, signalTab = read(filename)

        signalTab = signalTab - signalMean(signalTab)

        M = int(10*freqsampling/1000)
        N = int(32*freqsampling/1000)
        L = int(25*freqsampling/1000)

        energyTab = computeEnergy(signalTab, M, N)
        zeroTab = computeZeroCrossing(signalTab, M, N)

        autoCorrelTabL, autoCorrelTabCoeffs  = computeAutoCorrelation(signalTab, M, N, L)

        f0, decisions = computeF0(freqsampling, autoCorrelTabL, zeroTab, energyTab)

        if plot_graph:
            plotValues(filename, signalTab, energyTab, zeroTab, autoCorrelTabL, decisions, f0)

        writeFile(output_file, f0, decisions, autoCorrelTabCoeffs)

    elif(ext == ".f0"): # Fichier déjà analysé à comparer
        output_file = filename
        if(not ref_file):
            print("Veuillez spécifier un fichier de référence en argument (-r PATH).")
            sys.exit(1)
    else:
        print("Argument(s) invalide(s).")
        sys.exit(1)

    if(ref_file): # Fichier de référence pour la comparaison
        compareFiles(output_file, ref_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", help="Entrez le chemin du fichier .wav à analyser ou celui d'un fichier .f0 à comparer")
    parser.add_argument("-r", help="Entrez le fichier de référence à comparer (.f0)")
    parser.add_argument("-p", help="Afficher ou non les graphiques correspondants", action='store_true')
    args = parser.parse_args()
    main(args)