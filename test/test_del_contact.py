# -*- coding: utf-8 -*-


def test_del_first_contact(app):
    app.session.login(username="admin", pwd="secret")
    app.contact.delete_first_contact()
    app.session.logout()

def test_del_first_contact_in_form(app):
    app.session.login(username="admin", pwd="secret")
    app.contact.delete_first_contact_in_form()
    app.session.logout()

def test_del_all_contacts(app):
    app.session.login(username="admin", pwd="secret")
    app.contact.delete_all_contact()
    app.session.logout()