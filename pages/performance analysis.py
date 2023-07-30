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

st.subheader("Website performance analysis")
web_df = df.groupby('Website')['Avg_Daily_Visitors'].sum().reset_index()
web_df = web_df.sort_values('Avg_Daily_Visitors', ascending=False)
fig9 = px.bar(web_df.head(25), 'Website', 'Avg_Daily_Visitors', title="Number of visitors on website")
fig9a = px.violin(web_df, 'Avg_Daily_Visitors', hover_name='Website')
c1, c2 = st.columns(2)
c1.plotly_chart(fig9, use_container_width=True)
c2.plotly_chart(fig9a, use_container_width=True)
st.info("Google.com has the maximum number of visitors in the world")

web_df = df.groupby('Website')['Facebook_likes'].sum().reset_index()
web_df = web_df.sort_values('Facebook_likes', ascending=False)
fig10 = px.bar(web_df.head(10), 'Website', 'Facebook_likes', title="Number of facebook like for website")
fig10a = px.violin(web_df,'Facebook_likes',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig10, use_container_width=True)
c2.plotly_chart(fig10a, use_container_width=True)
st.info(" Google.com has maximum Facebook likes")

web_df = df.groupby('Website')['Twitter_mentions'].sum().reset_index()
web_df = web_df.sort_values('Twitter_mentions', ascending=False)
fig11 = px.bar(web_df.head(10), 'Website', 'Twitter_mentions', title="Number of twitter mentions for website")
fig11a = px.violin(web_df,'Twitter_mentions',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig11, use_container_width=True)
c2.plotly_chart(fig11a, use_container_width=True)
st.info('Wordpress.com has the maximum Twitter mentions')

web_df = df.groupby('Website')['Google_pluses'].sum().reset_index()
web_df = web_df.sort_values('Google_pluses', ascending=False)
fig12 = px.bar(web_df.head(10), 'Website', 'Google_pluses', title="Number of Google pluses for website")
fig12a = px.violin(web_df,'Google_pluses',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig12, use_container_width=True)
c2.plotly_chart(fig12a, use_container_width=True)
st.info('Yahoo.com has more Google_pluses')

web_df = df.groupby('Website')['LinkedIn_mentions'].sum().reset_index()
web_df = web_df.sort_values('LinkedIn_mentions', ascending=False)
fig13 = px.bar(web_df.head(10), 'Website', 'LinkedIn_mentions', title="Number of Linkedin mentions for website")
fig13a = px.violin(web_df,'LinkedIn_mentions',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig13, use_container_width=True)
c2.plotly_chart(fig13a, use_container_width=True)
st.info('Linkedin.com more LinkedIn_mentions')

web_df = df.groupby('Website')['Pinterest_pins'].sum().reset_index()
web_df = web_df.sort_values('Pinterest_pins', ascending=False)
fig14 = px.bar(web_df.head(10), 'Website', 'Pinterest_pins', title="Number of Pinterestpins for website")
fig14a = px.violin(web_df,'Pinterest_pins',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig14, use_container_width=True)
c2.plotly_chart(fig14a, use_container_width=True)
st.info('tumblr.com has more Pinterest_pins')

web_df = df.groupby('Website')['StumbleUpon_views'].sum().reset_index()
web_df = web_df.sort_values('StumbleUpon_views', ascending=False)
fig15 = px.bar(web_df.head(10), 'Website', 'StumbleUpon_views', title="StumbleUpon views Pinterestpins for website")
fig15a = px.violin(web_df,'StumbleUpon_views',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig15, use_container_width=True)
c2.plotly_chart(fig15a, use_container_width=True)
st.info('Youtube.com has more StumbleUpon_views')

web_df = df.groupby('Website')['Reach_Day'].sum().reset_index()
web_df = web_df.sort_values('Reach_Day', ascending=False)
fig16 = px.bar(web_df.head(10), 'Website', 'Reach_Day', title="Reach Day on website")
fig16a = px.violin(web_df,'Reach_Day',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig16, use_container_width=True)
c2.plotly_chart(fig16a, use_container_width=True)
st.info('More Reach_Day on youtube.com')

web_df = df.groupby('Website')['Traffic_Rank'].sum().reset_index()
web_df = web_df.sort_values('Traffic_Rank', ascending=False)
fig17 = px.bar(web_df.head(10), 'Website', 'Traffic_Rank', title="Traffic Rank on website")
fig17a = px.violin(web_df,'Traffic_Rank',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig17, use_container_width=True)
c2.plotly_chart(fig17a, use_container_width=True)
st.info('More Traffic_Rank on catfly.ph')

web_df = df.groupby('Website')['Month_Average_Daily_Reach'].sum().reset_index()
web_df = web_df.sort_values('Month_Average_Daily_Reach', ascending=False)
fig18 = px.bar(web_df.head(10), 'Website', 'Month_Average_Daily_Reach', title="Month_Average_Daily_Reach on website")
fig18a = px.violin(web_df,'Month_Average_Daily_Reach',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig18, use_container_width=True)
c2.plotly_chart(fig18a, use_container_width=True)
st.info('google.com has more Month_Average_Daily_Reach')

