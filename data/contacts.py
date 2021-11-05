from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1",
            nickname="nickname1", company="company1",
            address="address1",
            mobilephone="mobilephone1", email="email1"),
    Contact(firstname="firstname2", lastname="lastname2",
            nickname="nickname2", company="company2",
            address="address2",
            mobilephone="mobilephone2", email="email2")

]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", nickname="", company="", address="", mobilephone="", email="")] +  [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 15), company=random_string("company", 20), address=random_string("address", 30),
            mobilephone=random_string("mobilephone", 10), email=random_string("email", 10))
    for i in range(5)
]