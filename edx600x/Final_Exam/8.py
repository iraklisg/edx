class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    def __str__(self):
        return self.myName()
    def __repr__(self):
        return self.myName()


frobs = [Frob('eric')]
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    # assume that the atMe is already part of the linked list
    # Append the newFrob in list and then sort the list by name
    frobs.append(newFrob)
    sorted_frobs = sorted(frobs, key = metric, reverse = False)
    print sorted_frobs
    # find the index of the newFrob
    i = sorted_frobs.index(newFrob)
    print 'index = ',i
    # Go to the previous frob and set after=newFrob
    if i-1 >= 0: sorted_frobs[i-1].setAfter(newFrob)
#     else: sorted_frobs[i-1].setAfter(None)
    # Go to the next frob and set before=newFrob
    if i+1 <= len(sorted_frobs)-1: sorted_frobs[i+1].setBefore(newFrob)
#     else: sorted_frobs[i+1].setBefore(None)

     
# metric: use item's value
def metric(item):
    return item.myName()


# def insert(atMe, newFrob):
#     """
#     atMe: a Frob that is part of a doubly linked list
#     This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
#     """
#     # Your Code Here
#     # assume that the atMe is already part of the linked list
#     atMe_name = atMe.myName()
#     newFrob_name = newFrob.myName()
#     if atMe_name >= newFrob_name: #if atMe = fred and newFrob = eric
#         newFrob.setAfter(atMe)# after eric is fred 
#         atMe.setBefore(newFrob)# befor fred is eric
#     else:
#         newFrob.setBefore(atMe)
#         atMe.setAfter(newFrob)

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

guys = [fred, andrew, martha, eric, ruth]
sorted_guys = sorted(guys, key = metric, reverse = False)

# for guy in guys:
#     print '{} --> ({}) --> {}'.format(guy.getBefore(), guy.myName(), guy.getAfter())



# print sorted_guys

for guy in sorted_guys:
    print '{} --> ({}) --> {}'.format(guy.getBefore(), guy.myName(), guy.getAfter())