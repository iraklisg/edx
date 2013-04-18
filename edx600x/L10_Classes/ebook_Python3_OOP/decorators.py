# Direct attribute access 
class Color(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name
        
c = Color('#ff000', 'bright red')
print 'c.name =',c.name # direct get of object's 'c' name attribute
c.name = "blue" # direct set object's c name attribute
print 'c.name =',c.name # direct get of object's 'c' new name attribute
c.name  = ""
print 'c.name =',c.name # does NOT perform validation for given an empty name

# Simple method-based attribute access method

''' Now I decided to make attributes semi-private and change the access method form direct to method-based
However, now I should change the access method in IDLE !!!!

'''
class Color0(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name # change name attribute to semi-private _name
    
    def _set_name(self, name): # add semi-private method _set_name to set name
        self._name = name
    
    def _get_name(self): # add semi-private method _get_name to get name
        return self._name

c0 = Color0('#ff000', 'bright red')
print 'c.name =',c0.name # name does not exists anymore, I have to change access code in IDLE to c0._name in order to have direct access on object's name attribute
c0.name = "blue" # name does not exists anymore, changed to _name !!!
print 'c.name =',c0.name 
c0.name  = ""
print 'c.name =',c0.name

# Method based attribute access using PROPERTY keyword

'''in Java and similar languages, if we had written our original code to do direct
attribute access, and then later changed it to a method like the above, we'd have a
problem: Anyone who had written code that accessed the attribute directly would
now have to access the method; if they don't change the access style, their code
will be broken. The mantra in these languages is that we should never make public
members private. This doesn't make much sense in Python since there isn't any
concept of private members!

PROPERTY FUNCTION x = property(getx, setx, delx, "I'm the 'x' property.")
If then c is an instance of Color1, c.name will invoke the getter, c.name = value will invoke the setter and del c.name the deleter.
If given, doc will be the docstring of the property attribute. Otherwise, the property will copy fgets docstring (if it exists).

'''

class Color1(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name # change name attribute to semi-private _name
    
    def _set_name(self, name): # add semi-private method _set_name to set name
        if name == "":
            print 'where is the name?'
        self._name = name
    
    def _get_name(self): # add semi-private method _get_name to get name
        return self._name
    
    name = property(_get_name, _set_name)   # `name` is the attribute we want to get/set, etc i.e print c1.`name` / c1.`name` = value
                                            # creates a new attribute on the Color class called name , which now *replaces the previous
                                            # name attribute*. It sets this attribute to be a *property*, which calls the two methods
                                            # we just created *whenever the property is accessed or changed*.
                                            # This new version of the Color class can be used exactly the same way as the previous version, yet it now
                                            # does validation when we set the name (we do not need to change access method!!!)



c1 = Color1('#ff000', 'bright red')
print 'c1.name =',c1.name # get of object's name attribute through _get_name property
c1.name = "blue" # set object's c name attribute through _set_name property
print 'c1.name =',c1.name
c1.name  = ""
print 'c1.name =',c1.name # DOES perform validation for given an empty name through calling _set_name property

# SOS!!! Bear in mind that even with the name property, the previous code is not 100% safe.
# People can still access the _name attribute directly and set it to an empty string if
# they wanted to. E.g:
c1._name = ""
print 'c1.name =',c1.name # Now again, it DOES not perform validation for given an empty name through calling _set_name property


# ANOTHER EXAMPLE of Method based attribute access using PROPERTY DECORATOR

class Color2(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name # change name attribute to semi-private _name
    
    @property # this is getter by default. It's equal to color = property(color).  You have to define getter first, else error !!!
    def name(self): # the  getter function should be named whatever we want to get, e.g we want to get c2.`name` attribute, thus def `name`
        return self._name
    
    @name.setter # this is setter for var name
    def name(self, name): # the  getter function should be called whatever we want to set, e.g we want to set c2.`name` attribute, thus def `name`
        if name == "":
            print "You haven't provide any name motherfucker"
        self._name = name

c2 = Color2('#ff000', 'bright red')
print 'c2.name =',c2.name # set object's c name attribute (that's way I named property def name()) through decorator
c2.name = "blue" 
print 'c2.name =',c2.name
c2.name  = ""
print 'c2.name =',c2.name # DOES perform validation for given an empty name through calling _set_name property