web_df = df.groupby('Website')['Daily_Pageviews'].sum().reset_index()
web_df = web_df.sort_values('Daily_Pageviews', ascending=False)
fig19 = px.bar(web_df.head(10), 'Website', 'Daily_Pageviews', title="Daily_Pageviews on website")
fig19a = px.violin(web_df,'Daily_Pageviews',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig19, use_container_width=True)
c2.plotly_chart(fig19a, use_container_width=True)
st.info('google.com has maximum Daily_Pageviews')

web_df = df.groupby('Website')['Month_Average_Daily_Pageviews'].sum().reset_index()
web_df = web_df.sort_values('Month_Average_Daily_Pageviews', ascending=False)
fig20 = px.bar(web_df.head(10), 'Website', 'Month_Average_Daily_Pageviews', title="Month_Average_Daily_Pageviews on website")
fig20a = px.violin(web_df,'Month_Average_Daily_Pageviews',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig20, use_container_width=True)
c2.plotly_chart(fig20a, use_container_width=True)
st.info('google.com has maximum Month_Average_Daily_Pageviews')

web_df = df.groupby('Website')['Daily_Pageviews_per_user'].sum().reset_index()
web_df = web_df.sort_values('Daily_Pageviews_per_user', ascending=False)
fig21 = px.bar(web_df.head(10), 'Website', 'Daily_Pageviews_per_user', title="Daily_Pageviews_per_user on website")
fig21a = px.violin(web_df,'Daily_Pageviews_per_user',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig21, use_container_width=True)
c2.plotly_chart(fig21a, use_container_width=True)
st.info('google.com has maximum Daily_Pageviews_per_user')

web_df = df.groupby('Website')['Reach_Day_percentage'].sum().reset_index()
web_df = web_df.sort_values('Reach_Day_percentage', ascending=False)
fig22 = px.bar(web_df.head(10), 'Website', 'Reach_Day_percentage', title="Reach_Day_percentage on website")
fig22a = px.violin(web_df,'Reach_Day_percentage',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig22, use_container_width=True)
c2.plotly_chart(fig22a, use_container_width=True)
st.info('finacle-lp.com has maximum Reach_Day_percentage')

web_df = df.groupby('Website')['Month_Average_Daily_Reach_percentage'].sum().reset_index()
web_df = web_df.sort_values('Month_Average_Daily_Reach_percentage', ascending=False)
fig23 = px.bar(web_df.head(10), 'Website', 'Month_Average_Daily_Reach_percentage', title="Month_Average_Daily_Reach_percentage on website")
fig23a = px.violin(web_df,'Month_Average_Daily_Reach_percentage',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig23, use_container_width=True)
c2.plotly_chart(fig23a, use_container_width=True)
st.info('xicalsssadmission.gov.bd has max Month_Average_Daily_Reach_percentage')

web_df = df.groupby('Website')['Daily_Pageviews_percentage'].sum().reset_index()
web_df = web_df.sort_values('Daily_Pageviews_percentage', ascending=False)
fig24 = px.bar(web_df.head(10), 'Website', 'Daily_Pageviews_percentage', title="Daily_Pageviews_percentage on website")
fig24a = px.violin(web_df,'Daily_Pageviews_percentage',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig24, use_container_width=True)
c2.plotly_chart(fig24a, use_container_width=True)
st.info('finacle-lp.com has maximum Daily_Pageviews_percentage')

web_df = df.groupby('Website')['Month_Average_Daily_Pageviews_percentage'].sum().reset_index()
web_df = web_df.sort_values('Month_Average_Daily_Pageviews_percentage', ascending=False)
fig25 = px.bar(web_df.head(25), 'Website', 'Month_Average_Daily_Pageviews_percentage', title="Month_Average_Daily_Pageviews_percentage on website")
fig25a = px.violin(web_df,'Month_Average_Daily_Pageviews_percentage',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig25, use_container_width=True)
c2.plotly_chart(fig25a, use_container_width=True)
st.info('maximum Month_Average_Daily_Pageviews_percentage on xiclassadmission.gov.bd')

web_df = df.groupby('Website')['Daily_Pageviews_per_user_percentage'].sum().reset_index()
web_df = web_df.sort_values('Daily_Pageviews_per_user_percentage', ascending=False)
fig26 = px.bar(web_df.head(10), 'Website', 'Daily_Pageviews_per_user_percentage', title="Daily_Pageviews_per_user_percentage on website")
fig26a = px.violin(web_df,'Daily_Pageviews_per_user_percentage',hover_name='Website')
c1,c2 = st.columns(2)
c1.plotly_chart(fig26, use_container_width=True)
c2.plotly_chart(fig26a, use_container_width=True)
st.info('Maximum Daily_Pageviews_per_user_percentage on google.com')