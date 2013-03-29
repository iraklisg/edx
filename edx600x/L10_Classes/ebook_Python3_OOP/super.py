class A(object):
    def routine(self):
        print 'A.routine'
class B(A):
    def routine(self):
        print 'B.routine'
        super(B,self).routine()
class C(A):
    def routine(self):
        print 'C.routine'
        super(C,self).routine()
class D(A):
    def routine(self):
        print 'D.routine'
        super(D,self).routine()
class E(B,D,C):
    def routine(self):
        print 'E.routine'
        super(E,self).routine()

e=E()
e.routine()