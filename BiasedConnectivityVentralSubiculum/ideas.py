# Load a dataset and use plotly to show 3d plots

import pandas as pd
import plotly.express as px


# Load the .csv file for TRIO
df_trio = pd.read_csv("PFC_TRIO_cellcounts.csv")

fig = px.scatter_3d(df_trio, x="AP", y="ML", z="DV", color="color", opacity=0.5)

fig["layout"].update(width=1200, height=800, autosize=False)
fig.update_traces(marker_size=3)

fig.show()
