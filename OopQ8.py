class Triangle:
    def __init__(self,a,b,c):
        self.a=int(a)
        self.b=int(b)
        self.c=int(c)
    def area(self):
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(0.5)
    def perimeter(self):
        return (self.a+self.b+self.c)
A=input("Enter A: ")
B=input("Enter B: ")
C=input('Enter C: ')
obj1=Triangle(A,B,C)
print("Perimeter of the triangle is: ",obj1.perimeter())
print("Area of the triangle is: ",obj1.area())
