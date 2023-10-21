from city_functions import get_formatted_city

def  test_city_country():
    """Do city, country like 'Casablanca, Morocco' work?"""
    formatted_name = get_formatted_city('Casablanca', 'Morocco')
    assert formatted_name == 'Casablanca, Morocco'