# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    change_group = Group(id=group.id, name="NewName", header="newheader", footer="newfooter")
    app.group.modify_group_by_id(group.id, change_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    index = new_groups.index(change_group)
    old_groups[index] = change_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
