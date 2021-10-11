# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="777"))
    app.contact.delete_first()


def test_del_first_contact_in_form(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="777"))
    app.contact.delete_first_in_form()


def test_del_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="777"))
    app.contact.delete_all()
