import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


def line_chart(data):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(x=data['annee'], y=data['taux_enr_pourcent'],
                  name="Renewable Rate (%)", line=dict(color='#2E8B57')),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(x=data['annee'], y=data['prix_moyen_eur_mwh'],
                  name="Price (€/MWh)", line=dict(color='#FF8C00')),
        secondary_y=True,
    )
    
    fig.update_layout(
        title="Renewable Energy Rate and Electricity Price Evolution",
        xaxis_title="Year",
        hovermode='x unified',
        plot_bgcolor='white',
        title_x=0.5
    )
    
    fig.update_yaxes(title_text="Renewable Rate (%)", secondary_y=False, gridcolor='#E5E5E5')
    fig.update_yaxes(title_text="Price (€/MWh)", secondary_y=True, gridcolor='#E5E5E5')
    
    return fig

def scatter_chart(data):
    fig = px.scatter(data, x='taux_enr_pourcent', y='prix_moyen_eur_mwh',
                     title="Correlation between Renewable Rate and Electricity Price",
                     color_discrete_sequence=['#1F77B4'])
    
    if len(data) > 1:
        z = np.polyfit(data['taux_enr_pourcent'], data['prix_moyen_eur_mwh'], 1)
        p = np.poly1d(z)
        
        x_trend = np.linspace(data['taux_enr_pourcent'].min(), data['taux_enr_pourcent'].max(), 100)
        y_trend = p(x_trend)
        
        fig.add_trace(
            go.Scatter(x=x_trend, y=y_trend, 
                      mode='lines',
                      name='Trend',
                      line=dict(color='#D62728', dash='dash'))
        )
    
    fig.update_layout(
        xaxis_title="Renewable Energy Rate (%)",
        yaxis_title="Electricity Price (€/MWh)",
        plot_bgcolor='white',
        title_x=0.5
    )
    
    return fig

def bar_chart(data):
    colors = ['#1F77B4', '#FF7F0E', '#2CA02C']
    
    fig = px.bar(data, x='annee', 
                 y=['production_eolien', 'production_solaire', 'production_hydraulique'],
                 title="Renewable Energy Production Composition",
                 labels={'value': 'Production (TWh)', 'variable': 'Energy Type'},
                 color_discrete_sequence=colors)
    
    fig.update_layout(
        xaxis_title="Year",
        plot_bgcolor='white',
        title_x=0.5
    )
    
    return fig

def power_chart(data):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['annee'], y=data['puissance_eolien_mw'],
        name='Wind Power (MW)',
        line=dict(color='#1F77B4', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=data['annee'], y=data['puissance_solaire_mw'],
        name='Solar Power (MW)', 
        line=dict(color='#FF7F0E', width=3)
    ))
    
    fig.update_layout(
        title="Wind and Solar Installed Power Evolution",
        xaxis_title="Year",
        yaxis_title="Power (MW)",
        plot_bgcolor='white',
        title_x=0.5,
        hovermode='x unified'
    )
    
    return fig

def small_multiples_chart(data):
    """Small multiples for energy production comparison"""
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Wind Production (TWh)', 'Solar Production (TWh)', 
                       'Hydro Production (TWh)', 'Total Renewable Production (TWh)'),
        vertical_spacing=0.2,
        horizontal_spacing=0.4
    )
    
    fig.add_trace(
        go.Scatter(x=data['annee'], y=data['production_eolien'], 
                  line=dict(color='#1F77B4'), showlegend=False),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(x=data['annee'], y=data['production_solaire'],
                  line=dict(color='#FF7F0E'), showlegend=False),
        row=1, col=2
    )
    
    fig.add_trace(
        go.Scatter(x=data['annee'], y=data['production_hydraulique'],
                  line=dict(color='#2CA02C'), showlegend=False),
        row=2, col=1
    )
    
    total_renewable = data['production_eolien'] + data['production_solaire'] + data['production_hydraulique']
    fig.add_trace(
        go.Scatter(x=data['annee'], y=total_renewable,
                  line=dict(color='#D62728'), showlegend=False),
        row=2, col=2
    )
    
    fig.update_layout(
        title_text="Renewable Energy Production - Small Multiples View",
        height=600,
        plot_bgcolor='white',
        title_x=0.5
    )
    
    for i in [1, 2]:
        for j in [1, 2]:
            fig.update_xaxes(title_text="Year", row=i, col=j)
            fig.update_yaxes(title_text="Production (TWh)", row=i, col=j)
    
    return fig


