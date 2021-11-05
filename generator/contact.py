from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

n = 5
f = "data/contacts.json"

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", nickname="", company="", address="", mobilephone="", email="")] +  [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 15), company=random_string("company", 20), address=random_string("address", 30),
            mobilephone=random_string("mobilephone", 10), email=random_string("email", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))