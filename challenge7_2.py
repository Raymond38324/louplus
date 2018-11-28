import pandas as pd
import matplotlib.pyplot as plt
def co2_gdp_plot():
    data=pd.read_excel('ClimateChange.xlsx')
    data=data.set_index("Country code")
    data_co2=data[data['Series code']=="EN.ATM.CO2E.KT"]
    data_gdp=data[data['Series code']=="NY.GDP.MKTP.CD"]
    data_co2=data_co2.replace({"..":pd.np.nan})
    data_gdp=data_gdp.replace({"..":pd.np.nan})
    data_co2=data_co2.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data_gdp=data_gdp.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data_gdp.dropna()
    data_co2.dropna()
    co2=pd.concat([data_co2["Country name"],data_co2.sum(axis=1)],axis=1)
    gdp=pd.concat([data_gdp["Country name"],data_gdp.sum(axis=1)],axis=1)
    co2_1 = (co2[0]-co2.min()[0])/(co2.max()[0]-co2.min()[0])
    gdp_1 = (gdp[0]-gdp.min()[0])/(gdp.max()[0]-gdp.min()[0])
    num = list(map(lambda x:list(co2_1).index(co2_1[x]),['CHN', 'USA', 'GBR', 'FRA','RUS']))
    fig=plt.subplot()
    fig.plot(list(co2_1),color='b',label='CO2-SUM')
    fig.plot(list(gdp_1),color='r',label='GDP-SUM')
    fig.legend(loc='upper left')
    fig.set_xlabel("Countries")
    fig.set_ylabel("Values")
    fig.set_title("GDP-CO2")
    plt.xticks(num,['CHN', 'USA', 'GBR', 'FRA','RUS'], rotation=90)
    plt.show()
    c=float(format(co2_1['CHN'],'.3f'))
    g=float(format(gdp_1['CHN'],'.3f'))
    china = [c,g]
    return fig,china

print(co2_gdp_plot())
