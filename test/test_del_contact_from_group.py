# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db1 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="321", lastname="222", address="address", mobilephone="phone",
                                   email="432@yandex.ru"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="GroupName", header="NEWheader", footer="Footer"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    db.remove_all_contacts_from_all_groups()
    db.add_random_contact_to_random_group(contact.id, group.id)
    app.contact.del_from_group_by_id(contact.id, group.id)
    assert db1.get_contacts_in_group(Group(id=f"{group.id}")) == []

