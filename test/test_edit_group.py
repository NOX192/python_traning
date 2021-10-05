# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", pwd="secret")
    app.group.edit_first_group(Group(name="111", header="222", footer="333"))
    app.session.logout()