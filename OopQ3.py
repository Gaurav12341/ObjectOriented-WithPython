
class Dept:
    def __init__(self,*args):
        if len(args)==0:
            self.name='SCO'
            print(self.name)
        elif len(args)!=0:
            self.name=args
            print(self.name)
    

obj1=Dept()
obj2=Dept("Gaurav")
