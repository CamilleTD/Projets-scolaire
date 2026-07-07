# Renewable Energy vs Electricity Prices Dashboard
An interactive data storytelling dashboard analyzing the relationship between renewable energy adoption and electricity prices in France. By Camille Tura--Durand

## Project Overview
Does increasing renewable energy share lower or raise electricity prices for French households?
The data come from https://www.data.gouv.fr/pages/donnees-energie

### Installation
```bash
pip install -r requirements.txt
streamlit run app.py

#### PROJECT STRUCTURE
Project/ 
├── app.py                 
├── requirements.txt      
├── sections/             
│   ├── intro.py          
│   ├── overview.py       
│   ├── deep_dives.py     
│   └── conclusions.py    
├── utils/                
│   ├── io.py            
│   ├── prep.py          
│   └── viz.py           
└── data/                
    ├── Niveaux_prix_TRVG.csv
    ├── prod-national-annuel-filiere.csv
    └── parc-national-annuel-prod-eolien-solaire.csv