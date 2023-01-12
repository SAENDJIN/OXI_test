import allure


@allure.title("Login old user and make deposit 4 times different methods")
def test_login_to_deposit_four_methods(login_deposit_de_four_methods):
    login_deposit_de_four_methods.login_form()
    login_deposit_de_four_methods.go_to_deposit()
    login_deposit_de_four_methods.payment_bank_uberweisung_black()
    login_deposit_de_four_methods.payment_bank_uberweisung_white()
    # login_deposit_de_four_methods.payment_visa()
    login_deposit_de_four_methods.payment_mastercard_paygate()
    login_deposit_de_four_methods.payment_mastercard_payment_service()
    login_deposit_de_four_methods.close()
