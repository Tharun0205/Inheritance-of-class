class A:
    print("i'm class A")
class B(A):
    print("I'm class B")
p=A()
class A:
    def __init__(self):
        A.__init__(self)