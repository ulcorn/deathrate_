import pandas as pd
import streamlit as st

st.markdown('# Analysis')

st.header('Analysis of the statistics')

st.write('Here i would like to analyse the obtained data')

from main import showbar
from main import showpie

dfold = pd.read_csv('PythonProject/age-between-15-and-49.csv')
dfold = dfold.dropna()
dfold['Year'].astype('object')
dfold['total_deaths'] = dfold.sum(axis=1, numeric_only=True)
dfold = dfold.sort_values(by='total_deaths', ascending=False)
dfold.head()
dfold = dfold[dfold['Country'].str.contains('World') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Lower Middle Income') == False]
dfold.head()


dfyoung = pd.read_csv('PythonProject/age-between-5-and-14.csv')
dfyoung = dfyoung.dropna()
dfyoung['Year'].astype('object')
dfyoung['total_deaths'] = dfyoung.sum(axis=1, numeric_only=True)
dfyoung = dfyoung.sort_values(by='total_deaths', ascending=False)
dfyoung.head()
dfyoung = dfyoung[dfyoung['Country'].str.contains('World') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Upper Middle Income') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Lower Middle Income') == False]

dftodlers = pd.read_csv('PythonProject/under-age-5.csv')
dftodlers = dftodlers.dropna()
dftodlers['Year'].astype('object')
dftodlers['total_deaths'] = dftodlers.sum(axis=1, numeric_only=True)
dftodlers = dftodlers.sort_values(by='total_deaths', ascending=False)
dftodlers.head()
dftodlers = dftodlers[dftodlers['Country'].str.contains('World') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Upper Middle Income') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Lower Middle Income') == False]

dfveryold = pd.read_csv('PythonProject/age-between-50-and-69.csv')
dfveryold = dfveryold.dropna()
dfveryold['Year'].astype('object')
dfveryold['total_deaths'] = dfveryold.sum(axis=1, numeric_only=True)
dfveryold = dfveryold.sort_values(by='total_deaths', ascending=False)
dfveryold.head()
dfveryold = dfveryold[dfveryold['Country'].str.contains('World') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Lower Middle Income') == False]


st.header('AIDS epidemic')
reasonwhy = 'HIV/AIDS'
st.write('There was a pandemic')
showbar(dfold, reasonwhy, '#00CC96')
showbar(dfyoung, reasonwhy, '#AB63FA')
st.write('Stastistics of death on each year')
reasonwhy1 = 'Drowning'
showbar(dfyoung, reasonwhy1, '#AB63FA')