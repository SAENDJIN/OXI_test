import random

random_day = random.randint(1, 12)
random_month = random.randint(1, 12)
random_year = random.randint(1949, 2000)

random_date = (str(random_day).zfill(2) + "." + str(random_month).zfill(2) + "." + str(random_year))
