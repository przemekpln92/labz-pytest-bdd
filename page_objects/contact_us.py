from page_objects.base_page import BasePage

class ContactUs(BasePage):

    def go_to_contact_us(self):
        self.driver.get("https://webdriveruniversity.com/Contact-Us/contactus.html")