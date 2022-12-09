import pandas as pd
import plotly.express as px

def showbar(dataframe, reasonwhy):
    years = []
    deathsforreasons = []
    for i in range(1990, 2020):
        deathsforreasons.append(dataframe[dataframe['Year'] == i][reasonwhy].sum())
        years.append(i)
    fig = px.bar(dataframe[reasonwhy], years, deathsforreasons, labels={'x':'Year', 'y':'Deaths'})
    fig.show()
def showpie(df, when):
    names = []
    values = []
    for i in list(df)[3:-1]:
        names.append(i)
        values.append(df[df['Year'] == when][i].sum())
    fig = px.pie(df, values=values, names= names, labels={'names':'Reason', 'values':'Deaths'})
    fig.show()


dfold = pd.read_csv('age-between-15-and-49.csv')
dfold = dfold.dropna()
dfold['Year'].astype('object')
dfold['total_deaths'] = dfold.sum(axis=1, numeric_only=True)
dfold = dfold.sort_values(by='total_deaths', ascending=False)
dfold.head()
dfold = dfold[dfold['Country'].str.contains('World') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfold = dfold[dfold['Country'].str.contains('World Bank Lower Middle Income') == False]
dfold.head()


dfyoung = pd.read_csv('age-between-5-and-14.csv')
dfyoung = dfyoung.dropna()
dfyoung['Year'].astype('object')
dfyoung['total_deaths'] = dfyoung.sum(axis=1, numeric_only=True)
dfyoung = dfyoung.sort_values(by='total_deaths', ascending=False)
dfyoung.head()
dfyoung = dfyoung[dfyoung['Country'].str.contains('World') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Upper Middle Income') == False]
dfyoung = dfyoung[dfyoung['Country'].str.contains('World Bank Lower Middle Income') == False]

dftodlers = pd.read_csv('under-age-5.csv')
dftodlers = dftodlers.dropna()
dftodlers['Year'].astype('object')
dftodlers['total_deaths'] = dftodlers.sum(axis=1, numeric_only=True)
dftodlers = dftodlers.sort_values(by='total_deaths', ascending=False)
dftodlers.head()
dftodlers = dftodlers[dftodlers['Country'].str.contains('World') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Upper Middle Income') == False]
dftodlers = dftodlers[dftodlers['Country'].str.contains('World Bank Lower Middle Income') == False]

dfveryold = pd.read_csv('under-age-5.csv')
dfveryold = dfveryold.dropna()
dfveryold['Year'].astype('object')
dfveryold['total_deaths'] = dfveryold.sum(axis=1, numeric_only=True)
dfveryold = dfveryold.sort_values(by='total_deaths', ascending=False)
dfveryold.head()
dfveryold = dfveryold[dfveryold['Country'].str.contains('World') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Upper Middle Income') == False]
dfveryold = dfveryold[dfveryold['Country'].str.contains('World Bank Lower Middle Income') == False]

reasonwhy = 'total_deaths' #по по же
showbar(dftodlers, reasonwhy)
showbar(dfyoung, reasonwhy)
showbar(dfold, reasonwhy)
showbar(dfveryold, reasonwhy)

when = 2019
showpie(dftodlers, when)
showpie(dfyoung, when)
showpie(dfold, when)
showpie(dfveryold, when)

