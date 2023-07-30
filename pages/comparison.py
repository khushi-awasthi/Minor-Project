import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme

st.set_page_config(layout='wide')

def clean_visitors(data):
    if data:
        if isinstance(data, str):
            data = data.replace(' ','')
            return float(data)
        return data
    return np.nan

def number_converter(data):
    if isinstance(data, float):
        return data
    elif data:
        if '-' in data:
            return np.nan
        elif isinstance(data, str):
            data = data.replace(' ','')
            if data.strip().isnumeric():
                return int(data.strip())
            elif 'M' in data:
                data = float(data.replace("M",""))* 100000 
                return data
            elif 'K' in data:
                data = float(data.replace("K",""))* 100000
                return data
        else:
            return float(data)

# function to load the data only once
@st.cache_data()
def load_Web_Scraped_websites_data():
    df = pd.read_csv('datasets/Web_Scrapped_websites.csv',encoding='latin-1' )
    df['Avg_Daily_Visitors'] = df['Avg_Daily_Visitors'].apply(clean_visitors)
    df['Avg_Daily_Pageviews'] = df['Avg_Daily_Pageviews'].apply(clean_visitors)
    df['Facebook_likes'] = df['Facebook_likes'].apply(number_converter)
    df['Twitter_mentions'] = df['Twitter_mentions'].apply(number_converter)
    df['Google_pluses'] = df['Google_pluses'].apply(number_converter)
    df['LinkedIn_mentions'] = df['LinkedIn_mentions'].apply(number_converter)
    df['Pinterest_pins'] = df['Pinterest_pins'].apply(number_converter)
    df['StumbleUpon_views'] = df['StumbleUpon_views'].apply(number_converter)
    df['Traffic_Rank'] = df['Traffic_Rank'].apply(number_converter)
    return df

with st.spinner("loading dataset"):
    df = load_Web_Scraped_websites_data()

st.sidebar.header("Navigation")
if st.sidebar.checkbox("Show Web_Scraped_websites datasets"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df)

fig1 = px.scatter(df, 'Facebook_likes','Twitter_mentions',
                title='Facebook vs twitter comparison of a website',
                hover_name='Website')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(df, 'Google_pluses','LinkedIn_mentions',
                title='Google vs LinkedIn comparison of a website',
                hover_name='Website')
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(df, 'Traffic_Rank','Reach_Day',
                title='Traffic Rank vs Reach Day comparison of a website',
                hover_name='Website')
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.scatter(df, 'Pinterest_pins','StumbleUpon_views',
                title='Pinterest pins vs StumbleUpon views	 comparison on a website',
                hover_name='Website')
st.plotly_chart(fig4, use_container_width=True)

fig5 = px.scatter(df, 'Month_Average_Daily_Reach','Month_Average_Daily_Pageviews',
                title='Month Average Daily Reach vs Month Average Daily Pageviews comparison of a website',
                hover_name='Website')
st.plotly_chart(fig5, use_container_width=True)

fig6 = px.scatter(df, 'Daily_Pageviews','Daily_Pageviews_per_user',
                title='Daily Pageviews vs Daily Pageviews per user comparison of a website',
                hover_name='Website')
st.plotly_chart(fig6, use_container_width=True)

fig7 = px.scatter(df, 'Reach_Day_percentage','Month_Average_Daily_Reach_percentage',
                title='Reach Day percentage vs Month Average Daily Reach percentage comparison of a website',
                hover_name='Website')
st.plotly_chart(fig7, use_container_width=True)

fig8 = px.scatter(df, 'Daily_Pageviews_percentage','Month_Average_Daily_Pageviews_percentage',color='country',
                title='Daily Pageviews percentage vs Month Average Daily Pageviews percentage comparison of a website',
                hover_name='Website')
st.plotly_chart(fig8, use_container_width=True)




