import streamlit as st
import pandas as pd
import plotly.express as px

# Custom CSS for mind-blowing design: Gradient background, modern fonts, shadows, and subtle animations
st.markdown("""
<style>
    .stApp {
        background-image: linear-gradient(to bottom right, #1e3c72, #2a5298);
        color: white;
    }
    h1, h2, h3 {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .stDataFrame {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #ffcc00;
        color: black;
        border-radius: 20px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ffd633;
        transform: scale(1.05);
    }
    .stSlider .st-dn {
        background-color: #ffcc00;
    }
</style>
""", unsafe_allow_html=True)

# Data from previous (oil reserves in billion barrels), expanded with oil production (kb/d) and gas reserves (tcm)
data = {
    'Country': [
        'Venezuela', 'Saudi Arabia', 'Iran', 'Iraq', 'Canada', 'United Arab Emirates', 'Kuwait', 'Russia', 
        'United States', 'Libya', 'Nigeria', 'Kazakhstan', 'Somalia', 'China', 'Qatar', 'Brazil', 
        'Algeria', 'Guyana', 'Ecuador', 'Norway', 'Angola', 'Azerbaijan', 'Mexico', 'Oman', 
        'India', 'Vietnam', 'South Sudan', 'Malaysia', 'Egypt', 'Yemen', 'Argentina', 'Congo', 
        'United Kingdom', 'Syria', 'Uganda', 'Indonesia', 'Australia', 'Suriname', 'Colombia', 
        'Gabon', 'Chad', 'Turkey', 'Sudan', 'Brunei', 'Equatorial Guinea', 'Peru', 'Ghana', 
        'Romania', 'Turkmenistan', 'Uzbekistan', 'Pakistan', 'Italy', 'Denmark', 'Tunisia', 
        'Ukraine', 'Thailand', 'Trinidad and Tobago', 'Bolivia', 'Cameroon', 'Belarus', 'Bahrain', 
        'DR Congo', 'Papua New Guinea', 'Albania', 'Chile', 'Niger', 'Spain', 'Myanmar', 
        'Philippines', 'Netherlands', 'Cuba', 'Germany', 'Poland', 'Ivory Coast', 'Guatemala', 
        'Serbia', 'Croatia', 'France', 'Japan', 'New Zealand', 'Kyrgyzstan', 'Austria', 'Georgia', 
        'Bangladesh', 'Mauritania', 'Bulgaria', 'Czech Republic', 'South Africa', 'Israel', 
        'Hungary', 'Lithuania', 'Tajikistan', 'Greece', 'Slovakia', 'Benin', 'Belize', 'Taiwan', 
        'Barbados', 'Jordan', 'Morocco'
    ],
    'Reserves': [
        304.0, 267.0, 209.0, 201.0, 170.0, 113.0, 102.0, 80.0, 74.0, 50.0, 37.0, 30.0, 30.0, 26.0, 
        25.0, 13.0, 12.0, 11.0, 8.3, 8.1, 7.8, 7.0, 6.0, 5.4, 4.6, 4.4, 3.8, 3.6, 3.3, 3.0, 3.0, 
        2.9, 2.5, 2.5, 2.5, 2.5, 2.4, 2.4, 2.0, 2.0, 1.5, 1.4, 1.3, 1.1, 1.1, 0.9, 0.7, 0.6, 0.6, 
        0.6, 0.5, 0.5, 0.4, 0.4, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 
        0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.086, 0.077, 0.071, 0.061, 0.044, 0.04, 0.04, 0.035, 
        0.035, 0.028, 0.02, 0.015, 0.015, 0.015, 0.012, 0.012, 0.012, 0.012, 0.01, 0.009, 0.008, 
        0.006, 0.002, 0.001, 0.001, 0.001
    ]
}
df = pd.DataFrame(data)

