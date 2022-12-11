import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

st.markdown('# Analysis')


st.subheader('Here i would like to analyse the obtained data')
def drawplot(df, reason, color):
    fig = go.Figure()
    years = []
    deathsforreasons = []
    for o in range(1990, 2020):
        deathsforreasons.append(df[df['Year'] == o][reason].sum())
        years.append(o)
    fig = fig.add_trace(go.Scatter(x = years,
                                    y = deathsforreasons,
                                    line=dict(color=color, width=4)))
    st.plotly_chart(fig)


def showbar(dataframe, reasonwhy, color):
    years = []
    deathsforreasons = []
    for i in range(1990, 2020):
        deathsforreasons.append(dataframe[dataframe['Year'] == i][reasonwhy].sum())
        years.append(i)
    fig = px.bar(dataframe[reasonwhy], years, deathsforreasons, labels={'x':'Year', 'y':'Deaths'}, color_discrete_sequence = [color]*len(dataframe))
    st.plotly_chart(fig)
def showpie(df, when):
    names = []
    values = []
    for i in list(df)[3:-1]:
        names.append(i)
        values.append(df[df['Year'] == when][i].sum())
    fig = px.pie(df, values=values, names= names, labels={'names':'Reason', 'values':'Deaths'})
    st.plotly_chart(fig)



dfold = pd.read_csv('PythonProjectmilo/DataFiles/age-between-15-and-49.csv')
dfold = dfold.dropna()
dfold['Year'].astype('object')
dfold['Total deaths'] = dfold.sum(axis=1, numeric_only=True)
dfold = dfold.sort_values(by='Total deaths', ascending=False)
dfold = dfold[dfold['Country'].str.contains('World') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Lower Middle Income') == False]


dfyoung = pd.read_csv('PythonProjectmilo/DataFiles/age-between-5-and-14.csv')
dfyoung = dfyoung.dropna()
dfyoung['Year'].astype('object')
dfyoung['Total deaths'] = dfyoung.sum(axis=1, numeric_only=True)
dfyoung = dfyoung.sort_values(by='Total deaths', ascending=False)
dfyoung = dfyoung[dfyoung['Country'].str.contains('World') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Upper Middle Income') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Lower Middle Income') == False]

dftodlers = pd.read_csv('PythonProjectmilo/DataFiles/under-age-5.csv')
dftodlers = dftodlers.dropna()
dftodlers['Year'].astype('object')
dftodlers['Total deaths'] = dftodlers.sum(axis=1, numeric_only=True)
dftodlers = dftodlers.sort_values(by='Total deaths', ascending=False)
dftodlers = dftodlers[dftodlers['Country'].str.contains('World') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Upper Middle Income') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Lower Middle Income') == False]

dfveryold = pd.read_csv('PythonProjectmilo/DataFiles/age-between-50-and-69.csv')
dfveryold = dfveryold.dropna()
dfveryold['Year'].astype('object')
dfveryold['Total deaths'] = dfveryold.sum(axis=1, numeric_only=True)
dfveryold = dfveryold.sort_values(by='Total deaths', ascending=False)
dfveryold = dfveryold[dfveryold['Country'].str.contains('World') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Lower Middle Income') == False]

st.header('AIDS epidemic')
reasonwhy1 = 'HIV/AIDS'
st.subheader('In the 2000s, there was a fatal AIDS epidemic, so I assume that there will be a rise in graphs of deaths due to  HIV/AIDS of people aged 5 to 14 and 15 to 49.')
st.write('15-49 age group')
showbar(dfold, reasonwhy1, '#00CC96')
st.write('5-14 age group')
showbar(dfyoung, reasonwhy1, '#AB63FA')
st.subheader('Number of deaths on both graphs rise gradually until they reach their peak at 2005 for 15-49 age group and at 2004 for 5-14 age group. So my theory is proved.')
st.header('Self-Harm deaths throughout the years')
st.subheader('There also can be seen a significant change in self-harm deaths of both 15-49 and 5-14 age groups. It can be possibly explained by the fact that the psychological aid has become more widespread, so fewer persons commit suicide, because they seek help sooner.')
st.write('People of age from 5 to 14 that died from self-harm')
drawplot(dfyoung, 'Self-harm', 'pink')
st.write('People of age from 15 to 49 that died from self-harm')
drawplot(dfold, 'Self-harm', 'royalblue')
st.header('Deaths of kids under 5 years old')
st.subheader('The number of kids dying every year gradually decreases every year. I suppose that it is due to the development of medicine technologies and medical education.')
drawplot(dftodlers, 'Total deaths', 'lime')
