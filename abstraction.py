# here we create count as a private member that's why 
class Employee:
    __count = 0
    def __init__(self):
        Employee.__count = Employee.__count+1
    def display(self):
        print("The number of employees",Employee.__count)
emp = Employee()
# emp2 = Employee()
try:
    print(emp.__count)
except:
    print("this is the private member")
finally:
    emp.display()


# class Employee:
#     count = 0
#     def __init__(self):
#         Employee.count = Employee.count+1
#     def display(self):
#         print("The number of employees",Employee.count)
# emp = Employee()
# emp2 = Employee()
# try:
#     print(emp.count)
# finally:
#     emp.display()