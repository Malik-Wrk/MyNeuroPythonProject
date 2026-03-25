import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

LH_Data = pd.read_csv(
    "BiasedConnectivityVentralSubiculum/LH_TRIO_cellcounts.csv")

NA_Data = pd.read_csv(
    "BiasedConnectivityVentralSubiculum/NAc_TRIO_cellcounts.csv")

PFC_Data = pd.read_csv(
    "BiasedConnectivityVentralSubiculum/PFC_TRIO_cellcounts.csv")

sorted_LH_AP = LH_Data.sort_values(by=["AP"], ascending=False)
sorted_NA_AP = NA_Data.sort_values(by=["AP"], ascending=False)
sorted_PFC_AP = PFC_Data.sort_values(by=["AP"], ascending=False)

sorted_LH_ML = LH_Data.sort_values(by=["ML"], ascending=False)
sorted_NA_ML = NA_Data.sort_values(by=["ML"], ascending=False)
sorted_PFC_ML = PFC_Data.sort_values(by=["ML"], ascending=False)

sorted_LH_DV = LH_Data.sort_values(by=["DV"], ascending=False)
sorted_NA_DV = NA_Data.sort_values(by=["DV"], ascending=False)
sorted_PFC_DV = PFC_Data.sort_values(by=["DV"], ascending=False)


Cell_population_LH = (np.linspace(1, LH_Data.shape[0], LH_Data.shape[0]))/LH_Data.shape[0]  
Cell_population_NA = (np.linspace(1, NA_Data.shape[0], NA_Data.shape[0]))/NA_Data.shape[0] 
Cell_population_PFC = (np.linspace(1, PFC_Data.shape[0], PFC_Data.shape[0]))/ PFC_Data.shape[0]


plt.figure()

plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False


plt.subplot(1,3,1) 
plt.plot(sorted_LH_AP["AP"],
         Cell_population_LH, 
         color='#90EE90',
        )

plt.plot(sorted_NA_AP["AP"],
         Cell_population_NA,
         color='#800080',
        )

plt.plot(sorted_PFC_AP["AP"],
         Cell_population_PFC,
         color='#FFFF00',
         )
plt.xlabel("AP (mm)", size=10)
plt.ylabel("Cell Proportion", size=10)
plt.gca().set_box_aspect(1) 
plt.xlim(2, -5)
plt.ylim(0,1)
plt.xticks(np.linspace(2, -7, 4))
plt.yticks([0, 0.5, 1])
plt.legend(["LH","NA","PFC"], loc="upper left", fontsize=8, frameon=False)  

plt.subplot(1,3,2) 
plt.plot(sorted_LH_ML["ML"],
         Cell_population_LH, 
         color='#90EE90',
        )

plt.plot(sorted_NA_ML["ML"],
         Cell_population_NA,
         color='#800080',
        )

plt.plot(sorted_PFC_ML["ML"],
         Cell_population_PFC,
         color='#FFFF00',
         )
plt.xlabel("ML (mm)", size=10)
plt.ylabel("Cell Proportion", size=10)
plt.gca().set_box_aspect(1) 
plt.xlim(5, 0)
plt.ylim(0,1)
plt.xticks(np.linspace(4, 0, 3))
plt.yticks([0, 0.5, 1])

plt.subplot(1,3,3) 
plt.plot(sorted_LH_DV["DV"],
         Cell_population_LH, 
         color='#90EE90',
        )

plt.plot(sorted_NA_DV["DV"],
         Cell_population_NA,
         color='#800080',
        )

plt.plot(sorted_PFC_DV["DV"],
         Cell_population_PFC,
         color='#FFFF00',
         )

plt.xlabel("DV (mm)", size=10)
plt.ylabel("Cell Proportion", size=10)
plt.gca().set_box_aspect(1) 
plt.xlim(-1, -8)
plt.ylim(0,1)
plt.xticks(np.linspace(-2, -8, 3))
plt.yticks([0, 0.5, 1])


plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.tight_layout()


plt.show()
