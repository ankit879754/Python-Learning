#from os import name


#class ankit_info():
   # ankit_bank_name ="SBI"
   # passbook_number = "87657578698"
   # ifsc_code = "AIRP0000001"

#ankit_obj = ankit_info()
#print(ankit_obj.ankit_bank_name)
#print(ankit_obj.passbook_number)

#________________________________________________________________________________

#privet

#class student:
#    def __init__(self, name):
#        self.__name = name
#
#s = student("ankit")
#print(s._student__name)

#________________________________________________________________________________

#protected

#class student:
   # def __init__(self,name,):
   # self._name = name

#s = student("ankit")
#print(s._name)

#________________________________________________________________________________

#public

#class student:
    #def __init__(self,name):
        #self.name = name


#s = student("ankit")


#___________________________________________________________________________________
# PUBLIC

class college:
    college_name = "IES UNIVERSITY"
    branch = "CSE"
    fee = "1L"

c = college()
print(c.college_name)
print(c.branch)
print(c.fee)

#____________________________________________________________________________________

# PROTECTED

class college:
    _college_name = "IES UNIVERSITY"
    _branch = "CSE"
    _fee = "1L"

c = college()
print(c._college_name)
print(c._branch)
print(c._fee)

#_____________________________________________________________________________________

#PRIVATE

class college:
    __college_name = "IES UNIVERSITY"
    __branch = "CSE"
    __fee = "1L"

c = college()
print(c.__college_name)
print(c.__branch)
print(c.__fee)