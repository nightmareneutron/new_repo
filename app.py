import streamlit as st
from nsetools import Nse
import plotly.figure_factory as ff
from nsepy import get_history
from datetime import date




nse = Nse()

#this code is to get historical data
start=date(2000,1,1)
end=date.today()



#to install talib on heroku



#to install talib on heroku





#from here we will get the patterns








def history(stockName):
    st.header(symbols)
    stockData = get_history(symbol=stockName, start=start, end=end)
    #pattern_fun = getattr(talib, pattern)
    df = stockData
    st.dataframe(df)
    st.download_button("Download stock data", 
                       df.to_csv(),
                       mime='text/csv',
                       file_name=f'{stockName}.csv',
                       )
    pert = (df['Open']/df['Prev Close'])-1
    
    st.dataframe(pert)
    st.line_chart(pert)
     




#don't touch this
stock = nse.get_stock_codes()
symbols = st.selectbox('dashboard',(stock))

if (symbols):
    history(symbols)






#use this while selling stocks
#get_quote = nse.get_quote(stockName)
    #fd = pd.Series(get_quote)