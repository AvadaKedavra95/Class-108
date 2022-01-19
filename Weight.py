import csv
import pandas as pd
import plotly.figure_factory as ff

# with open("data.csv") as f:
#     reader=csv.reader(f)
#     weight_list=list(reader)
#     print(weight_list)
#     weight_list_df=weight_list[2]
df=pd.read_csv("data.csv")


fig=ff.create_distplot([df["Weight"].tolist()],["Weight"])
fig.show()