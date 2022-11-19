class CTECH:
    pass
class CINTEL:
    pass
class NWC:
    pass
class DSBS:
    pass
obj1=CTECH()
obj2=CINTEL()
obj3=NWC()
obj4=DSBS()
print(isinstance(obj1,CTECH))
print(isinstance(obj2,CINTEL))
print(isinstance(obj3,NWC))
print(isinstance(obj4,DSBS))
print(isinstance(CTECH,object))