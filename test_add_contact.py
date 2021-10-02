# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", pwd="secret")
    app.create_contact(Contact(firstname="Anton", lastname="Ivanov", nickname="fddsfsfds",
                                                  company="Google", address="www.Leningrad", mobile="+7123456789",
                                                  email="dsfdshiu@gmail.com", bday="14", bmonth="August",
                                                  byear="1987"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", pwd="secret")
    app.create_contact(Contact(firstname="", lastname="", nickname="",
                                                  company="", address="", mobile="",
                                                  email="", bday="", bmonth="-",
                                                  byear=""))
    app.logout()
