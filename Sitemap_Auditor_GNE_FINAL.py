#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import gzip
import xmltodict
from cachecontrol import CacheControl
import time


# In[2]:


# improve performance if needed
sess = requests.session()
cached_sess = CacheControl(sess)

response = cached_sess.get('http://google.com')

sitemap_urls = pd.read_excel('sitemap-urls.xlsx')

sitemap_crawl_list = sitemap_urls.iloc[:, 0].to_list()

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
         'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-x-robots'
          }


# In[3]:


## request the url in the list
data = []
connection_errors = []

for url in sitemap_crawl_list:
    time.sleep(1)
    print('URL: ' + str(url))
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

## Iterate through req history, which gives you all status etc. and get status url and status code 
#         if len(req.history) > 0:  
#             for resp in req.history:
#                 f_data['Redirect_URL'] = resp.url
#                 f_data['Redirect_Status'] = resp.status_code 
# 'Redirect_Chain': resp.history 
                      
                #print(resp.url)
#             if 'X-Robots-Tag' in resp.headers.keys():
#                 response_data['X_Robots_Tag']=resp.headers['X-Robots-Tag']
#             else:
#                 response_data['X_Robots_Tag']=None
            #redirect_chain.append(response_data)    
        ## final (destination) url after any redirects collected here       
#         f_data = {'url':req.url,
#                   'Status Code':req.status_code, 
#                   'Redirect_Chain':req.history, 
#                   'Redirect_URL': req.headers['Location']
#                   #'Response_History': response_history
#                  }     
       
        # add robots tag data if it exists, if not write "none"
#         else:
#             continue
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


# In[ ]:




