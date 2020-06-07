class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    def do_something(self):
        print("Method Defined In: B")
        super().do_something()

class C(A):
    def do_something(self):
        print("Method Defined In: C")

class D(B,C):
    def do_something(self):
        print("Method Defined In: D")
        super().do_something()

thing = D()
thing.do_something()


#        A
#      /   \
#     B     C
#      \   /
#        D
#D,B,C,A,Object

print(D.__mro__)
print(D.mro())
help(D)
