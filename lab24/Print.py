from functions import AddNew, AddPrevious, AddScore, DelPoz, DelFrom, Replace, Minim, Sort, Maxim, Avrg, Min, \
	TenMultiple, FilterMul, FilterMin, Undo, Redo
    
    
def print_AddNew(l,ant):
    AddPrevious(l,ant)
    AddNew(l)
    print(l)
    
def print_Score(l, ant):
	
	poz=int(input("Add score on position: "))
	if poz<0 or poz>len(l)-1:
		raise ValueError("The number is not on the list")
	s=int(input("The score: "))
	if s<0 or s>100:
		raise ValueError("The score must be between 0 and 100" )
	AddPrevious(l,ant)
	AddScore(poz, l, s)
	print(l)
    
def print_DelPoz(l, ant):
	poz=int(input("Delete score on position: "))
	if poz<0 or poz>len(l)-1:
		raise ValueError("The number is not on the list")
	AddPrevious(l, ant)
	DelPoz(l, poz)
	print(l)
	
def print_DelFrom(l, ant):
	n=int(input("Delete participants from position: "))
	if n<0 or n>len(l)-1:
		raise ValueError("The number is not on the list")
	m=int(input("Until position: "))
	if m<0 or m>len(l)-1:
		raise ValueError("The number is not on the list")
	AddPrevious(l, ant)
	DelFrom(n,m,l)
	print(l)    
    
def print_Replace(l, ant):
	poz=int(input("Replace the note on position: "))
	if poz<0 or poz>len(l)-1:
		raise ValueError("The number is not on the list")
	s=int(input("With the score: "))
	if s<0 or s>100:
		raise ValueError("The score must be between 0 and 100" )
	AddPrevious(l, ant)
	Replace(l,poz, s)
	print(l)	

def print_Minim(l):
    n=int(input("Give a value: "))
    if n<0 or n>100:
        raise ValueError("The score must be between 0 and 100")
    print(Minim(n,l))

def print_Sort(l):
	print(Sort(l))

def print_Maxim(l):
	n=int(input("Give a value: "))
	if n<0 or n>100:
	    raise ValueError("The score must be between 0 and 100")
	print(Maxim(n,l))

def print_Avrg(l):
    n=int(input("Give the first participant: "))
    if n<0 or n>len(l)-1:
        raise ValueError("The participant does not exist")
    m=int(input("Give the last participant: "))
    if m<0 or m>len(l)-1:
        raise ValueError("The participant does not exist")
    print(Avrg(n,m,l))
    
def print_Min(l):
    n=int(input("Give the first participant: "))
    if n<0 or n>len(l)-1:
        raise ValueError("The participant does not exist")
    m=int(input("Give the last participant: "))
    if m<0 or m>len(l)-1:
        raise ValueError("The number does not exist")
    print(Min(n,m,l))
    
def print_Multiple(l):
	n=int(input("Give the first number: "))
	if n<0 or n>len(l)-1:
	    raise ValueError("The participant does not exist")
	m=int(input("Give the last participant: "))
	if m<0 or m>len(l)-1:
	    raise ValueError("The participant does not exist")
	print(TenMultiple(n,m,l))

def print_FilterMul(l):
    n=int(input("Give a number: "))
    print(FilterMul(n,l))
    
def print_FilterMin(l):
    n=int(input("Give a score: "))
    if n<0 or n>100:
        raise ValueError("The score must be between o and 100 ")
    print(FilterMin(n,l))
    
def print_Undo(l,ant):
    l=Undo(l,ant)
    print(l)  

def print_Redo(l, ant):
	l=Redo(l, ant)
	print(l)
	
