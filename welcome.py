import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme


st.set_page_config(layout='wide')


st.image("https://colibriwp.com/blog/wp-content/uploads/2018/07/banner-redimensionat.jpg", use_column_width=True)
st.title("WEBSITE DASHBOARD ANALYSIS")

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
rows,cols = df.shape
st.subheader('Analysis of Data')
total_Avg_Daily_Visitors = df['Avg_Daily_Visitors'].sum()
c1,c2= st.columns(2)
c1.metric('Total Records', rows)
c2.metric("Daily average visitors in all website", int(total_Avg_Daily_Visitors))    

trust_count = df['Trustworthiness'].value_counts()
fig1 = px.pie(trust_count, trust_count.index, trust_count.values, title="Percentage of Trustwothy websites")
st.plotly_chart(fig1, use_container_width=True)
st.warning("63% websites are trustworthy and can be considered safe")

Privacy_count = df['Privacy'].value_counts()
fig2 = px.pie(Privacy_count, Privacy_count.index, Privacy_count.values, title="Percentage of Privacy websites")
st.plotly_chart(fig2, use_container_width=True)
st.warning("63% websites are maintain Privacy")

Status_count = df['Status'].value_counts()
fig3 = px.pie(Status_count, Status_count.index, Status_count.values, title="Percentage of Status websites")
st.plotly_chart(fig3, use_container_width=True)
st.warning("99%  websites Status")

Location_count = df['Location'].value_counts().head(10)
fig4 = px.pie(Location_count, Location_count.index, Location_count.values, title="Top 10 locations")
st.plotly_chart(fig4, use_container_width=True)
st.warning("77%  websites Location in United States")

# Subnetworks_count = df['Subnetworks'].value_counts().head(10)
# fig5 = px.pie(Subnetworks_count,Subnetworks_count.index, Subnetworks_count.values, title="Percentage of Subnetworks")
# st.plotly_chart(fig5, use_container_width=True)
# st.warning("66%  websites Subnetwork")

Registrant_count = df['Registrant'].value_counts().head(10)
fig6 = px.pie(Location_count, Location_count.index, Location_count.values, title="Percentage of Registrant websites")
st.plotly_chart(fig6, use_container_width=True)
st.warning("77%  Registrant of websites ")

Registrar_count = df['Registrar'].value_counts().head(10)
fig7 = px.pie(Registrar_count, Registrar_count.index, Registrar_count.values, title="Percentage of Registrar websites")
st.plotly_chart(fig7, use_container_width=True)
st.warning("44% Registrar of  websites ")


