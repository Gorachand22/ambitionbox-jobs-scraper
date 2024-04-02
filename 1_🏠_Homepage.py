'''This the Home page fow web scrapping'''
from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st
import time

if 'logo' not in st.session_state:
    st.session_state['logo'] = []
if 'title' not in st.session_state:
    st.session_state['title'] = []
if 'company' not in st.session_state:
    st.session_state['company'] = []
if 'rating' not in st.session_state:
    st.session_state['rating'] = []
if 'experience' not in st.session_state:
    st.session_state['experience'] = []
if 'location' not in st.session_state:
    st.session_state['location'] = []
if 'skills' not in st.session_state:
    st.session_state['skills'] = []
if 'query' not in st.session_state:
    st.session_state['query'] = None

if 'dataframe' not in st.session_state:
    st.session_state['dataframe'] = None

logo = st.session_state['logo']
title = st.session_state['title']
company = st.session_state['company']
rating = st.session_state['rating']
experience = st.session_state['experience']
location = st.session_state['location']
skills = st.session_state['skills']
query = st.session_state['query']

st.set_page_config(page_title="AmbitionBox", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="auto")
st.subheader("Welcome to AmbitionBox Jobs Scrapper")

st.link_button("Go to website", "https://www.ambitionbox.com/")

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

with st.sidebar:
    var = st.text_input("Search for a job")
    query = var
    if st.button("Scrap"):
        try:
            webpage=requests.get(f'https://www.ambitionbox.com/jobs/search?tag={query}&page=1', headers=headers).text
            soup = BeautifulSoup(webpage, 'lxml')
        except:
            st.error("Something went wrong. Try another keyword")
        else:
            try:
                number = int(soup.find('h1', class_ = "container jobs-h1 bold-title-l").text.strip().split('\n')[0].replace(',',''))
                page_num = None
                if number%10 == 0:
                    page_num = number//10
                else:
                    page_num = number//10+1
                
            except:
                page_num = 0

            if page_num > 0:    
                st.write(f"**{page_num}** Jobs found with **{query}**")
                for i in range(1, page_num+1):
                    webpage=requests.get(f'https://www.ambitionbox.com/jobs/search?tag={query}&page={i}', headers=headers).text
                    soup1 = BeautifulSoup(webpage, 'lxml')
                    page1 = soup1.find_all("div", class_ = "jobsInfoCardCont")

                
                    # logo
                    for i in page1:
                        try:
                            logo.append(i.find("img",class_="logo").get("src"))
                        except:
                            logo.append('NaN')

                    # title
                    for i in page1:
                        try:
                            title.append(i.find("a", class_ = "title noclick").text)
                        except:
                            title.append('NaN')        
                    
                    # company name
                    for i in page1:
                        try:
                            company.append(i.find("p", class_ = "company body-medium").text.strip())
                        except:
                            company.append('NaN')
                    
                    # rating
                    for i in page1:
                        try:
                            rating.append(i.find("span", class_ = "body-small").text.strip())
                        except:
                            rating.append('NaN')
                    
                    # experience
                    for i in page1:
                        try:
                            experience.append(i.find_all("p", class_ = "body-small-l")[0].text.strip())
                        except:
                            experience.append('NaN')
                    
                    # location
                    for i in page1:
                        try:
                            location.append(i.find("div",class_="entity loc").text.strip())
                        except:
                            location.append('NaN')
                        
                    # skills
                    for i in page1:
                        try:
                            skills.append(i.find_all("p", class_ = "body-small-l")[-1].text.strip())
                        except:
                            skills.append('NaN')
                with st.spinner('Wait for it...'):
                        time.sleep(5)
                        st.success('Done!')
                df = pd.DataFrame({"logo":logo,'title':title, 'company':company, 'rating':rating, 'experience':experience, 'location':location, 'skills':skills})
                st.session_state['dataframe'] = df
                st.session_state['dataframe']["skills"]=st.session_state['dataframe']["skills"].str.replace("\n","").str.replace("\t"," ",1).str.replace("\t","")
                st.session_state['dataframe']['rating'] = st.session_state['dataframe']['rating'].fillna(0)
                st.session_state['dataframe']['rating'] = st.session_state['dataframe']['rating'].astype(float)
            else:
                st.write(f"No Jobs found with **{query}**")



if st.session_state['dataframe'] is not None:
    dataframe = st.session_state['dataframe']
    if dataframe is not None:
        st.data_editor(
            dataframe,
            column_config={
                "logo": st.column_config.ImageColumn(
                    "Preview Image", help="Company Logo"
                ),
                "rating": st.column_config.NumberColumn(
                                    "Jobs rating",
                                    help="Showing Jobs Rating",
                                    min_value=1,
                                    max_value=5,
                                    step=0.1,
                                    format="%.1f ⭐",
        ),
            },
            hide_index=True,
        )

        st.download_button(
            label="Download data as CSV",
            data = dataframe.to_csv(index=False).encode('utf-8'),
            file_name=f'{query} job.csv',
            mime='text/csv',
        )
                
            