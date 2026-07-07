import streamlit as st
from utils.prep import validate_data

def show_conclusions(tables, min_year, max_year):
    st.header("Conclusions & Perspectives")
    
    with st.expander("Data Quality Assessment Methodology"):
        st.markdown("""
        **Data Quality Assessment**:
        - Validation checks for data completeness and consistency
        - Missing values analysis for reliability assessment
        - Period coverage verification for temporal analysis validity
        - Duplicate detection for data integrity
        """)
    
    st.markdown("### Data Quality Assessment")
    validation_results = validate_data(tables['raw_clean'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Data Validation Summary:**")
        st.write(f"• Analysis Period: {validation_results['years_range']['min']}-{validation_results['years_range']['max']}")
        st.write(f"• Total Data Points: {validation_results['data_points']:,}")
        st.write(f"• Duplicate Rows: {validation_results['duplicate_rows']}")
    
    with col2:
        st.write("**Data Completeness:**")
        total_missing = sum(validation_results['missing_values'].values())
        completeness_rate = ((len(tables['raw_clean']) - total_missing) / len(tables['raw_clean']) * 100)
        st.write(f"• Missing Values: {total_missing}")
        st.write(f"• Data Completeness: {completeness_rate:.1f}%")
    
    st.markdown("---")
    
    st.markdown("### Key Insights")
    
    insight_col1, insight_col2 = st.columns(2)
    
    with insight_col1:
        st.success("""
        **Renewable Growth Trend**
        - Consistent increase in renewable energy share
        - Significant growth in solar and wind capacity
        - Positive correlation with long-term price stability
        """)
    
    with insight_col2:
        st.warning("""
        **Market Dynamics**
        - Multiple factors influence electricity prices
        - Renewable energy is one component of the energy mix
        - Infrastructure and policy play crucial roles
        """)
    
    st.markdown("---")
    
    st.markdown("### Limitations & Considerations")
    
    st.info("""
    **Data Limitations:**
    - Nationally aggregated data (no regional breakdown)
    - Historical data may not reflect current market dynamics
    - Average prices may mask seasonal and regional variations
    
    **Methodological Notes:**
    - Correlation analysis does not imply causation
    - Energy markets are influenced by multiple external factors
    - Policy changes and global events significantly impact prices
    """)
    
    st.markdown("---")
    
    st.markdown("### Next Steps & Recommendations")
    
    st.success("""
    **For Further Analysis:**
    - Incorporate regional data for geographic comparisons
    - Add weather and seasonal factors to the model
    - Include non-renewable energy sources in the analysis
    - Analyze impact of specific energy policies
    
    **For Decision Makers:**
    - Consider long-term infrastructure investments
    - Balance renewable growth with grid stability
    - Monitor international energy market trends
    """)
    
    st.markdown("---")
    
    st.markdown("### Final Assessment")
    
    filtered_data = tables['timeseries'][
        (tables['timeseries']['annee'] >= min_year) & 
        (tables['timeseries']['annee'] <= max_year)
    ]
    
    if not filtered_data.empty:
        start_renewable = filtered_data['taux_enr_pourcent'].iloc[0]
        end_renewable = filtered_data['taux_enr_pourcent'].iloc[-1]
        renewable_change = end_renewable - start_renewable
        
        start_price = filtered_data['prix_moyen_eur_mwh'].iloc[0]
        end_price = filtered_data['prix_moyen_eur_mwh'].iloc[-1]
        price_change = end_price - start_price
        price_change_pct = (price_change / start_price) * 100
        
        final_col1, final_col2 = st.columns(2)
        
        with final_col1:
            st.metric(
                "Renewable Energy Progress",
                f"{end_renewable:.1f}%",
                f"{renewable_change:+.1f} points since {min_year}"
            )
        
        with final_col2:
            st.metric(
                "Price Evolution",
                f"{end_price:.0f} €/MWh", 
                f"{price_change_pct:+.1f}% since {min_year}"
            )
    
    st.markdown("---")
    
    st.markdown("### Data Sources & Attribution")
    
    st.caption("""
    **Primary Data Sources:**
    - Energy Production Data : data.gouv.fr 
    - Installed Capacity Data : data.gouv.fr 
    - Price Data : data.gouv.fr 
    
    **Methodology:**
    - Data analysis performed using Python, Pandas, and Streamlit
    - Visualizations created with Plotly
    """)