from tech_news.database import search_news
from tech_news.analyzer.search_engine import search_by_category


def top_5_categories():
    news_list = search_news({
        "title": {"$regex": ""}})

    categories_list = set()
    for news in news_list:
        categories_list.add(news["category"])

    categories_repetition_list = []
    for category in categories_list:
        db_itens = search_by_category(category)
        truple_category = (category, len(db_itens))
        categories_repetition_list.append(truple_category)

    categories_repetition_list.sort()
    categories_repetition_list.sort(key=lambda a: a[1], reverse=True)

    i = 0
    top_5_list = []
    for category in categories_repetition_list:
        if i < 5:
            top_5_list.append(category[0])
            i = i + 1

    return top_5_list
