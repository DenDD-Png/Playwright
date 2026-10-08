import pytest

from data import data_id, load_login_data


@pytest.mark.smoke
def test_login_form_opens(login):
    login.should_be_opened()

@pytest.mark.parametrize("td", load_login_data(ids=["empty_email"]), ids=data_id)
def test_empty_email_error(login, td):
    login.enter_email(td.email)
    login.submit()
    login.should_show_error(td.expected_error)

@pytest.mark.parametrize("td", load_login_data(ids=["sample_email"]), ids=data_id)
def test_email_input(login, td):
    login.enter_email(td.email)
    login.should_have_email(td.email)
