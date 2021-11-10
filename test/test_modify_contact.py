# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_modify_some_contat(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="777"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    change_contact = Contact(id=contact.id, firstname="11111111", lastname="123", address="dsadaasda", mobilephone="213131312", email="dsad@mail.ru")
    app.contact.modify_by_id(contact.id, change_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    index = new_contacts.index(change_contact)
    old_contacts[index] = change_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

