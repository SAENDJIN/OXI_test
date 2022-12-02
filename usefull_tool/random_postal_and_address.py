import random

postal_de = ['31623', '37434', '99303', '76831', '27412', '86925', '39326', '54340', '79283', '95506', '31785', '79787']
address_de = ["Feldstrasse", "Hedemannstasse",
           "Kieler Strasse", "Rohrdamm",
           "Bissingzeile", "Mohrenstrasse",
           "Albrechtstrasse", "Ufnau Strasse"]
city_de = ["Dormettingen", "Friedberg", "Memmingen",
        "Gilching", "Thurnau", "Vienenburg"]

random_postal = random.choice(postal_de)
random_address = random.choice(address_de)
random_city = random.choice(city_de)


