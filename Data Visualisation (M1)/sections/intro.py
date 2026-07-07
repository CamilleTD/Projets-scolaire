import streamlit as st

def show_intro():
    st.header("Context and Problem")
    
    st.markdown("""
    ### Why is this topic important?
    The transition to renewable energy is central to energy policies, 
    but its impact on electricity prices remains a major concern.
    
    ### Key Question
    **Does increasing the share of renewable energy lower or raise 
    electricity prices for French households?**
    
    ### Target Audience
    - Citizens concerned about energy transition
    - Policy makers
    - Energy sector stakeholders
    """)
    

    with st.expander("Key Definitions & Methods"):
        st.markdown("""
        **Renewable Energy Rate**: Percentage of total electricity production coming from renewable sources (wind, solar, hydro).
        
        **Correlation Analysis**: Statistical method measuring the relationship between two variables. 
        Correlation does not imply causation.
        
        **Data Sources**: data.gouv.fr.
        
        **Methodology**: 
        - Data cleaning and validation
        - Time series analysis
        - Correlation calculations
        - Interactive visualization
        """)
    
