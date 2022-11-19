
class Rectangle:
    def __init__(self,*args):
        if len(args)==0:
            self.l=0
            self.b=0
        elif len(args)==1:
            self.l=args[0]
            self.b=args[0]
        elif len(args)==2:
            self.l=args[0]
            self.b=args[1]
        
    
    def area(self):
        return self.l*self.b
obj1=Rectangle()
obj2=Rectangle(5,4)
obj3=Rectangle(6)
print(obj1.area())
print(obj2.area())
print(obj3.area())
