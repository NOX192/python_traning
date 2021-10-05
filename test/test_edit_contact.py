# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact_button_of_the_bottom(app):
    app.session.login(username="admin", pwd="secret")
    app.contact.edit_button_of_the_bottom(Contact(firstname="1", lastname="2", nickname="3",
                               company="4", address="5", mobile="6",
                               email="7@inbox.ru", bday="8", bmonth="September",
                               byear="1999"))
    app.session.logout()

def test_edit_contact_button_at_the_top(app):
    app.session.login(username="admin", pwd="secret")
    app.contact.edit_button_at_the_top(Contact(firstname="00", lastname="00", nickname="00",
                               company="00", address="00", mobile="00",
                               email="89@inbox.ru", bday="5", bmonth="September",
                               byear="2005"))
    app.session.logout()