# Oil production data (kb/d, 2025)
oil_prod_dict = {
    'United States': 13870, 'Saudi Arabia': 10050, 'Russia': 9803, 'Canada': 5049, 'China': 4300,
    'Iraq': 4009, 'Brazil': 3894, 'United Arab Emirates': 3363, 'Iran': 3221, 'Kuwait': 2569,
    'Kazakhstan': 2147, 'Norway': 1974, 'Mexico': 1735, 'Nigeria': 1436, 'Libya': 1365,
    'Qatar': 1322, 'Venezuela': 1142, 'Oman': 1008, 'Algeria': 968, 'Argentina': 817,
    'Colombia': 750, 'India': 610, 'Indonesia': 596, 'Azerbaijan': 559, 'Malaysia': 542,
    'United Kingdom': 537, 'Egypt': 501, 'Ecuador': 468, 'Congo': 276, 'Australia': 233,
    'Gabon': 217, 'Turkmenistan': 191, 'Ghana': 182, 'Bahrain': 180, 'Vietnam': 173,
    'Thailand': 164, 'Chad': 126, 'Turkey': 122, 'Niger': 108, 'Brunei': 98,
    'Italy': 85, 'Syria': 85, 'Denmark': 75, 'Pakistan': 64, 'Ivory Coast': 62,
    'Cameroon': 59, 'Romania': 51, 'Trinidad and Tobago': 51, 'Peru': 44,
    'Equatorial Guinea': 41, 'Papua New Guinea': 31, 'Germany': 30, 'Sudan': 30,
    'Uzbekistan': 29, 'Belarus': 26, 'Cuba': 25, 'Tunisia': 24, 'Hungary': 22,
    'Netherlands': 21, 'Bolivia': 19, 'Poland': 17, 'DR Congo': 16, 'Israel': 15,
    'Yemen': 15, 'Mongolia': 14, 'Albania': 12, 'Suriname': 12, 'Serbia': 11
}
df['Oil_Production_kbd'] = df['Country'].map(oil_prod_dict).fillna(0)

# Natural gas reserves data (tcm, end-2024)
gas_res_dict = {
    'Canada': 2.462, 'Chile': 0.010, 'Mexico': 0.276, 'United States': 17.912, 'Denmark': 0.090,
    'Germany': 0.017, 'Italy': 0.047, 'Netherlands': 0.074, 'Norway': 1.890, 'Poland': 0.090,
    'United Kingdom': 0.161, 'Australia': 2.741, 'Japan': 0.022, 'New Zealand': 0.045,
    'China': 2.890, 'India': 1.145, 'Bangladesh': 0.186, 'Brunei': 0.217, 'Indonesia': 0.894,
    'Malaysia': 2.112, 'Myanmar': 0.217, 'Pakistan': 0.427, 'Thailand': 0.162, 'Vietnam': 0.174,
    'Argentina': 0.470, 'Bolivia': 0.175, 'Brazil': 0.628, 'Colombia': 0.054, 'Ecuador': 0.009,
    'Peru': 0.237, 'Trinidad and Tobago': 0.299, 'Venezuela': 5.511, 'Iran': 33.988,
    'Iraq': 3.714, 'Kuwait': 1.784, 'Oman': 0.644, 'Qatar': 23.831, 'Saudi Arabia': 9.727,
    'United Arab Emirates': 8.210, 'Algeria': 4.504, 'Angola': 0.129, 'Cameroon': 0.170,
    'Congo': 0.284, 'Egypt': 2.209, 'Equatorial Guinea': 0.040, 'Gabon': 0.027, 'Libya': 0.730,
    'Nigeria': 5.979, 'Russia': 46.832, 'Azerbaijan': 1.900, 'Kazakhstan': 1.830,
    'Turkmenistan': 13.900, 'Ukraine': 0.239, 'Uzbekistan': 0.846, 'Bulgaria': 0.004,
    'Romania': 0.080, 'Mozambique': 2.840  # Added as it's significant, even if not in original country list
}
df['Gas_Reserves_tcm'] = df['Country'].map(gas_res_dict).fillna(0)

# Fix country names for Plotly map compatibility
name_map = {
    'Congo': 'Republic of the Congo',
    'DR Congo': 'Democratic Republic of the Congo',
    'United States': 'United States of America',
    'United Kingdom': 'United Kingdom of Great Britain and Northern Ireland',
    'Vietnam': 'Viet Nam',
    'Iran': 'Iran (Islamic Republic of)',
    'Syria': 'Syrian Arab Republic',
    'Czech Republic': 'Czechia',
    'Taiwan': 'Taiwan (Province of China)',
    'Bolivia': 'Bolivia (Plurinational State of)',
    'Venezuela': 'Venezuela (Bolivarian Republic of)',
    'Russia': 'Russian Federation',
    'South Sudan': 'South Sudan',
    'Trinidad and Tobago': 'Trinidad and Tobago'
}
df['Country_for_map'] = df['Country'].replace(name_map)

# App Title
st.title('🌍 Global Energy Resources Explorer')

st.markdown('An enhanced interactive dashboard for exploring crude oil reserves, production, and natural gas reserves worldwide. Switch metrics on the map, compare countries, and more!')

# Sidebar for Filters
with st.sidebar:
    st.header('🛠️ Controls')
    min_value = st.slider('Min Value Filter (applies to selected metric)', 0.0, float(df[['Reserves', 'Oil_Production_kbd', 'Gas_Reserves_tcm']].max().max()), 0.0, step=0.1)
    search = st.text_input('🔍 Search Country')
    top_n = st.number_input('Top N for Charts', min_value=5, max_value=50, value=10)

