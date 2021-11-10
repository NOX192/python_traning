from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:


    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.click_add_new_contact()
        self.fill_contact_form(contact)
        self.click_submit()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[1]/a").click()
        self.contact_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_in_form(self):
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/input[2]").click()
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[1]/a").click()
        self.contact_cache = None

    def delete_all(self):
        wd = self.app.wd
        self.open_contact_page()
        # select all contacts
        wd.find_element_by_xpath("//*[@id='MassCB']").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[1]/a").click()
        self.contact_cache = None

    def first_edit_lower(self, contact):
        # button "update" of the bottom
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit()
        self.fill_contact_form(contact)
        # button "update"
        wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[22]").click()
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[1]/a").click()
        self.contact_cache = None

    def first_edit_upper(self, contact):
        # button "update" at the top
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit()
        self.fill_contact_form(contact)
        self.submit_update_top()
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[1]/a").click()
        self.contact_cache = None

    def submit_update_top(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[1]").click()

    def submit_edit(self):
        wd = self.app.wd
        wd.find_element_by_title("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()

    def submit_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath(f"/html/body/div/div[4]/form[2]/table/tbody/tr[{index+2}]/td[8]/a/img").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobilephone)
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

    def modify_first(self):
        self.submit_edit_by_index(0)

    def modify_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        self.submit_update_top()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            n = 2
            for element in wd.find_elements_by_name("entry"):
                ln = element.find_element_by_xpath(f"//tbody/tr[{n}]/td[2]").text
                fn = element.find_element_by_xpath(f"//tbody/tr[{n}]/td[3]").text
                all_phones = element.find_element_by_xpath(f"//tbody/tr[{n}]/td[6]").text
                addr = element.find_element_by_xpath(f"//tbody/tr[{n}]/td[4]").text
                mail = element.find_element_by_xpath(f"//tbody/tr[{n}]/td[5]").text
                n = n + 1
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=ln, firstname=fn, id=id, all_phones_from_home_page=all_phones,
                                                  address=addr, all_email=mail))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath(f"//tbody/tr[{index + 2}]/td[7]/a[1]/img[1]").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, address=address, email=email1,
                       email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[1]/a").click()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.submit_edit_by_id(id)
        self.fill_contact_form(new_contact_data)
        self.submit_update_top()
        self.contact_cache = None

    def submit_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' % id).click()
