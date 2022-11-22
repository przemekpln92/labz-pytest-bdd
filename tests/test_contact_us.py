from pytest_bdd import scenarios, given, when, then
from page_objects.contact_us import ContactUs



scenarios("../features/frontend/contact_us.feature")


@given("Open Contact Us")
def open_contact_us(init_driver, variables):
    assert 'Firefox' == variables['capabilities']['browser']
    page = ContactUs(init_driver)
    page.go_to_contact_us()