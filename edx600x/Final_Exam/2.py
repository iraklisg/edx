class EdxStudent(object):
      def __init__(self,first,last):
             self.setName("given",first)
             self.setName("family",last)

      def setName(self,which,name):
            if which == "given" or which == "first":
                  self.firstName = name
            elif which == "family" or which == "last":
                  self.lastName = name
            else:
                  raise ChoiceError(which)

      def getName(self,which):
            if which == "given" or which == "first":
                  return self.firstName
            elif which == "family" or which == "last":
                  return self.lastName
            raise ChoiceError(which)

class ChoiceError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr("Invalid value for name field:"+self.value)


firstName = "Raquel"
lastName = "Pomplun"

try:
        student = EdxStudent(firstName,lastName)

        initialFirstName = student.getName("first")
        initialLastName = student.getName("last")


        newFirstName = student.getName("given")
        newLastName = student.getName("family")

        if initialFirstName == newFirstName and initialLastName == newLastName:
               print "Passed unit test 1" ###
        else:
               print "Failed unit test 1"

        student.setName("given","LeBron")
        student.setName("family","James")
        print "LeBron"+"James",student.getName("first")+student.getName("last")
        if "LeBron"+"James" == student.getName("first")+student.getName("last"):
               
               print "Passed unit test 2"
        else:
               print "Failed unit test 2"

except ChoiceError as e:
       print "Failed unit test. Exception is:",
       print e

# print student.setName("Given")
student = EdxStudent("sd", "last")
print student.getName("last")
# print student.setName("which", "john")