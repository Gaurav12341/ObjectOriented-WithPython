class PrintDT:
    def py_data(self,list):
        self.list=[]
        print(self.list)
        
    def py_data(self,tuple):
        self.tuple=()
        print(tuple)
        
    def py_data(self,str):
        self.str=''
        print(str)
        
p=PrintDT()
p.py_data([1,2,3])
p.py_data(('H',[8,4,6],"Worldd"))
p.py_data('Broo')
