def test_registration_to_deposit(registration_deposit_de):
    registration_deposit_de.registration_form()
    registration_deposit_de.trigger_profile_input()
    registration_deposit_de.profile_info_fill()
    registration_deposit_de.deposit_to_redirect()
    assert registration_deposit_de.check_new_window()
    registration_deposit_de.close()