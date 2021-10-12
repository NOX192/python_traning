from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.click_add_new_contact()
        self.fill_contact_form(contact)
        self.click_submit()

    def delete_first(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def delete_first_in_form(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/input[2]").click()

    def delete_all(self):
        wd = self.app.wd
        self.open_contact_page()
        # select all contacts
        wd.find_element_by_xpath("//*[@id='MassCB']").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def first_edit_lower(self, contact):
        # button "update" of the bottom
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit()
        self.fill_contact_form(contact)
        # button "update"
        wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[22]").click()

    def first_edit_upper(self, contact):
        # button "update" at the top
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit()
        self.fill_contact_form(contact)
        self.submit_update_top()

    def submit_update_top(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[1]").click()

    def submit_edit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        self.change_field_value_select("bday", contact.bday)
        self.change_field_value_select("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

    def change_field_value_select(self, select_name, select_text):
        wd = self.app.wd
        if select_text is not None:
            wd.find_element_by_name(select_name).click()
            Select(wd.find_element_by_name(select_name)).select_by_visible_text(select_text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def click_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_xpath("//*[@id='nav']/ul/li[1]/a").click()

    def click_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def modify_first(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit()
        self.fill_contact_form(new_contact_data)
        self.submit_update_top()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))