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

    while line1 and line2:

        tab1 = line1.split(" ")
        tab2 = line2.split(" ")

        f01 = tab1[0]
        f02 = tab2[0]

        vois1 = tab1[1]
        vois2 = tab2[1]

        if vois1 != vois2:
            evoist += 1

        deltaf0 = abs(f01 - f02)/f02
        
        if deltaf0 > 0.95 and deltaf0 < 1.05:
            edouble += 1
        elif deltaf0 > 0.45 and deltaf0 < 0.55:
            emoitie += 1
        elif deltaf0 > 0.2:
            e20 += 1

        nb_ligne += 1

        line1 = f1.readline()
        line2 = f2.readline()

    evoist = evoist / nb_ligne

    e20 = e20 / nb_ligne
    emoitie = emoitie / nb_ligne
    edouble = edouble / nb_ligne

    return (evoist, e20, edouble, emoitie)
