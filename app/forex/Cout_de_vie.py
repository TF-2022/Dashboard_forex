import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

def read_country_data():
    """
    Lit le fichier CSV avec le nom de colonne 'Pays'
    """
    df = pd.read_csv('app/forex/csv/pays/Pays_devise.csv')
    return df

def get_html_content(url):
    """
    Récupère le contenu HTML d'une URL donnée
    """
    response = requests.get(url)
    html_content = response.text
    return html_content


def get_summary_data(html_content, selected_country):
    """
    Extraire les informations du résumé sur le coût de la vie dans le pays
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    summary = soup.find('div', {'class': 'seeding-call table_color summary limit_size_ad_right padding_lower other_highlight_color'})
    if summary is None or not hasattr(summary, 'text'):
        st.write("Il n'y a pas beaucoup de données pour " + selected_country + ". Nous aimerions avoir plus de contributeurs pour une meilleure fiabilité des données.")
        return None
    else:
        summary_text = summary.text
        st.write(f"{summary_text}")
        return soup

def get_dataframes(soup):
    """
    Extraire les informations de la table "data_wide_table new_bar_table"
    """
    categories = {}
    current_category = None

    table = soup.find('table', {'class': 'data_wide_table new_bar_table'})
    rows = table.find_all('tr')

    for row in rows:
        # Si la ligne commence par une nouvelle catégorie
        if row.find('div', {'class': 'category_title'}):
            current_category = row.find('div', {'class': 'category_title'}).text.strip()
            categories[current_category] = pd.DataFrame(columns=['Indicator', 
                                                                 'Value', 
                                                                 "Moyenne"])
        # Sinon, si la ligne contient des données
        elif len(row.find_all('td')) == 3:
            cells = row.find_all('td')
            category = cells[2].text.strip()
            indicator = cells[0].text.strip()
            value = cells[1].text.strip()
            categories[current_category] = pd.concat([categories[current_category], 
                                                      pd.DataFrame({'Indicator': [indicator], 
                                                                    'Value': [value], 
                                                                    "Moyenne" : category})], 
                                                                    ignore_index=True)
    # Affichage des DataFrames par catégorie
    for category, df in categories.items():
        expander = st.expander(f"{category}")
        with expander:
            st.write(df)
            
    return categories

def display_data(selected_country, all_data):
    """
    Afficher le nom du pays et le dataframe avec toutes les informations
    """
    st.write(all_data)


###################################### MAIN
def main_comparaison_pouvoir_achat():
    df = read_country_data()
    selected_country = st.selectbox('Sélectionnez un pays', df['Pays'], key="country")
    country_url = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=' + selected_country
    html_content = get_html_content(country_url)
    soup = get_summary_data(html_content, selected_country)
    if soup:
        categories = get_dataframes(soup)
        all_data = pd.concat(categories.values())
        
        display_data(selected_country, all_data)

###################################### MAIN
def prix_recement_ajouter() :
    url = 'https://www.numbeo.com/cost-of-living/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', {'class': 'nice_items_container'})
    if items is not None:
        for item in items:
            text = item.text.strip() # supprimer les espaces inutiles au début et à la fin
            lines = text.split('\n') # diviser le texte en une liste de lignes
            for line in lines:
                st.write('- ' + line) # afficher chaque ligne en tant que liste à puce
                 
### MAIN *************************
def main_pouvoir_monnaie_achat() :
    tab1, tab2 = st.tabs(["Prix récemment ajouter", "Pouvoir d'achat"])
    with tab1 :
        prix_recement_ajouter()
        
    with tab2 :
        main_comparaison_pouvoir_achat()
        
if __name__ == '__main__':
    main_pouvoir_monnaie_achat()







#### POUR traduire dans le futur car API pas asser de requete 
def translate_text(text, to_lang):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": text,
        "source": "en",
        "target": to_lang
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "x-rapidapi-key": "97f08f3307msh88ec6b2b74dcddfp18dad4jsn04af1ceb0462",
        "x-rapidapi-host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()
#translated_line = translate_text(line, "fr") # traduire la ligne en français
#st.write(translated_line)



