import allure


@allure.title("Registration new user and make deposit 5 different methods")
def test_registration_to_deposit_five_methods(registration_deposit_five_methods):
    registration_deposit_five_methods.registration_form()
    registration_deposit_five_methods.trigger_profile_input()
    registration_deposit_five_methods.profile_info_fill()
    registration_deposit_five_methods.payment_bank_uberweisung_black()
    registration_deposit_five_methods.payment_bank_uberweisung_white()
    registration_deposit_five_methods.payment_visa()
    registration_deposit_five_methods.payment_mastercard_paygate()
    registration_deposit_five_methods.payment_mastercard_payment_service()
    registration_deposit_five_methods.close()
