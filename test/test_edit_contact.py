# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact_lower(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="777"))
    app.contact.first_edit_lower(Contact(firstname="1", lastname="2", nickname="3",
                                         company="4", address="5", mobile="6",
                                         email="7@inbox.ru", bday="8", bmonth="September",
                                         byear="1999"))


def test_edit_first_contact_upper(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="777"))
    app.contact.first_edit_upper(Contact(firstname="00", lastname="00", nickname="00",
                                         company="00", address="00", mobile="00",
                                         email="89@inbox.ru", bday="5", bmonth="September",
                                         byear="2005"))
