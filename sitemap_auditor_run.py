#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import xmltodict
from cachecontrol import CacheControl
import time

# st.title('Sitemap Auditor')
# st.subheader('Audit the Sitemaps for Genetech.')

# file = st.file_uploader("Select your file.")

# if file is not None:
#     st.write("Your File is: ", file.name)
#     df=pd.read_excel(file)
#     df['Google_URL'] = 'https://www.google.com/search?q=' + df['Keyword'].str.replace(' ', '%20')
#     st.write(df)
# else:
#     st.warning('Please upload a file to get started.')
#     st.stop()
    
# st.write('Press continue to begin...')   
# run_it = st.button("Continue")

# improve performance if needed
sess = requests.session()
cached_sess = CacheControl(sess)

response = cached_sess.get('http://google.com')

sitemap_urls = pd.read_excel('C:/Users/Spencer Baselice/OneDrive - Relevate Health/Documents/SEO/SEO Tools/GNE Tools/Sitemaps/sitemap-urls.xlsx"sitemap-urls.xlsx')

sitemap_crawl_list = sitemap_urls.iloc[:, 0].to_list()

@st.cache_data
def header():
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-x-robots'
             }
    return header


## request the url in the list
data = []
connection_errors = []

@st.cache_data
def sitemap_crawl():
    for url in sitemap_crawl_list:
        time.sleep(1)
        st.write('Crawling URL: ' + str(url))
        f_data = {}
        try:    
            req = requests.get(url, headers=header)
            print(req.status_code)
            print(req.url)
            print(req.history)
            #location= req.headers['location']
            #print(location)
            f_data['Sitemap'] = req.url
            f_data['Status_Code'] = req.status_code
            #f_data['Redirect_chain'] = req.history
            f_data['Encoding'] = req.encoding
            #f_data['Last_Modified'] = req.headers['Last-Modified']
            #f_data['Redirect_URL'] = req.headers['Location']
            if 'X-Robots-Tag' in req.headers.keys():
                f_data['X_Robots_Tag']=req.headers['X-Robots-Tag']
            else:
                f_data['X_Robots_Tag']=None  
            #f_data['Redirects'] = redirect_chain
            # read thge xml in soup for each URL iteration
            # find localhost
            xml = req.text
            soup = BeautifulSoup(xml, 'xml')
            loc_tags = soup.find_all('loc')
            for tag in loc_tags:
                if 'https://localhost:' in tag.text:
                    f_data['localhost_found'] = 'Yes'
                else:
                    f_data['localhost_found'] = 'No'
                    # find CDATA
            if '<![CDATA' in xml:
                f_data['CDATA_found_in_loc'] = 'Yes'
                    #print('CDATA found.')
            else:
                f_data['CDATA_found_in_loc'] = 'No'
                    #print('CDATA not found.')
            data.append(f_data)
        except:
            print("URL:" + str(url) + ' had a connection error.')
            connection_errors.append(url)
            continue
      

    all_data = pd.DataFrame.from_dict(data)
    all_data.to_excel('sitemap-audit_1.xlsx')

sitemap_crawl()




