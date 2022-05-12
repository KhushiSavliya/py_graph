import pandas as pd
import plotly.express as px
import kaleido

df = pd.read_csv('covid.csv')
values = df['Deaths']
names = df['Country'].tolist()

fig = px.pie(df, values=values, names=names, title="Covid analysis")
fig.write_image("images/fig1.png") #for this we need to install kaleido
