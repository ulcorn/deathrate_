import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

st.markdown('# Analysis')


st.write('Here i would like to analyse the obtained data')

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



dfold = pd.read_csv('PythonProject/age-between-15-and-49.csv')
dfold = dfold.dropna()
dfold['Year'].astype('object')
dfold['total_deaths'] = dfold.sum(axis=1, numeric_only=True)
dfold = dfold.sort_values(by='total_deaths', ascending=False)
dfold = dfold[dfold['Country'].str.contains('World') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Lower Middle Income') == False]


dfyoung = pd.read_csv('PythonProject/age-between-5-and-14.csv')
dfyoung = dfyoung.dropna()
dfyoung['Year'].astype('object')
dfyoung['total_deaths'] = dfyoung.sum(axis=1, numeric_only=True)
dfyoung = dfyoung.sort_values(by='total_deaths', ascending=False)
dfyoung = dfyoung[dfyoung['Country'].str.contains('World') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Upper Middle Income') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Lower Middle Income') == False]

dftodlers = pd.read_csv('PythonProject/under-age-5.csv')
dftodlers = dftodlers.dropna()
dftodlers['Year'].astype('object')
dftodlers['total_deaths'] = dftodlers.sum(axis=1, numeric_only=True)
dftodlers = dftodlers.sort_values(by='total_deaths', ascending=False)
dftodlers = dftodlers[dftodlers['Country'].str.contains('World') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Upper Middle Income') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Lower Middle Income') == False]

dfveryold = pd.read_csv('PythonProject/age-between-50-and-69.csv')
dfveryold = dfveryold.dropna()
dfveryold['Year'].astype('object')
dfveryold['total_deaths'] = dfveryold.sum(axis=1, numeric_only=True)
dfveryold = dfveryold.sort_values(by='total_deaths', ascending=False)
dfveryold = dfveryold[dfveryold['Country'].str.contains('World') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Lower Middle Income') == False]


st.header('AIDS epidemic')
reasonwhy1 = 'HIV/AIDS'
st.header('In the 2000s, there was a fatal AIDS pandemic, which can be seen in death graphs of people aged 5 to 14 and 15 to 49.')
st.write('15-49 age group')
showbar(dfold, reasonwhy1, '#00CC96')
st.write('5-14 age group')
showbar(dfyoung, reasonwhy1, '#AB63FA')
st.header('According to my theory, as psychological aid has become more widespread, fewer persons commit suicide by harming themselves because they seek help sooner.')
st.write('People of age from 5 to 14 that died from self-harm')

# dict for the dataframes and their names
dfs = {"15-49" : dfold, "5-14": dfyoung}

def drawplot(df, reason):
    fig = go.Figure()
    years = []
    deathsforreasons = []
    for o in range(1990, 2020):
        deathsforreasons.append(df[df['Year'] == o][reason].sum())
        years.append(o)
    fig = fig.add_trace(go.Scatter(x = years,
                                    y = deathsforreasons,
                                    line=dict(color='pink', width=4, dash='dot')))
    st.plotly_chart(fig)
drawplot(dfold, 'Self-harm')
drawplot(dfyoung, 'Self-harm')
st.write('Since the numbers were lower at the beginning, my idea cannot be supported by figures of children aged 5 to 14, but there has been a noticeable difference in fatalities among persons aged 15 to 49, with almost 100k people having died from suicides being prevented. (')
# def showbar(dataframe, reasonwhy, color):
#     years = []
#     deathsforreasons = []
#     for i in range(1990, 2020):
#         deathsforreasons.append(dataframe[dataframe['Year'] == i][reasonwhy].sum())
#         years.append(i)
#     fig = px.bar(dataframe[reasonwhy], years, deathsforreasons, labels={'x':'Year', 'y':'Deaths'}, color_discrete_sequence = [color]*len(dataframe))
#     st.plotly_chart(fig)
# showbar(dfyoung, 'Self-harm', '#EEA6FB')
# st.write('People of age from 15 to 49 that died from self-harm')
# showbar(dfold, 'Self-harm', '#EEA6FB')
# st.write('My hypothesis can be clearly proved by the statistics of people from 5 to 14, but the number of people dying from self-harm aged 15 to 49 have remained approx. the same, so my theory is partially true.')
#

