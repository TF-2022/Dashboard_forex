import streamlit as st
from app.home.theme import Theme_fond
Theme_fond()

from app.home.theme import Theme_fond

Theme_fond()
##################################################

st.write("test")
# TAUX INTERET---------------------------------------------------------------------------------------------------------------------------

choix_currency = [ "Accueil", 
                  "Convertisseur", 
                  "Cout de la vie"]

choix = st.sidebar.selectbox("Choisir", 
                            choix_currency, key= "convert")


def main_forex() :
    if "Accueil" in choix :
        st.title("Acceuil")

    elif "Convertisseur" in choix :
        from app.forex.Convertisseur import main_convertisseur
        main_convertisseur()

    elif "Cout de la vie" in choix :
        from app.forex.Cout_de_vie import main_pouvoir_monnaie_achat
        main_pouvoir_monnaie_achat()

if __name__ == '__main__':
    main_forex()

