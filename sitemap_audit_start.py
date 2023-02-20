import subprocess
import sys
import streamlit as st

st.title('GNE Sitemap Auditor')
st.subheader('Check the sitemaps for Genetech brand websites.')

def start_crawl():
    subprocess.run([f"{sys.executable}", "sitemap_auditor_run.py"])


def run_crawl():
    crawl_button = st.button("Start Crawl Now") # Give button a variable name
    if crawl_button: # Make button a condition.
        start_crawl()
        st.text("Crawl is starting. Your file will be downloaded shortly!")
        
run_crawl()       
