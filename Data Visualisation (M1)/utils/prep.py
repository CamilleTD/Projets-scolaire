import pandas as pd

def make_tables(df_raw):
    df_clean = df_raw.copy()
    
    df_clean['production_enr'] = (df_clean['production_eolien'] + 
                                df_clean['production_solaire'] + 
                                df_clean['production_hydraulique'])
    
    df_clean['taux_enr_pourcent'] = (df_clean['production_enr'] / 
                                   df_clean['production_totale'] * 100).round(1)
    
    timeseries = df_clean[['annee', 'taux_enr_pourcent', 'prix_moyen_eur_mwh']].copy()
    correlation = df_clean[['taux_enr_pourcent', 'prix_moyen_eur_mwh']].copy()
    mix_enr = df_clean[['annee', 'production_eolien', 'production_solaire', 
                       'production_hydraulique']].copy()
    puissance_installee = df_clean[['annee', 'puissance_eolien_mw', 'puissance_solaire_mw']].copy()
    
    tables = {
        'timeseries': timeseries,
        'correlation': correlation, 
        'mix_enr': mix_enr,
        'puissance_installee': puissance_installee,
        'raw_clean': df_clean
    }
    
    return tables

def validate_data(df):
    missing_data = df.isnull().sum()
    duplicates = df.duplicated().sum()
    
    validation_results = {
        'missing_values': missing_data.to_dict(),
        'duplicate_rows': int(duplicates),
        'years_range': {
            'min': int(df['annee'].min()),
            'max': int(df['annee'].max())
        },
        'data_points': len(df)
    }
    
    return validation_results