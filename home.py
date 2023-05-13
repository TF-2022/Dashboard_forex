import streamlit as st

st.title("Dashboard Forex")
st.warning("Page en construction")


def main_home() :
    from app.home.theme import Theme_fond
    Theme_fond()

if __name__ == '__main__':
    main_home()