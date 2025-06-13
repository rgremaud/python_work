def get_city_name(city, country, population=''):
    """Generate full city name"""
    if population:
        full_name = f"{city}, {country} - population {population}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()
