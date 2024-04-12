import numpy as np

def writeFile(name, f0, decision, coeffAutoCorrel):
    f = open(name, "w")
    for i in range(0, len(f0)):
        f.write(str(float(f0[i])) + " " + str(float(decision[i])) + " 0.0 " + str(coeffAutoCorrel[i]) + "\n")
    f.close()

def compareFiles(name1, nameFileRef):
    f1 = open(name1, "r")
    f2 = open(nameFileRef, "r")

    line1 = f1.readline()
    line2 = f2.readline()

    evoist = 0

    e20 = 0
    edouble = 0
    emoitie = 0

    nb_ligne = 0
    nb_voisee = 0

    while line1 and line2:

        tab1 = line1.split(" ")
        tab2 = line2.split(" ")

        f01 = float(tab1[0])
        f02 = float(tab2[0])

        vois1 = float(tab1[1])
        vois2 = float(tab2[1])

        if vois1 != vois2:
            evoist += 1

        if vois2 == 1:
            deltaf0 = abs(f01 - f02)/f02
            
            if deltaf0 > 0.95 and deltaf0 < 1.05:
                edouble += 1
            if deltaf0 > 0.45 and deltaf0 < 0.55:
                emoitie += 1
            if deltaf0 > 0.2:
                e20 += 1

            nb_voisee += 1

        nb_ligne += 1

        line1 = f1.readline()
        line2 = f2.readline()

    evoist = evoist / nb_ligne

    e20 = e20 / nb_voisee
    emoitie = emoitie / nb_voisee
    edouble = edouble / nb_voisee

    print("Résultats de la comparaison des fichiers " + name1 + " et " + nameFileRef + " :")
    print("Erreurs voisement : " + str(np.around(evoist * 100, decimals=2)) + " %")
    print("Erreurs 20 % : " + str(np.around(e20 * 100,decimals=2)) + " %")
    print("Erreurs 50 % : " + str(np.around(edouble * 100,decimals=2)) + " %")
    print("Erreurs 100 % : " + str(np.around(emoitie * 100,decimals=2)) + " %")
    print("\n")
