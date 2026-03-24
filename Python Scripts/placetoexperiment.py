import matplotlib as plt 
import pandas as pd
import plotly.express as px

Lateral_Thalamus_cellcounts = pd.read_csv('LH_TRIO_cellcounts.csv')

Nucleus_accumbens_cellcounts = pd.read.csv('NAc_TRIO_cellcounts.csv')

Prefrontal_Cortex_cellcounts = pd.read.csv('PRC_TRIO_cellcounts.csv')

PFC_colour="#FFDB6E"
NA_colour="#BF43CC"
LH_colour="#87FFE1"


df["projection"] = "LH"
df2["projection"] = "NA"
df3["projection"] = "PFC"

subset_LH = df[df.projection == "LH"]
subset_NA = df2[df2.projection == "NA"]
subset_PFC = df3[df3.projection == "PFC"]

merged_DF=pd.concat([df, df2, df3], ignore_index=True)

fig = px.scatter_3d(subset_LH,x="AP", y="DV", z="AP", marker={"size": 2, "color": LH_colour, "opacity": 0.7}, name='LH')

fig.add_scatter3d(x=subset_NA["AP"], y=subset_NA["DV"], z=subset_NA["AP"], mode='markers', marker={"size": 2, "color": NA_colour, "opacity": 0.7}, name='NAc')

fig.add_scatter3d(x=subset_PFC["AP"], y=subset_PFC["DV"], z=subset_PFC["AP"], mode='markers', marker={"size": 2, "color": PFC_colour, "opacity": 0.7}, name='PFC')