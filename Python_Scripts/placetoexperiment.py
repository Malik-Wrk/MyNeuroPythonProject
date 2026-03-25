import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



PFC_colour="#FFDB6E"
NA_colour="#BF43CC"
LH_colour="#87FFE1"

AllData = pd.read_csv("BiasedConnectivityVentralSubiculum/coronal_CTBLabelled_dataset.csv")

subset_LH = AllData[AllData.Projection == "LH"]
subset_NA = AllData[AllData.Projection == "NAc"]
subset_PFC = AllData[AllData.Projection == "PFC"]


fig = px.scatter_3d(subset_LH,x="AP", y="ML", z="DV", opacity=0.5,)
fig.update_traces(marker=dict(color=LH_colour, size=2), name="LH", showlegend=True)


fig.add_trace(
    go.Scatter3d(x=subset_NA["AP"], y=subset_NA["ML"], z=subset_NA["DV"], 
    mode="markers", 
    marker={"color": NA_colour, "size": 2}, 
    opacity=0.5, 
    name="NA")
)

fig.add_trace(
    go.Scatter3d(x=subset_PFC["AP"], y=subset_PFC["ML"], z=subset_PFC["DV"], 
    mode="markers", 
    marker={"color": PFC_colour, "size": 2}, 
    opacity=0.5, 
    name="PFC")
)

fig["layout"].update(width=1000, height=600, autosize=False)

fig.update_scenes(aspectmode="data")

fig.update_legends(font_size=15)

fig.show()