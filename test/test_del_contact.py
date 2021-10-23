# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_del_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="777"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

#def test_del_first_contact_in_form(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="777"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.delete_first_in_form()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == len(new_contacts)
#    old_contacts[0:1] = []
#    assert old_contacts == new_contacts

#def test_del_all_contacts(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="777"))
#    app.contact.delete_all()
#    new_contacts = app.contact.get_contact_list()
#    assert len(new_contacts) == 0
#    assert new_contacts == []