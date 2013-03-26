class Contact(object):
    all_contacts = [] # is the same as all_contacts.list()
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
        
class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send '{}' order to '{}'".format(order, self.name))

c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email, s.name, s.email)
print c.all_contacts # all_contacts list contains 2 objects: <__main__.Contact instance at 0x7ff7ade230e0> and <__main__.Supplier instance at 0x7ff7ade23128>
#c.order("I need pliers")
s.order("I need pliers")
