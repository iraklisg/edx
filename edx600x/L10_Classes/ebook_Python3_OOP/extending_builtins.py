class ContactList(list): # ContactList extends list class
    def search(self, searh_name):
        '''Return all contacts that contain the search value
        in their name.'''
        matching_contacts = []
        for contact in self: # for any Contact object in Contact.all_contacts ; e.g: Contact.all_contacts = [c1, c2, c3]
            if searh_name in contact.name: # if searh_name in Contact.object.name, e.g: c1.name
                matching_contacts.append(contact)
        return matching_contacts


class Contact(object):
    all_contacts = ContactList()    # all_contacts type = ContactList 
                                    # upon initialization, all_contacts calls __init__ from built-in class list, that is self = list() == []
                                    # Therefore, all_contacts = ContactList() == all_contacts = []
                                    # Due to inheritance, now all_contacts has an additional method called search!
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

list1 = ContactList()
print list1 # results in an empty list [], because upon initialization, list1 runs __init__ from built-in class list, that is self = list() == []

c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")

print [c.name for c in Contact.all_contacts.search('John')]


class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self: # for key in longkeys <LongNameDict> object; i.e for key in {'longest yet': 5, 'hello2': 'world', 'hello': 1}
            if not longest or len(key) > len(longest):
                longest = key
        return longest

longkeys = LongNameDict() # initialize an empty dict, since `LongNameDict` class inherits from built-in `dict` class
print longkeys
longkeys['hello'] = 1 # create the first <key:value> pair
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'
print longkeys
for e in longkeys:
    print e
print longkeys.longest_key()
