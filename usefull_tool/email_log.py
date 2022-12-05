from email_generator import random_email


def add_email_to_txt():
    txt = open("email.txt", "a+")
    txt.seek(0)
    data = txt.read(100)
    if len(data) > 0:
        txt.write("\n")

    run_txt = txt.write(random_email)


# add_email_to_txt()