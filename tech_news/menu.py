import traceback
import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_categories


def analyzer_menu():
    view_menu()
    try:
        input_function = int(input())
        if input_function in range(0, 5):
            analyzer_menu_valid_item(input_function)
        else:
            analyzer_menu_invalid_item(input_function)
    except NameError:
        sys.stderr.write("Opção inválida\n")
    except Exception:
        traceback.print_exc()


def view_menu():
    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por categoria;")
    print(" 4 - Listar top 5 categorias;")
    print(" 5 - Sair.")


def analyzer_menu_invalid_item(item):
    if item == 5:
        print("Encerrando script")
        raise Exception
    else:
        raise NameError


def analyzer_menu_valid_item(item):
    if item == 0:
        print("Digite quantas notícias serão buscadas:")
        input_amount = input()
        get_tech_news(int(input_amount))
    elif item == 1:
        print("Digite o título:")
        input_title = input()
        search_by_title(input_title)
    elif item == 2:
        print("Digite a data no formato aaaa-mm-dd:")
        input_date = input()
        search_by_date(input_date)
        print(item)
    elif item == 3:
        print("Digite a categoria:")
        input_category = input()
        search_by_category(input_category)
        print(item)
    else:
        categories = top_5_categories()
        print(categories)
