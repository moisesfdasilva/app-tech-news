from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest


def test_reading_plan_group_news():
    """
    Verifica se cria retorna uma lista com as notícias que podem ser lidas, em
    um limite de tempo, e as que não podem, sendo verificado se ocorrem erros
    se o limite for zero ou uma string.
    """

    output = {
        'readable': [
            {'chosen_news': [('Notícia bacana', 4)], 'unfilled_time': 1},
            {'chosen_news': [('Notícia bacana 2', 1)], 'unfilled_time': 4}],
        'unreadable': []}
    res_stantard = ReadingPlanService.group_news_for_available_time(5)
    assert res_stantard == output

    output_readable_empty = {
        'readable': [],
        'unreadable': [('Notícia bacana', 4), ('Notícia bacana 2', 1)]}
    res_readable_empty = ReadingPlanService.group_news_for_available_time(0.5)
    assert res_readable_empty == output_readable_empty

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    with pytest.raises(TypeError):
        ReadingPlanService.group_news_for_available_time("x")
