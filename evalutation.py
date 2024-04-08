def computeDeviation(f0, f0Ref, pourcent):
    return abs(f0 - f0Ref) / f0Ref


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
    while line1 and line2:

        line1 = f1.readline()
        line2 = f2.readline()