# Filter Data
filtered_df = df.copy()
if search:
    filtered_df = filtered_df[filtered_df['Country'].str.contains(search, case=False)]

# Tabs for Organized Views
tab1, tab2, tab3, tab4 = st.tabs(['📋 Table', '🗺️ Map', '📊 Charts', '🔍 Stats & Compare'])

with tab1:
    st.subheader('Data Table')
    st.dataframe(filtered_df.sort_values('Reserves', ascending=False).style.format({
        'Reserves': '{:.2f}', 'Oil_Production_kbd': '{:.0f}', 'Gas_Reserves_tcm': '{:.3f}'
    }), use_container_width=True)
    st.download_button('📥 Download CSV', data=filtered_df.to_csv(index=False), file_name='energy_resources.csv', mime='text/csv')

with tab2:
    st.subheader('Interactive World Map')
    metric_options = {
        'Oil Reserves (billion barrels)': 'Reserves',
        'Oil Production (kb/d)': 'Oil_Production_kbd',
        'Natural Gas Reserves (tcm)': 'Gas_Reserves_tcm'
    }
    selected_metric = st.selectbox('Select Metric for Map', list(metric_options.keys()))
    color_col = metric_options[selected_metric]
    color_scale = 'YlOrRd' if 'Reserves' in selected_metric else 'Blues' if 'Production' in selected_metric else 'Greens'
    
    # Filter by min_value
    map_df = filtered_df[filtered_df[color_col] >= min_value]
    
    fig_map = px.choropleth(
        map_df,
        locations='Country_for_map',
        locationmode='country names',
        color=color_col,
        hover_name='Country',
        hover_data={'Reserves': ':.2f', 'Oil_Production_kbd': ':.0f', 'Gas_Reserves_tcm': ':.3f'},
        color_continuous_scale=color_scale,
        projection='natural earth',
        title=f'{selected_metric} by Country (Hover for Details)'
    )
    
    # Enhance with scatter overlay for top 10
    top_10 = map_df.nlargest(10, color_col)
    fig_map.add_scattergeo(
        locations=top_10['Country_for_map'],
        locationmode='country names',
        text=top_10['Country'],
        marker=dict(size=top_10[color_col] / top_10[color_col].max() * 20, color='red', symbol='circle'),
        hoverinfo='text'
    )
    
    fig_map.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0}, height=600,
        geo=dict(showframe=False, showcoastlines=True, projection_type='natural earth'),
        dragmode='zoom',  # Enhanced interactivity
        updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Reset Zoom', method='relayout', args=['geo.projection.scale', 1])])]
    )
    st.plotly_chart(fig_map, use_container_width=True)

with tab3:
    st.subheader('Bar Chart: Top N Countries')
    top_df = df.sort_values('Reserves', ascending=False).head(top_n)
    fig_bar = px.bar(top_df, x='Country', y=['Reserves', 'Oil_Production_kbd', 'Gas_Reserves_tcm'], barmode='group')
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.subheader('Pie Chart: Global Distribution (Oil Reserves)')
    pie_df = top_df.copy()
    others = df['Reserves'].sum() - top_df['Reserves'].sum()
    pie_df = pd.concat([pie_df, pd.DataFrame({'Country': ['Others'], 'Reserves': [others]})], ignore_index=True)
    fig_pie = px.pie(pie_df, values='Reserves', names='Country', hole=0.3)
    st.plotly_chart(fig_pie, use_container_width=True)

with tab4:
    st.subheader('Key Stats')
    st.metric('Total Oil Reserves', f"{df['Reserves'].sum():.0f} billion barrels")
    st.metric('Total Oil Production', f"{df['Oil_Production_kbd'].sum():.0f} kb/d")
    st.metric('Total Gas Reserves', f"{df['Gas_Reserves_tcm'].sum():.2f} tcm")
    st.metric('Countries with Data', len(df))
    
    st.subheader('Unique Comparison Tool')
    col1, col2 = st.columns(2)
    with col1:
        country1 = st.selectbox('Country 1', options=df['Country'])
    with col2:
        country2 = st.selectbox('Country 2', options=df['Country'], index=1)
    if country1 and country2:
        comp_df = df[df['Country'].isin([country1, country2])]
        fig_comp = px.bar(comp_df, x='Country', y=['Reserves', 'Oil_Production_kbd', 'Gas_Reserves_tcm'], barmode='group')
        st.plotly_chart(fig_comp, use_container_width=True)

# Fun Unique Feature: Celebration Button
if st.button('🎉 Celebrate Energy Insights!'):
    st.balloons()
    st.success('Exploration unlocked! Keep discovering.') 