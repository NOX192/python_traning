from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, company=None,
                 address=None, mobilephone=None, homephone=None, workphone=None, secondaryphone=None,
                 email=None, bday=None, bmonth=None, byear=None, id=None, all_phones_from_home_page=None, all_email=None,
                 email2=None, email3=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.mobilephone = mobilephone
        self.homephone = homephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email = all_email
        self.email2 = email2
        self.email3 = email3


    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s" % (self.id, self.lastname, self.firstname, self.nickname, self.company,
                                         self.address, self.mobilephone, self.email )

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and \
               self.firstname == other.firstname



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize