import streamlit as st
from utils.io import load_data
from utils.prep import make_tables
from sections.intro import show_intro
from sections.overview import show_overview
from sections.deep_dives import show_deep_dives
from sections.conclusions import show_conclusions

st.set_page_config(
    page_title="Renewable Energy vs Prices",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data(show_spinner=False)
def get_data():
    df_raw = load_data()

    if df_raw.empty:
        st.error("No data available. Please check your data files.")
        st.stop()
    tables = make_tables(df_raw)
    return df_raw, tables

st.title("Renewable Energy Adoption vs Energy Prices")
st.caption("Source : data.gouv.fr")


try:
    raw_data, tables = get_data()
    min_year = int(tables['raw_clean']['annee'].min())
    max_year = int(tables['raw_clean']['annee'].max())
    
    with st.sidebar:
        st.header("Filters")
        
        year_min, year_max = st.slider(
            "Analysis Period",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year)
        )
        
        st.markdown("---")
        st.markdown("**Navigation**")
        page = st.radio("Sections", [
            "Introduction", 
            "Overview", 
            "Detailed Analysis", 
            "Conclusions"
        ])
    

    if page == "Introduction":
        show_intro()
    elif page == "Overview":
        show_overview(tables, year_min, year_max)
    elif page == "Detailed Analysis":
        show_deep_dives(tables, year_min, year_max)
    elif page == "Conclusions":
        show_conclusions(tables, year_min, year_max)

except Exception as e:
    st.error(f"Unable to load application: {e}")

st.markdown("---")
st.caption("© Camille Tura--Durand - Data Visualisation EFREI 2025-2026")