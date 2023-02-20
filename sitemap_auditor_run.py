#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import xmltodict
from cachecontrol import CacheControl
import time
import streamlit as st

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




st.title('GNE Sitemap Auditor')
st.subheader('Check the sitemaps for Genetech brand websites.')


def run_crawl():
    crawl_button = st.button("Start Crawl Now") # Give button a variable name
    if crawl_button: # Make button a condition.
        start_crawl()
        st.text("Crawl is starting. Your file will be downloaded shortly!")
        
run_crawl()

def crawl_sitemaps():
    st.write("Building sitemap list...")
    sess = requests.session()
    return sess
    cached_sess = CacheControl(sess)
    return cached_sess
    response = cached_sess.get('http://google.com')
    return response
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-x-robots'
             }
    return header
    sitemap_crawl_list = ["https://www.gazyva.com/sitemap.xml",
                        "https://www.gazyva-hcp.com/sitemap.xml",
                        "https://www.polivy.com/sitemap.xml",
                        "https://www.lucentis.com/sitemap.xml",
                        "https://www.againstlivercancer.com/sitemap.xml",
                        "https://www.biomarkertesting.com/sitemap.xml",
                        "https://www.earlynsclc.com/sitemap.xml",
                        "https://www.tecentriq-hcp.com/sitemap.xml",
                        "https://www.tecentriq.com/sitemap.xml",
                        "https://www.venclextahcp.com/sitemap.xml",
                        "https://www.ocrevus-hcp.com/sitemap.xml",
                        "https://www.ocrevus.com/sitemap.xml",
                        "https://www.ocrelizumabinfo.com/sitemap.xml",
                        "https://www.susvimo-hcp.com/sitemap.xml",
                        "https://www.susvimo.com/sitemap.xml",
                        "https://www.vabysmo-hcp.com/sitemap.xml",
                        "https://www.vabysmo.com/sitemap.xml",
                        "https://www.genentech-access.com/sitemap.xml",
                        "https://www.evrysdi-hcp.com/sitemap.xml",
                        "https://www.evrysdi.com/sitemap.xml",
                        "https://www.herceptin.com/sitemap.xml",
                        "https://www.xolair.com/sitemap.xml",
                        "https://www.xolairhcp.com/sitemap.xml",
                        "https://www.alecensa.com/sitemap.xml",
                        "https://www.gavreto.com/sitemap.xml",
                        "https://www.gavreto-hcp.com/sitemap.xml",
                        "https://www.rozlytrek-hcp.com/sitemap.xml",
                        "https://www.rozlytrek.com/sitemap.xml",
                        "https://www.genentechhemophilia.com/sitemap.xml",
                        "https://www.hemlibra-hcp.com/sitemap.xml",
                        "https://www.hemlibra.com/sitemap.xml",
                        "https://www.emicizumabinfo.com/patient/sitemap.xml",
                        "https://www.rituxanhycela.com/sitemap.xml",
                        "https://www.avastin.com/sitemap.xml",
                        "https://www.cellcept.com/sitemap.xml",
                        "https://www.cotellic.com/sitemap.xml",
                        "https://www.erivedge.com/sitemap.xml",
                        "https://www.nutropin.com/sitemap.xml",
                        "https://www.enspryng-hcp.com/sitemap.xml",
                        "https://www.enspryng.com/sitemap.xml",
                        "https://www.esbriet.com/sitemap.xml",
                        "https://www.esbriethcp.com/sitemap.xml",
                        "https://www.huntingtonsdisease.com/sitemap.xml",
                        "https://www.huntingtonsdiseasehcp.com/sitemap.xml",
                        "https://www.cathflo.com/sitemap.xml",
                        "https://www.xofluza-hcp.com/sitemap.xml",
                        "https://www.xofluza.com/sitemap.xml",
                        "https://www.ophthalmologyvision.com/sitemap.xml",
                        "https://www.screenyourlungs.org/sitemap.xml",
                        "https://www.cancerscreenweek.org/sitemap.xml",
                        "https://www.strokeawareness.com/sitemap.xml",
                        "https://www.genentechoncology.com/sitemap.xml",
                        "https://www.genentech-pro.com/sitemap.xml",
                        "https://www.phesgo.com/sitemap.xml",
                        "https://www.hemework.com/sitemap.xml",
                        "https://www.kadcyla.com/sitemap.xml",
                        "https://www.perjeta.com/sitemap.xml",
                        "https://www.phesgo-hcp.com/sitemap.xml",
                        "https://www.herceptinhylecta.com/sitemap.xml",
                        "https://www.genentech-forum.com/sitemap.xml",
                        "https://www.pulmozyme.com/sitemap.xml",
                        "https://www.rituxan-hcp.com/sitemap.xml",
                        "https://www.rituxan.com/sitemap.xml",
                        "https://www.fuzeon.com/sitemap.xml",
                        "https://www.faceipf.com/sitemap.xml",
                        "https://www.actemra.com/sitemap.xml",
                        "https://www.actemrahcp.com/sitemap.xml",
                        "https://www.activase.com/sitemap.xml",
                        "https://www.pinkribbonbottle.com/sitemap.xml",
                        "https://www.tnkase.com/sitemap.xml",
                        "https://www.herconnection.com/sitemap.xml",
                        "https://www.mycareforward.com/sitemap.xml",
                        "https://www.allforalz.com/sitemap.xml",
                        "https://www.rethinkdlbcl.com/sitemap.xml",
                        "https://www.genentechmaterials.com/sitemap.xml",
                        "https://www.researchakt.com/sitemap.xml",
                        "https://www.examinebiosimilars.com/sitemap.xml",
                        "https://www.rarediseasesignup.com/sitemap.xml",
                        "https://www.her2treatmentoptions.com/sitemap.xml",
                        "https://www.discovertrk.com/sitemap.xml",
                        "https://www.thehiddenpredator.com/sitemap.xml",
                        "https://www.genentech-clinicaltrials.com/sitemap.xml",
                        "https://www.gatherms.com/sitemap.xml",
                        "https://www.mycareroadmap.com/sitemap.xml",
                        "https://www.tamiflu.com/sitemap.xml",
                        "https://www.her2empowered.com/sitemap.xml",
                        "https://www.ocrevusmanagedcare.com/sitemap.xml",
                        "https://www.lunsumio.com/sitemap.xml",
                        "https://www.kadcyla-hcp.com/sitemap.xml",
                        "https://www.drugpricinglaw.com/sitemap.xml",
                        "https://www.lunsumio-hcp.com/sitemap.xml",
                        "https://www.genentech-medinfo.com/sitemap.xml",
                        "https://www.emicizumabinfo.com/patient/sitemap.xml",
                        "https://www.homevisionmonitor.com/sitemap.xml",
                        "https://www.mytactic.com/sitemap.xml"]
    data = []
    connection_errors = []

    st.write("Starting sitemap crawl...")
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

crawl_sitemaps()




