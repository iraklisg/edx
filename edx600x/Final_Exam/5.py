class Member(object):
    def __init__(self, founder): # string
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name     

    def add_parent(self, mother): # Memeber()
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother): # Memeber()
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child): # Memeber()
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):  # string
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """
        #{'vasileia':Member('vasileia')}
        # Memeber('Vasileia'): name = 'Vasileia', parent = Member('Tasos'), children = [Member('Nikos'), Memeber('Mirsini')] 
        self.names_to_nodes = {} 
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root
#         self.cousine_type = 0 #                       !!!!!!!!!!!!!!   

    def set_children(self, mother, list_of_children):  # string , list of strings
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        if mother in self.names_to_nodes:
            mom_node = self.names_to_nodes[mother]
        else:
            raise KeyError('{} not in Family Tree'.format(mother))   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother] # assume that 'mother' is in self.names_to_nodes; else: KeyError
        child_node = self.names_to_nodes[kid] # assume that 'kid' is in self.names_to_nodes; else: KeyError
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b, cousin_type = 0, degree_removed = 0):
        """
        Returns a tuple of (the cousin type, degree removed) 
 
        cousin type is an integer that is -1 if a and b
        are the same node or if one is the direct descendent 
        of the other.  Otherwise, cousin type is 0 or greater,
        representing the shorter distance to their common 
        ancestor as described in 5-2.
 
        degree removed is the distance to the common ancestor
 
        Keyword arguments: 
        a -- string that is the name of a
        b -- string that is the name of b
        """
         
        ## YOUR CODE HERE ####
        # assume that both a and b are in names_to_nodes; else KeyError
        node_a = self.names_to_nodes[a]
        node_b = self.names_to_nodes[b]
        # if a and b are the same node or if one is the direct descendent of the other
        if node_a == node_b:
            return (-1, 0)
         
        # ======== wrapper function ==============    
        def find_ancestors(node, ancestors = []):
            ''' 
            returns a list of all ancestors of a node (included)
            up to the root node
             
            '''
            # BASE CASE:
            if node == None: # when hit the root node, whose parent is None
                return ancestors # return the list of ancestors
            # RECURSIVE CASE
            else: # while node is not the root node
                ancestors = [node] + ancestors # add this node to the ancestors list
                return find_ancestors(node.get_parent(), ancestors) # recursively repeat for the parent of this node, given the ancestors list so far
        # ========================================
           
        # ======== wrapper function ==============    
        def find_common_ancestor(n1, n2, ancest1 = [], ancest2 = [], count = 0):
            # BASE CASEs: if the parents of the node are the same, return the parent
            if n1 == n2: #means that n1 n2 was of the sane degree and reached at the same time recursively the common parent
                return n1, count # I may return n1.get_parrent() if I consider the parent node to be the common ancestor
            elif n1 in ancest2: # n1 is lower than n2 in tree
                return n1, count
            elif n2 in ancest1: # n2 is lower than n1 in tree
                return n2, count
            # RECURSIVE CASE
            else:
                # keep track of ancestors of n1 and n2
                ancest1 = [n1] + ancest1 
                ancest2 = [n2] + ancest2
                print 'n1 = {} in ancest2 = {} and n2 = {} in ancest1 = {}    count = {}'.format(n1, ancest2, n2, ancest1, count)
                return find_common_ancestor(n1.get_parent(), n2.get_parent(), ancest1, ancest2, count+1)
        # ========================================  
        print find_common_ancestor(node_a, node_b) 
             
         
         
        # ======== wrapper function ==============     
        def find_depth(node, depth = -2):
            if node == None:
                return depth
            else:
#                 print 'current parent = {}'.format(node.get_parent())
#                 print 'current depth = {}'.format(depth)
                return find_depth(node.get_parent(), depth+1)
        # ========================================  
        
        return 1, 2

         
f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

# print f.cousin('h', 'f')

## These are your test cases. 
 
## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'
t, r = f.cousin("b", "m")
print "'c' is a", words[t],"cousin", r, "removed from 'l'"
 
## For the remaining test cases, use the graph to figure out what should 
## be printed, and make sure that your code prints out the appropriate values.
 
# t, r = f.cousin("d", "f")
# print "'d' is a", words[t],"cousin", r, "removed from 'f'"
#    
# t, r = f.cousin("i", "n")
# print "'i' is a", words[t],"cousin", r, "removed from 'n'"
#    
# t, r = f.cousin("q", "e")
# print "'q' is a", words[t], "cousin", r, "removed from 'e'"
#    
# t, r = f.cousin("h", "c")
# print "'h' is a", words[t], "cousin", r, "removed from 'c'"
#    
# t, r = f.cousin("h", "a")
# print "'h' is a", words[t], "cousin", r, "removed from 'a'"
#    
# t, r = f.cousin("h", "h")
# print "'h' is a", words[t], "cousin", r, "removed from 'h'"
#    
# t, r = f.cousin("a", "a")
# print "'a' is a", words[t], "cousin", r, "removed from 'a'"