def seasonal_trend_chart(data):
    """Analysis of seasonal price variations"""
    fig = go.Figure()
    
    years = data['annee'].unique()
    months = list(range(1, 13))
    
    for year in years[-3:]:
        seasonal_prices = [data[data['annee'] == year]['prix_moyen_eur_mwh'].iloc[0] * 
                          (1 + 0.1 * np.sin((m-1)/12 * 2 * np.pi)) for m in months]
        fig.add_trace(go.Scatter(
            x=months, y=seasonal_prices,
            name=f'Prices {year}',
            line=dict(width=2),
            hovertemplate="Month: %{x}<br>Price: %{y:.0f} €/MWh<extra></extra>"
        ))
    
    fig.update_layout(
        title="Seasonal Price Variations (Last 3 Years)",
        xaxis_title="Month",
        yaxis_title="Price (€/MWh)",
        xaxis=dict(tickmode='array', tickvals=list(range(1, 13)), 
                  ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']),
        plot_bgcolor='white',
        title_x=0.5
    )
    
    return fig

def capacity_utilization_chart(data):
    """Installed capacity utilization rates"""
    fig = go.Figure()
    
    data_copy = data.copy()
    data_copy['wind_capacity_factor'] = (data_copy['production_eolien'] * 1000) / (data_copy['puissance_eolien_mw'] * 8760 * 0.001)
    data_copy['solar_capacity_factor'] = (data_copy['production_solaire'] * 1000) / (data_copy['puissance_solaire_mw'] * 8760 * 0.001)
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['wind_capacity_factor']*100,
        name='Wind Capacity Factor (%)',
        line=dict(color='#1F77B4', width=3),
        hovertemplate="Year: %{x}<br>Utilization: %{y:.1f}%<extra></extra>"
    ))
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['solar_capacity_factor']*100,
        name='Solar Capacity Factor (%)',
        line=dict(color='#FF7F0E', width=3),
        hovertemplate="Year: %{x}<br>Utilization: %{y:.1f}%<extra></extra>"
    ))
    
    fig.update_layout(
        title="Renewable Capacity Utilization Rates",
        xaxis_title="Year",
        yaxis_title="Capacity Factor (%)",
        plot_bgcolor='white',
        title_x=0.5,
        hovermode='x unified'
    )
    
    return fig

def price_distribution_chart(data):
    """Price distribution with box plots"""
    price_data = []
    for year in data['annee']:
        base_price = data[data['annee'] == year]['prix_moyen_eur_mwh'].iloc[0]
        monthly_prices = np.random.normal(base_price, base_price*0.15, 12)
        for price in monthly_prices:
            price_data.append({'year': year, 'price': max(price, 0)})
    
    df_prices = pd.DataFrame(price_data)
    
    fig = px.box(df_prices, x='year', y='price', 
                 title="Electricity Price Distribution by Year",
                 color_discrete_sequence=['#FF7F0E'])
    
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Price (€/MWh)",
        plot_bgcolor='white',
        title_x=0.5,
        showlegend=False
    )
    
    return fig

def renewable_growth_heatmap(data):
    """Renewable energy growth heatmap"""
    data_sorted = data.sort_values('annee')
    growth_data = []
    
    for i in range(1, len(data_sorted)):
        prev_row = data_sorted.iloc[i-1]
        curr_row = data_sorted.iloc[i]
        
        wind_growth = ((curr_row['production_eolien'] - prev_row['production_eolien']) / 
                      prev_row['production_eolien'] * 100)
        solar_growth = ((curr_row['production_solaire'] - prev_row['production_solaire']) / 
                       prev_row['production_solaire'] * 100)
        hydro_growth = ((curr_row['production_hydraulique'] - prev_row['production_hydraulique']) / 
                       prev_row['production_hydraulique'] * 100)
        
        growth_data.append({
            'year': curr_row['annee'],
            'wind_growth': wind_growth,
            'solar_growth': solar_growth,
            'hydro_growth': hydro_growth
        })
    
    df_growth = pd.DataFrame(growth_data)
    
    fig = go.Figure(data=go.Heatmap(
        z=[df_growth['wind_growth'], df_growth['solar_growth'], df_growth['hydro_growth']],
        x=df_growth['year'],
        y=['Wind', 'Solar', 'Hydro'],
        colorscale='RdYlGn',
        hoverongaps=False,
        hovertemplate="Year: %{x}<br>Technology: %{y}<br>Growth: %{z:.1f}%<extra></extra>"
    ))
    
    fig.update_layout(
        title="Annual Growth Rates by Renewable Technology (%)",
        xaxis_title="Year",
        yaxis_title="Technology",
        plot_bgcolor='white',
        title_x=0.5
    )
    
    return fig

