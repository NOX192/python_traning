# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_first_contat_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="777"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="11111111", lastname="123")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

 #def test_modify_first_contat_lastname(app):
  #  if app.contact.count() == 0:
    #     app.contact.create(Contact(firstname="777"))
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(lastname="123")
    #contact.id = old_contacts[0].id
    #app.contact.modify_first(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
    #old_contacts[0] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_first_contat_bday(app):
    #if app.contact.count() == 0:
    #    app.contact.create(Contact(firstname="777"))
   # old_contacts = app.contact.get_contact_list()
#    contact = Contact(bday="15")
 #   contact.id = old_contacts[0].id
  #  app.contact.modify_first(contact)
   # new_contacts = app.contact.get_contact_list()
   # assert len(old_contacts) == len(new_contacts)
   # old_contacts[0] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)