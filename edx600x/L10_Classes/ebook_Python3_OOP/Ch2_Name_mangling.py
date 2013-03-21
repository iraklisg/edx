class SecretString:
    '''A not-at-all secure way to store a secret string.'''
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
    def decrypt(self, pass_phrase):
        '''Only show the string if the pass_phrase is correct.'''
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ''
secret_string = SecretString("ACME: Top Secret", "antwerp")
print(secret_string.decrypt("antwerp")) # ACME: Top Secret
print(secret_string.__plain_text) # Traceback AttributeError !!!!
#When we use a double underscore, the property
#is prefixed with _<classname>. When methods in the class internally access the
#variable, they are automatically unmangled. When external classes wish to access
#it, they have to do the name mangling themselves
#IN ORDER TO ACCESS __plain_text, prefix it with _<classname> i.e. _SecretString 
print(secret_string._SecretString__plain_string)

# FROM STACK OVERFLOW
# http://stackoverflow.com/questions/7456807/python-name-mangling-when-in-doubt-do-what

class Stack(object):

    def __init__(self):
        self.__storage = [] # Too uptight

    def push(self, value):
        self.__storage.append(value)

class Stack1(object):

    def __init__(self):
        self.storage = [] # No mangling

    def push(self, value):
        self.storage.append(value)

class Stack3(object):

    def __init__(self):
        self._storage = [] # This is ok but pythonistas use to be relaxed about it

    def push(self, value):
        self._storage.append(value)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age if age >= 0 else 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            self._age  = 0