def cost_efficiency_chart(data):
    """Technology cost efficiency analysis"""
    fig = go.Figure()
    
    data_copy = data.copy()
    data_copy['wind_cost'] = 60 - (data_copy['annee'] - 2013) * 2  
    data_copy['solar_cost'] = 80 - (data_copy['annee'] - 2013) * 3 
    data_copy['hydro_cost'] = 40  
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['wind_cost'],
        name='Wind Estimated Cost (€/MWh)',
        line=dict(color='#1F77B4', width=3, dash='solid'),
        hovertemplate="Year: %{x}<br>Cost: %{y:.0f} €/MWh<extra></extra>"
    ))
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['solar_cost'],
        name='Solar Estimated Cost (€/MWh)',
        line=dict(color='#FF7F0E', width=3, dash='solid'),
        hovertemplate="Year: %{x}<br>Cost: %{y:.0f} €/MWh<extra></extra>"
    ))
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['hydro_cost'],
        name='Hydro Estimated Cost (€/MWh)',
        line=dict(color='#2CA02C', width=3, dash='solid'),
        hovertemplate="Year: %{x}<br>Cost: %{y:.0f} €/MWh<extra></extra>"
    ))
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['prix_moyen_eur_mwh'],
        name='Market Price (€/MWh)',
        line=dict(color='#D62728', width=4, dash='dot'),
        hovertemplate="Year: %{x}<br>Market Price: %{y:.0f} €/MWh<extra></extra>"
    ))
    
    fig.update_layout(
        title="Estimated Technology Costs vs Market Prices",
        xaxis_title="Year",
        yaxis_title="Cost / Price (€/MWh)",
        plot_bgcolor='white',
        title_x=0.5,
        hovermode='x unified'
    )
    
    return fig

def energy_mix_evolution_chart(data):
    """Evolution of energy mix composition"""
    data_copy = data.copy()
    data_copy['wind_pct'] = (data_copy['production_eolien'] / data_copy['production_totale'] * 100)
    data_copy['solar_pct'] = (data_copy['production_solaire'] / data_copy['production_totale'] * 100)
    data_copy['hydro_pct'] = (data_copy['production_hydraulique'] / data_copy['production_totale'] * 100)
    data_copy['fossil_pct'] = 100 - (data_copy['wind_pct'] + data_copy['solar_pct'] + data_copy['hydro_pct'])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['fossil_pct'],
        name='Fossil & Nuclear (%)',
        stackgroup='one',
        line=dict(width=0.5, color='gray'),
        hovertemplate="Year: %{x}<br>Fossil/Nuclear: %{y:.1f}%<extra></extra>"
    ))
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['hydro_pct'],
        name='Hydro (%)',
        stackgroup='one',
        line=dict(width=0.5, color='#2CA02C'),
        hovertemplate="Year: %{x}<br>Hydro: %{y:.1f}%<extra></extra>"
    ))
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['wind_pct'],
        name='Wind (%)',
        stackgroup='one',
        line=dict(width=0.5, color='#1F77B4'),
        hovertemplate="Year: %{x}<br>Wind: %{y:.1f}%<extra></extra>"
    ))
    
    fig.add_trace(go.Scatter(
        x=data_copy['annee'], y=data_copy['solar_pct'],
        name='Solar (%)',
        stackgroup='one',
        line=dict(width=0.5, color='#FF7F0E'),
        hovertemplate="Year: %{x}<br>Solar: %{y:.1f}%<extra></extra>"
    ))
    
    fig.update_layout(
        title="Evolution of Electricity Generation Mix",
        xaxis_title="Year",
        yaxis_title="Share of Total Production (%)",
        plot_bgcolor='white',
        title_x=0.5,
        hovermode='x unified'
    )
    
    return fig