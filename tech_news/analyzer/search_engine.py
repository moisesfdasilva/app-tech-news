from tech_news.database import search_news


def search_by_title(title):
    news_list = search_news({"title": {"$regex": title.lower()}})
    title_and_url_list = []

    for news in news_list:
        news_truple = (news["title"], news["url"])
        title_and_url_list.append(news_truple)

    return title_and_url_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
