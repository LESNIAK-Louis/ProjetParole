def decision(tabValue, index, lastDecision, SEUIL_BAS, SEUIL_HAUT):

    res = lastDecision

    if lastDecision:
        if (tabValue[index] <= SEUIL_BAS):
            res = 0
    else:
        if(tabValue[index] >= SEUIL_HAUT):
            res = 1

    return res

def computeF0(freqsampling, autoCorrelTab, zeroTab, energyTab):
    decisions = []
    f0 = []

    lastDecision0 = 1
    SEUIL_HAUT_0 = 0.15
    SEUIL_BAS_0 = 0.08

    lastDecisionE = 1
    SEUIL_HAUT_E = 95
    SEUIL_BAS_E = 70
    
    for i in range(0, len(autoCorrelTab)):
        lastDecision0 = decision(zeroTab, i, lastDecision0, SEUIL_BAS_0, SEUIL_HAUT_0)
        lastDecisionE = 1 - decision(energyTab, i, lastDecisionE, SEUIL_BAS_E, SEUIL_HAUT_E)
        
        if lastDecision0 and lastDecisionE:
            f0.append( int(float(freqsampling) /  float(autoCorrelTab[i])) )
        else:
            f0.append( 0 )

        decisions.append(lastDecision0 and lastDecisionE)

    return (f0, decisions)