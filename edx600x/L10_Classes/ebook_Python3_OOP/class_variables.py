# p. 64
class Contact(object):
    all_contacts = [] # class variable, shared by all instances of this class;
    #there is only one Contact.all_contacts list, and if we call
    #self.all_contacts on any one object, it will refer to that single list 
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(name) #if we call self.all_contacts on any one object, it will refer to that single list 
        
    def __str__(self):
        return str(self.name)
    
    def print_all(self):
        return self.all_contacts
    
    def set_instance_var(self,name):
        self.all_contacts = name #if you ever set the variable using self.all_contacts,
        # you will actually be creating a new instance variable on the object;
        # the class variable will still be unchanged and accessible as Contact.all_contacts.
    def set_class_var(self, name):
        Contact.all_contacts = name #if you ever set the variable using self.all_contacts,
        # you will actually be creating a new instance variable on the object;
        # the class variable will still be unchanged and accessible as Contact.all_contacts.

nick = Contact('Nikos','nick@gmail.com')
mitsos = Contact('Mitsos','mitsos@gmail.com')
ira = Contact('Iraklis','ira@gmail.com')

print nick.email
print nick # ovewritten by __str__
print Contact.all_contacts
print 'Ah-ha !! ',nick.print_all() # Now that I have NOT set an instance var all_contacts, it prints out the class variable (Contact.all_contacts) value
print '============= SET INSTANCE VAR ==========='
nick.set_instance_var('Nikolaras') # Here I set the variable using self.all_contacts
print 'Class var =',Contact.all_contacts # class variable will still be unchanged and accessible as Contact.all_contacts
print 'Instance var =',nick.all_contacts # all contacts now is a new instance variable 
print '============= SET CLASS VAR ==========='
nick.set_class_var('Marmaras') # Here I set variable using Contacts.
print 'Class var =',Contact.all_contacts # class variable has been changed!
print 'Instance var =',nick.all_contacts # instance var has not been affected
print '=============='
print nick.print_all()  # now that I have set an instance var all_contacts, it prints out the instance variable (self.all_contacts) value
                        # an object variable with the same name as a class variable will hide the class variable!!!!