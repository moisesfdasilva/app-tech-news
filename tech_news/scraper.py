import requests
import time
from parsel import Selector
import unicodedata


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
    next_page_url = selector.css(".next::attr(href)").get()
    return next_page_url


def scrape_news(html_content):
    selector = Selector(text=html_content)

    url_buttons = selector.css(".pk-share-buttons-link *::attr(href)").getall()
    facebook_share = "https://www.facebook.com/sharer.php?u="
    page_url = url_buttons[0].replace(facebook_share, "")

    page_title = selector.css(".entry-title::text").get()
    page_title = unicodedata.normalize('NFKC', page_title).rstrip()

    page_timestamp = selector.css(".entry-header-inner .meta-date::text").get()

    page_writer = selector.css(".author a::text").get()

    page_reading_time_text = selector.css(".meta-reading-time::text").get()
    page_reading_time = int(page_reading_time_text.split(' ')[0])

    page_first_par_html = selector.css(".entry-content p")[0]
    page_first_par_text = page_first_par_html.css("*::text").getall()
    page_summary = ""
    for phrase in page_first_par_text:
        page_summary = page_summary + phrase
    page_summary = unicodedata.normalize('NFKC', page_summary).rstrip()

    page_category = selector.css(".entry-header-inner .label::text").get()

    obj_summary = {
        "url": page_url,
        "title": page_title,
        "timestamp": page_timestamp,
        "writer": page_writer,
        "reading_time": page_reading_time,
        "summary": page_summary,
        "category": page_category,
    }

    return obj_summary


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
