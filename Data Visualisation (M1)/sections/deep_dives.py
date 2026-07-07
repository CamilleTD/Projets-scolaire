import streamlit as st
from utils.viz import (scatter_chart, bar_chart, power_chart, small_multiples_chart,
                      seasonal_trend_chart, capacity_utilization_chart, 
                      price_distribution_chart, renewable_growth_heatmap,
                      cost_efficiency_chart, energy_mix_evolution_chart)

def show_deep_dives(tables, min_year, max_year):
    st.header("Deep Dive Analysis")
    

    with st.expander("Analysis Methods & Interpretation Guide"):
        st.markdown("""
        **Advanced Analytics Section**:
        
        **Relationship Analysis**:
        - Correlation analysis between renewable share and electricity prices
        - Price distribution and volatility patterns
        
        **Technical Performance**:
        - Capacity utilization rates (actual vs potential output)
        - Installed capacity growth tracking
        
        **Economic Analysis**:
        - Technology cost trends vs market prices
        - Seasonal price variations and patterns
        
        **Market Dynamics**:
        - Growth rates by technology type
        - Energy mix composition evolution
        
        **Note**: Some data is simulated for demonstration purposes.
        """)
    
    filtered_mix = tables['mix_enr'][
        (tables['mix_enr']['annee'] >= min_year) & 
        (tables['mix_enr']['annee'] <= max_year)
    ]
    
    filtered_corr = tables['correlation']
    
    filtered_power = tables['puissance_installee'][
        (tables['puissance_installee']['annee'] >= min_year) & 
        (tables['puissance_installee']['annee'] <= max_year)
    ]
    
    filtered_raw = tables['raw_clean'][
        (tables['raw_clean']['annee'] >= min_year) & 
        (tables['raw_clean']['annee'] <= max_year)
    ]

    st.subheader("Relationship between Renewable Energy and Prices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(scatter_chart(filtered_corr), use_container_width=True)
        correlation = filtered_corr['taux_enr_pourcent'].corr(filtered_corr['prix_moyen_eur_mwh'])
        st.metric("Correlation Coefficient", f"{correlation:.2f}")
        st.caption("**Interpretation**: Values close to +1 indicate strong positive correlation, close to -1 indicate negative correlation")
    
    with col2:
        st.plotly_chart(price_distribution_chart(filtered_raw), use_container_width=True)
        st.caption("**Box plot interpretation**: Shows price range, median, and outliers for each year")
    

    st.subheader("Technical Performance & Efficiency")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(capacity_utilization_chart(filtered_raw), use_container_width=True)
        st.caption("**Capacity factor**: Percentage of maximum potential output actually achieved")
    
    with col2:
        st.plotly_chart(power_chart(filtered_power), use_container_width=True)
        st.caption("**Installed capacity**: Maximum potential power output of energy facilities")
    

    st.subheader("Economic Analysis & Cost Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(cost_efficiency_chart(filtered_raw), use_container_width=True)
        st.caption("**Cost trends**: Estimated technology costs compared to market electricity prices")
    
    with col2:
        st.plotly_chart(seasonal_trend_chart(filtered_raw), use_container_width=True)
        st.caption("**Seasonal patterns**: Monthly price variations showing cyclical trends")
    
 
    st.subheader("Market Dynamics & Growth Patterns")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(renewable_growth_heatmap(filtered_raw), use_container_width=True)
        st.caption("**Growth heatmap**: Annual percentage growth rates by technology (green = positive, red = negative)")
    
    with col2:
        st.plotly_chart(energy_mix_evolution_chart(filtered_raw), use_container_width=True)
        st.caption("**Energy mix**: Evolution of electricity generation sources as percentage of total")
    

    st.subheader("Energy Composition & Mix Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(bar_chart(filtered_mix), use_container_width=True)
        st.caption("**Production composition**: Absolute energy production by renewable technology")
    
    with col2:
        st.plotly_chart(small_multiples_chart(filtered_raw), use_container_width=True)
        st.caption("**Small multiples**: Comparative view allowing easy pattern recognition across technologies")
    

    st.subheader("Performance Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        wind_growth = ((filtered_mix['production_eolien'].iloc[-1] - filtered_mix['production_eolien'].iloc[0]) / 
                      filtered_mix['production_eolien'].iloc[0] * 100)
        st.metric("Wind Growth", f"{wind_growth:+.1f}%")
    
    with col2:
        solar_growth = ((filtered_mix['production_solaire'].iloc[-1] - filtered_mix['production_solaire'].iloc[0]) / 
                       filtered_mix['production_solaire'].iloc[0] * 100)
        st.metric("Solar Growth", f"{solar_growth:+.1f}%")
    
    with col3:
        price_change = ((filtered_raw['prix_moyen_eur_mwh'].iloc[-1] - filtered_raw['prix_moyen_eur_mwh'].iloc[0]) / 
                       filtered_raw['prix_moyen_eur_mwh'].iloc[0] * 100)
        st.metric("Price Change", f"{price_change:+.1f}%")
    
    with col4:
        renewable_share_change = ((filtered_raw['taux_enr_pourcent'].iloc[-1] - filtered_raw['taux_enr_pourcent'].iloc[0]))
        st.metric("Renewable Share Δ", f"{renewable_share_change:+.1f} pts")