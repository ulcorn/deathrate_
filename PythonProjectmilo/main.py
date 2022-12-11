import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown('# Death Rate analysis (1990-2019)')

st.write('This statistics will examine main causes of death of people of different ages')

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

dfold = pd.read_csv('DataFiles/age-between-15-and-49.csv')
dfold = dfold.dropna()
dfold['Year'].astype('object')
dfold['total_deaths'] = dfold.sum(axis=1, numeric_only=True)
dfold = dfold.sort_values(by='total_deaths', ascending=False)
dfold = dfold[dfold['Country'].str.contains('World') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Lower Middle Income') == False]


dfyoung = pd.read_csv('DataFiles/age-between-5-and-14.csv')
dfyoung = dfyoung.dropna()
dfyoung['Year'].astype('object')
dfyoung['total_deaths'] = dfyoung.sum(axis=1, numeric_only=True)
dfyoung = dfyoung.sort_values(by='total_deaths', ascending=False)
dfyoung = dfyoung[dfyoung['Country'].str.contains('World') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Upper Middle Income') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Lower Middle Income') == False]

dftodlers = pd.read_csv('DataFiles/under-age-5.csv')
dftodlers = dftodlers.dropna()
dftodlers['Year'].astype('object')
dftodlers['total_deaths'] = dftodlers.sum(axis=1, numeric_only=True)
dftodlers = dftodlers.sort_values(by='total_deaths', ascending=False)
dftodlers = dftodlers[dftodlers['Country'].str.contains('World') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Upper Middle Income') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Lower Middle Income') == False]

dfveryold = pd.read_csv('DataFiles/age-between-50-and-69.csv')
dfveryold = dfveryold.dropna()
dfveryold['Year'].astype('object')
dfveryold['total_deaths'] = dfveryold.sum(axis=1, numeric_only=True)
dfveryold = dfveryold.sort_values(by='total_deaths', ascending=False)
dfveryold = dfveryold[dfveryold['Country'].str.contains('World') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Lower Middle Income') == False]

tab1, tab2, tab3, tab4, tab5= st.tabs(['People under age 5', 'People of age between 5 and 14','People of age between 15 and 49', 'People of age between 50 and 69', 'General Statistics' ])
with tab1:
    st.header('How many people people under age 5 died for different reasons')
    reasonwhy = st.selectbox('Reason', sorted(list(dftodlers)[3:]),key="orel")
    showbar(dftodlers, reasonwhy, '#0099C6')
    when = st.selectbox('Year', sorted(list(dftodlers['Year'].unique())),key="python")
    st.write('Stastistics of death on each year')
    showpie(dftodlers, when)
with tab2:
    st.header('How many people people people of age between 5 and 14 died for different reasons')
    reasonwhy = st.selectbox('Reason', sorted(list(dfyoung)[3:]),key="algosi")
    showbar(dfyoung, reasonwhy, 'plum')
    st.write('Stastistics of death on each year')
    when1 = st.selectbox('Year', sorted(list(dfyoung['Year'].unique())),key="matan")
    showpie(dfyoung, when1)
with tab3:
    st.header('How many people people of age between 15 and 49 died for different reasons')
    reasonwhy = st.selectbox('Reason', sorted(list(dfold)[3:]),key="plusi]")
    showbar(dfold, reasonwhy, '#17BECF')
    st.write('Stastistics of death on each year')
    when2 = st.selectbox('Year', sorted(list(dfold['Year'].unique())),key="diskru")
    showpie(dfold, when2)
with tab4:
    st.header('How many people people of age between 50 and 69 died for different reasons')
    reasonwhy = st.selectbox('Reason', sorted(list(dfveryold)[3:]),key="vse")
    showbar(dfveryold, reasonwhy, '#00CC96')
    st.write('Stastistics of death on each year')
    when3 = st.selectbox('Year', sorted(list(dfveryold['Year'].unique())),key="lynal")
    showpie(dfveryold, when3)
with tab5:
    st.write('Basic statistics of deaths of people under age 5')
    st.write(dftodlers.describe())
    st.write('Basic statistics of deaths of people of age between 5 and 14')
    st.write(dfyoung.describe())
    st.write('Basic statistics of deaths of people of age between 15 and 49')
    st.write(dfold.describe())
    st.write('Basic statistics of deaths of people of age between 50 and 69')
    st.write(dfveryold.describe())
