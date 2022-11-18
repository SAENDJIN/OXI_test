import random

random_number = random.randint(0, 9)
random_number_three = random.randint(100, 999)
random_number_two = random.randint(10, 99)

"+4 (930) 674-06-06 65"
random_phone = ("+4 (930) " + str(random_number_three) + "-" + str(random_number_two) + "-" + str(
    random_number_two) + " 65")

print(random_phone)
