import random
import plotly.express as px
import plotly.figure_factory as ff
count=[]
dice_result=[]
for x in range(1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(x)

fig=ff.create_distplot([dice_result],["Result"])
fig.show()

