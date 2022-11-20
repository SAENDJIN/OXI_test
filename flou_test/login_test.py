def test_login_to_deposit(login_deposit_de):
    login_deposit_de.login_form()
    login_deposit_de.go_to_deposit()
    login_deposit_de.choose_payment_method()
    assert login_deposit_de.check_new_window()
    login_deposit_de.close()
