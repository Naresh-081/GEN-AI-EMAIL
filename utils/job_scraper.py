# utils/job_scraper.py

from langchain_community.document_loaders import WebBaseLoader

def scrape_job_description(url):
    loader = WebBaseLoader(url)
    page_data = loader.load()
    return page_data[0].page_content
