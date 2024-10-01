# class A:
#     def sum(self):
#         print("A")
# class B:
#     def sum(self):
#         print("B")
# class C(B,A):
#     def add(self):
#         print("C")
    
# d = C()
# d.sum()


# class A:
#     def sum(self):
#         print("A")
# class B(A):
#     def sum(self):
#         print("B")
# class C(B):
#     def add(self):
#         print("C")
# d = C()
# d.sum()
# d.sum()
# d.add()


# original sub sup
# (sub,sup) this is the format to write subscript and superscript to check if it is subscript or superscript

class C1:
    def Summation(self,a,b):
        return a+b
class C2:
    def Multiplication(self,a,b):
        return a*b
class D1(C1,C2):
    def Divide(self,a,b):
        return a/b
d = D1()

# print(issubclass(D1,C2))  True
# print(issubclass(C1,C2))

# print(issubclass(C2,D1))    False
# print(issupclass(C1,C2))



class A:
    def amit():
        print("amit")
class B:
    def amit():
        print("anurag")
b = B()
b.amit()