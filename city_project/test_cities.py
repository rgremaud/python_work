from city_functions import get_city_name

def test_city_name():
    """Test that city name and country pulls correctly"""
    city_name = get_city_name("raleigh", "united states")
    assert city_name == "Raleigh, United States"

def test_city_name_population():
    """Test that city name, country and populate populate correctly"""
    city_name = get_city_name("raleigh", "united states", 1000000)
    assert city_name == "Raleigh, United States - Population 1000000"