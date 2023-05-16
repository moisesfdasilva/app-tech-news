import requests
import time
from parsel import Selector


def fetch(url):
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None


def scrape_updates(html_content):
    selector = Selector(text=html_content)
    all_urls = selector.css(".entry-title a::attr(href)").getall()
    return all_urls


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    all_urls = selector.css(".page-numbers a::attr(href)").getall()
    print(all_urls)
    return "all_urls"


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
