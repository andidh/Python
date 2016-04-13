from Menu import *

from Print import *
    
    
    
def menu_ui(l,ant): 
    options={1:add_ui,2:modify_ui,3:compare_ui,4:evaluate_ui,5:filter_ui,6:undo_ui, 7:redo_ui}
    printMenu()
    cmd=input("Option: ")
    if cmd!='x':
        try:
            cmd=int(cmd)
            options[cmd](l,ant)
        except ValueError:
            print("Invalid input")
        except KeyError:
            print("This key is not implemented")
            
            
def add_ui(l,ant):
    lista=[]
    options={'a':print_AddNew, 'b':print_Score}
    while True:
        printAdd()
        cmd=input("Option: ")
        if cmd=="m":
            menu_ui(l,ant)
            break
        try:
            lista.append(l[:])
            options[cmd](l,ant)
        except ValueError as msg:
            print(msg)
            
def modify_ui(l,ant):
    lista=[]
    options={'a': print_DelPoz, 'b': print_DelFrom, 'c': print_Replace}
    while True:
        printModify()
        cmd=input("Option: ")
        if cmd=="m":
            menu_ui(l,ant)
            break
        try:
            lista.append(l[:])
            options[cmd](l,ant)
        except ValueError as msg:
            print(msg)

def compare_ui(l,ant):
    options={'a': print_Minim, 'b': print_Sort, 'c': print_Maxim}
    while True:
        printCompare()
        cmd=input("Option: ")
        if cmd=="m":
            menu_ui(l,ant)
            break
        try:
            options[cmd](l)
        except ValueError as msg:
            print(msg)

def evaluate_ui(l,ant):
    options={'a':print_Avrg, 'b': print_Min, 'c': print_Multiple}
    while True:
        printEvaluate()
        cmd=input("Option: ")
        if cmd=="m":
            menu_ui(l,ant)
            break
        try:
            options[cmd](l)
        except ValueError as msg:
            print(msg)

def filter_ui(l,ant):
    options={'a': print_FilterMul, 'b': print_FilterMin}
    while True:
        printFilter()
        cmd=input("Option: ")
        if cmd=="m":
            menu_ui(l,ant)
            break
        try:
            options[cmd](l)
        except ValueError as msg:
            print(msg)

def undo_ui(l,ant):
    options={'a':print_Undo}
    while True:
        printUndo()
        opt=input("Option: ")
        if opt=="m":
            menu_ui(l,ant)
            break
        try:
            options[opt](l,ant)
        except ValueError as msg:
            print(msg)
    
def redo_ui(l, ant):
	options={'a':print_Redo}
	while True:	
		printRedo()
		opt=input("Option: ")
		if opt=="m":
			menu_ui(l,ant)
			break
		try:
			options[opt](l,ant)
		except ValueError as msg:
			print(msg)
			
def startui():
    l=[]
    ant=[]
    options={1:add_ui, 2:modify_ui, 3:compare_ui, 4:evaluate_ui, 5:filter_ui, 6:undo_ui, 7:redo_ui}
    printMenu()
    cmd=input("Option: ")
    if cmd!='x':
        try:
            cmd=int(cmd)
            options[cmd](l,ant)
        except ValueError:
            print("invalid input")
        except KeyError:
            print("This key is not implemented")
            
    
startui()