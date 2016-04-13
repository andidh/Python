'''
Created on Feb 5, 2016

@author: AndiD
'''


class UI:
    
    def __init__(self, scntr, gcntr):
        self.scntr = scntr
        self.gcntr = gcntr
        
    def menu(self):
        print("0 - Exit")
        print("1 - Add student")
        print("2 - Add laboratory")
        print("3 - Show all students")
        print("4 - Show all laboratories")
        print("5 - Filter by grade")
        print("6 - Delete by ID")
        
        
        
        
    def start(self):
        
        while True:
            self.menu()
            cmd = int(input("Give a command: "))
            
            if cmd == 0:
                break
            
            if cmd == 1:
                id = int(input("Give id: "))
                name = input("Give name: ")
                group = int(input("Give group: "))
                self.scntr.add(id, name, group)
                
            if cmd == 2:
                sid = int(input("Give student id: "))
                object = input("Give object: ")
                grade = int(input("Give grade: "))
                self.gcntr.addgrade(sid, object, grade)
                
            if cmd == 3:
                all = self.scntr.get_all()
                for s in all:
                    print(s)
                
            if cmd == 4:
                all = self.gcntr.get_all()
                for g in all:
                    print(g)
                    
            if cmd == 5:
                g = int(input("Give grade: "))
                gr = self.gcntr.filterGrade(g)
                for s in gr:
                    print(s)
                    
            if cmd == 6:
                id = int(input("Give id: "))
                self.scntr.delete(id)
                