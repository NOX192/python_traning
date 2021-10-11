from selenium.webdriver.support.ui import WebDriverWait

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, pwd):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pwd)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logget_in():
            wd.find_element_by_link_text("Logout").click()

    def is_logget_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logget_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    def ensure_login(self, username, pwd):
        wd = self.app.wd
        if self.is_logget_in():
            if self.is_logget_in_as(username):
                return
            else:
                self.logout()
        self.login(username, pwd)