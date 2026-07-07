import pandas as pd
import streamlit as st

@st.cache_data(show_spinner="Loading data...")
def load_data():
    try:
        df_production = pd.read_csv('prod-national-annuel-filiere.csv', encoding='latin1', sep=';')
        df_production.columns = df_production.columns.str.replace('ï»¿', '', regex=False)
        
        df_production = df_production.rename(columns={
            'AnnÃ©e': 'annee',
            'Production Ã©olienne (TWh)': 'production_eolien',
            'Production solaire (TWh)': 'production_solaire',
            'Production hydraulique (TWh)': 'production_hydraulique',
            'Production totale (TWh)': 'production_totale'
        })
         
        df_parc = pd.read_csv('parc-national-annuel-prod-eolien-solaire.csv', encoding='latin1', sep=';')
        df_parc.columns = df_parc.columns.str.replace('ï»¿', '', regex=False)
        
        df_parc = df_parc.rename(columns={
            'Annee': 'annee',
            'Parc installÃ© Ã©olien (MW)': 'puissance_eolien_mw',
            'Parc installÃ© solaire (MW)': 'puissance_solaire_mw'
        })

        years = df_production['annee'].unique()

        price_data = {
            2013: 42.5, 2014: 44.2, 2015: 46.8, 2016: 48.1, 2017: 50.3,
            2018: 52.9, 2019: 55.2, 2020: 58.7, 2021: 65.5, 2022: 85.8
        }
        
        synthetic_prices = []
        for year in sorted(years):
            if year in price_data:
                synthetic_prices.append(price_data[year])
            else:
                base_price = 40 + (year - 2013) * 4
                synthetic_prices.append(base_price)
        
        df_price = pd.DataFrame({
            'annee': sorted(years),
            'prix_moyen_eur_mwh': synthetic_prices
        })
        
        df = pd.merge(df_production, df_price, on='annee', how='inner')
        df = pd.merge(df, df_parc, on='annee', how='inner')
        
        df['annee'] = df['annee'].astype(int)
        
        return df
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def get_license_text():
    return "Open Licence Version 2.0"