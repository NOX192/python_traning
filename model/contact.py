from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, company=None,
                 address=None, mobile=None, email=None, bday=None, bmonth=None, byear=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id



    def __repr__(self):
        return "%s:%s %s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and \
               self.firstname == other.firstname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize