import matplotlib.pyplot as plt

def plotValues(title, signal, energy, zero, autoCorrelTabL, decisions, f0Passage0, f0Energy):
    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7)
    fig.suptitle(title)

    ax1.set_title("Signal")
    ax1.set(xlabel="temps (echt)", xticks=[0, 5301,10602,15903,21204,26505,31806,37107,42408,47709])
    ax1.set(ylabel="Hz")
    ax1.plot(signal, 'tab:blue')

    ax2.set_title("Energie")
    ax2.set(xlabel="temps (echt)")
    ax2.set(ylabel="dB")
    ax2.plot(energy, 'tab:red')

    ax3.set_title("Passage à zéro")
    ax3.set(xlabel="temps (echt)")
    ax3.set(ylabel="")
    ax3.plot(zero, 'tab:green')

    ax4.set_title("Auto Correl")
    ax4.set(xlabel="temps (echt)")
    ax4.set(ylabel="")
    ax4.plot(autoCorrelTabL, 'tab:green')

    ax5.set_title("Decisions")
    ax5.set(xlabel="temps (echt)")
    ax5.set(ylabel="")
    ax5.plot(decisions, 'tab:green')

    ax6.set_title("F0 - Passage à 0")
    ax6.set(xlabel="temps (echt)")
    ax6.set(ylabel="")
    ax6.plot(f0Passage0, 'tab:orange')

    ax7.set_title("F0 - Energie")
    ax7.set(xlabel="temps (echt)")
    ax7.set(ylabel="")
    ax7.plot(f0Energy, 'tab:orange')

    #plt.tight_layout()
    plt.show()