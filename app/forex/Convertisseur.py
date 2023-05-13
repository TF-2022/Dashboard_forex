import streamlit as st
import pandas as pd
import requests

from app.home.theme import Theme_fond
Theme_fond()


import re
import requests
import pandas as pd
import streamlit as st

def main_convertisseur():
    # read the country and currency code mapping into a pandas dataframe
    df = pd.read_csv("app/forex/csv/pays/pays_code_devise.csv")

    # define a selectbox for the user to choose the base currency
    with st.sidebar:
        base_currency = st.selectbox("Convertir", 
                             [f"{pays} ({devise})" for pays, devise in zip(df["pays"].unique(), df["devise"].unique())], 
                             index=df["devise"].unique().tolist().index("EUR"), key="eurusd")

    # extract the currency code from base_currency
    pattern = r'\((.*?)\)'
    matches = re.findall(pattern, base_currency)
    if len(matches) > 0:
        devise = matches[0]
    else:
        devise = ""

    # define a multiselect for the user to choose the quote currencies
    with st.sidebar:
        quote_currencies = st.multiselect("en", df["devise"].unique(), default=["USD"])

    # define the list of base amounts
    base_amounts = [50, 100, 500, 1000, 2000, 5000, 7000, 10000, 20000, 50000, 70000, 100000]

    # create a pandas dataframe with the exchange rate and converted amounts
    data = {"Montant de base": base_amounts}

    # loop through the selected quote currencies
    for quote_currency in quote_currencies:
        url = f"https://api.apilayer.com/exchangerates_data/latest?base={devise}&symbols={quote_currency}"
        headers = {"apikey": "1JsH6GngIdk25rmagvUtCQIh8MeZPU52"}
        response = requests.get(url, headers=headers)
        result = response.json()

        # get the exchange rate for the quote currency
        if "rates" in result and quote_currency in result["rates"]:
            rate = result["rates"][quote_currency]
            converted_amounts = [amount * rate for amount in base_amounts]
            data[f"{devise} to {quote_currency}"] = converted_amounts
        
        # add a column to the dataframe to show whether the base currency is greater or less than the quote currency
        if rate > 1:
            symbol = ">"
        else:
            symbol = "<"
        data[f"{base_currency} {symbol} {quote_currency}"] = [symbol if amount > 1/ rate else "" for amount in converted_amounts]

    df_result = pd.DataFrame(data)

    # display the result
    st.write(df_result)

if __name__ == '__main__':
    main_convertisseur()
