from datetime import datetime


now = datetime.now()
CorrectDateFormat = now.strftime("%d.%m.%y.%H_%M")

random_email = ("andrii.qa31+autotest_" + str(CorrectDateFormat) + "@gmail.com")
