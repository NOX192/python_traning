# -*- coding: utf-8 -*-


def test_del_first_contact(app):
    app.contact.delete_first()


def test_del_first_contact_in_form(app):
    app.contact.delete_first_in_form()


def test_del_all_contacts(app):
    app.contact.delete_all()
