import streamlit as st
from utils.viz import line_chart

def show_overview(tables, min_year, max_year):
    st.header("Overview")
    
    with st.expander("About these metrics"):
        st.markdown("""
        **Key Performance Indicators (KPIs)**:
        - **Renewable Rate**: Percentage of electricity from renewable sources
        - **Electricity Price**: Average market price in €/MWh
        - **Renewable Production**: Total energy from wind, solar, hydro in TWh
        """)
    
    filtered_data = tables['timeseries'][
        (tables['timeseries']['annee'] >= min_year) & 
        (tables['timeseries']['annee'] <= max_year)
    ]
    
    if filtered_data.empty:
        st.warning("No data available for the selected period.")
        return
    
    avg_renewable_rate = filtered_data['taux_enr_pourcent'].mean()
    avg_price = filtered_data['prix_moyen_eur_mwh'].mean()
    
    start_data = tables['timeseries'][tables['timeseries']['annee'] == min_year]
    end_data = tables['timeseries'][tables['timeseries']['annee'] == max_year]
    
    if not start_data.empty and not end_data.empty:
        price_variation = end_data['prix_moyen_eur_mwh'].values[0] - start_data['prix_moyen_eur_mwh'].values[0]
        renewable_variation = end_data['taux_enr_pourcent'].values[0] - start_data['taux_enr_pourcent'].values[0]
    else:
        price_variation = 0
        renewable_variation = 0
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Average renewable rate",
            f"{avg_renewable_rate:.1f}%",
            f"{renewable_variation:+.1f}% vs {min_year}"
        )
    
    with col2:
        st.metric(
            "Average electricity price",
            f"{avg_price:.0f} €/MWh",
            f"{price_variation:+.0f} € vs {min_year}"
        )
    
    with col3:
        total_production = tables['raw_clean']['production_enr'].mean()
        st.metric(
            "Average renewable production",
            f"{total_production:.0f} TWh",
            "Wind + solar + hydro"
        )
    
    st.caption("""
    **Dual-axis Chart**: 
    - Left axis (green): Renewable energy rate as percentage of total production
    - Right axis (orange): Electricity market price in Euros per MWh
    """)
    
    st.plotly_chart(line_chart(filtered_data), use_container_width=True)
    
    st.info(
        f"**Key insight**: Between {min_year} and {max_year}, renewable rate increased by {renewable_variation:+.1f} points "
        f"while electricity price changed by {price_variation:+.0f} €/MWh."
    )