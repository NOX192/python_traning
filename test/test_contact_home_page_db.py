# -*- coding: utf-8 -*-
import re
from model.contact import Contact


def test_contact_on_home_page_with_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="321", lastname="222", address="address", mobilephone="phone",
                                   email="432@yandex.ru"))
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    contact_from_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)
    contact_from_db = sorted(contact_from_db, key=Contact.id_or_max)
    all_mails_from_home_page = []
    all_phone_from_home_page = []
    all_address_from_home_page = []
    for index in range(len(contact_from_home_page)):
        all_phone_from_home_page.append(contact_from_home_page[index].all_phones_from_home_page)
        all_mails_from_home_page.append(contact_from_home_page[index].all_email)
        all_address_from_home_page.append(contact_from_home_page[index].address)
    all_phone_from_db = []
    all_mails_from_db = []
    all_address_from_db = []
    for i in range(len(contact_from_db)):
        all_phone_from_db.append(contact_from_db[i].mobilephone)
        all_mails_from_db.append(contact_from_db[i].email)
        all_address_from_db.append(contact_from_db[i].address)
        if contact_from_db[i].workphone != "":
            all_phone_from_db[i] = all_phone_from_db[i] + '\n' + contact_from_db[i].workphone
        if contact_from_db[i].secondaryphone != "":
            all_phone_from_db[i] = all_phone_from_db[i] + '\n' + contact_from_db[i].secondaryphone
        if contact_from_db[i].email2 != "":
            all_mails_from_db[i] = all_mails_from_db[i] + '\n' + contact_from_db[i].email2
        if contact_from_db[i].email3 != "":
            all_mails_from_db[i] = all_mails_from_db[i] + '\n' + contact_from_db[i].email3
    all_phone_from_db = clear(str(all_phone_from_db))
    all_phone_from_home_page = clear(str(all_phone_from_home_page))
    assert contact_from_home_page == contact_from_db
    assert all_phone_from_home_page == all_phone_from_db
    assert all_mails_from_home_page == all_mails_from_db
    assert all_address_from_home_page == all_address_from_db

def clear(s):
    return re.sub("[() -]", "", s)