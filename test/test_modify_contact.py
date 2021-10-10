# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_first_contat_firstname(app):
    app.contact.modify_first(Contact(firstname="11111111"))


def test_modify_first_contat_lastname(app):
    app.contact.modify_first(Contact(lastname="dfssdff"))


def test_modify_first_contat_bday(app):
    app.contact.modify_first(Contact(bday="15"))
