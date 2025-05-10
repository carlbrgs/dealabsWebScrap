import streamlit as st
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas as pd
import os

# Fonction pour exécuter le spider
def run_spider():
    # Supprimer les anciens résultats s'ils existent
    if os.path.exists("results.json"):
        os.remove("results.json")

    # Configurer et exécuter le spider
    process = CrawlerProcess(get_project_settings())
    process.crawl("dealabs")  # Nom du spider
    process.start()

    # Charger les résultats dans un DataFrame
    if os.path.exists("results.json"):
        return pd.read_json("results.json")
    else:
        return pd.DataFrame()

# Interface Streamlit
st.title("Suivi des Offres Dealabs")

# Barre de recherche
search = st.text_input("Rechercher un produit")

if st.button("Lancer la recherche"):
    st.write("Scraping en cours...")
    df = run_spider()  # Lancer le spider et récupérer les données

    if not df.empty:
        # Filtrer les résultats par recherche
        filtered_df = df[df['product_name'].str.contains(search, case=False, na=False)]

        if not filtered_df.empty:
            st.write(f"Résultats pour '{search}':")
            st.dataframe(filtered_df[['product_name', 'price', 'merchant', 'link']])

            # Sélectionner un produit pour afficher les détails
            selected_product = st.selectbox("Sélectionnez un produit pour voir les détails", filtered_df['product_name'])
            if selected_product:
                product_details = filtered_df[filtered_df['product_name'] == selected_product].iloc[0]
                st.subheader("Détails du produit")
                st.write(f"**Nom**: {product_details['product_name']}")
                st.write(f"**Prix**: {product_details['price']}")
                st.write(f"**Prix original**: {product_details['original_price']}")
                st.write(f"**Réduction**: {product_details['discount']}")
                st.write(f"**Marchand**: {product_details['merchant']}")
                st.write(f"**Date de publication**: {product_details['date_posted']}")
                st.write(f"**Votes**: {product_details['votes']}")
                st.write(f"**Commentaires**: {product_details['comments']}")
                st.write(f"[Lien vers l'offre]({product_details['link']})")
        else:
            st.write("Aucun produit trouvé.")
    else:
        st.write("Aucune donnée récupérée.")