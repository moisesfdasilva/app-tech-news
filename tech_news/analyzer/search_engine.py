from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    news_list = search_news({"title": {"$regex": title.lower()}})
    title_and_url_list = []

    for news in news_list:
        news_truple = (news["title"], news["url"])
        title_and_url_list.append(news_truple)

    return title_and_url_list


def search_by_date(date):
    date_ISO = ""

    try:
        date_format_ISO = '%Y-%m-%d'
        date_ISO = datetime.strptime(date, date_format_ISO).date()
    except ValueError:
        raise ValueError("Data inválida")

    date_BR = format(date_ISO, '%d/%m/%Y')

    news_list = search_news({"timestamp": {"$regex": date_BR}})

    title_and_url_list = []

    for news in news_list:
        news_truple = (news["title"], news["url"])
        title_and_url_list.append(news_truple)

    return title_and_url_list


def search_by_category(category):
    """Seu código deve vir aqui"""
