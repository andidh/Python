from utility import *

def AddNew(l):
    '''
    Description: adds a new participant in the list
    Input: l- the list with participants
            score - the sum of all the notes
    Output- l- the updated list
    '''
    score=sum()
    l.append(score)
    
def AddScore(poz,l,s):
    '''
    Add the score for a new participant on a given position
    Input: -poz is integer and represents the position 
           -s is integer and represents the score 
    Output: -l the updated list
    '''
    l.insert(poz,s)
    return l


def DelPoz(l, poz):

    ''' Delete the score of a pariticipant on a given value
    -poz is integer and shows the index of the participant
    '''
    
    l[poz]=0
    return l

    
def DelFrom(n, m, l):
    
    '''Delete multiple participants
    m is integer and represents the the index of the first participant to be deleted
    n is integer and represents the index until the deleting process takes place
    '''

    del l[n:m]
    return l
    

    
def Replace(l, poz, s):

    '''Replace the score of a participant with another score
    poz is the index of the participant
    s is the score 
    ''' 
    
    l[poz]=s
    return l


def Minim(n,l):

    '''Description: Return all the participants with score less than a given Value
    Input: n- a given value
    Output: c-the list with participants
    '''
    c=[]
    for i in range(0,len(l),1):
        if l[i] < n:
            c=c+[i]
    return c

def Sort(l):
    '''
    Description: Returns the participants sorted in a certain order, considering their scores
    Input: l- the list with participants
    Output: l- sorted list
    '''
    poz=[]
    for i in range(len(l)):
        poz.append(i)
        
    for i in range (len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                aux=l[i]
                l[i]=l[j]
                l[j]=aux
                aux=poz[i]
                poz[i]=poz[j]
                poz[j]=aux
    return poz


def Maxim(n,l):
    '''Description: writes the participants having the score greater than a given value
        Input: n- the given value
        Output: c - the sorted list of scores greater than a given value
        '''
    c=[]
    for i in l:
        if i>n:
            c.append(i)
    return c



def Avrg(n,m,l):
    '''Description: Writes the average of the scores for given participants
    Input: n- the first participant
           m-the last participant
    Output: s- the average of scores
    '''
    k=m-n+1
    s=0
    for i in range(n,m+1,1):
        s=s+l[i]
    s=s/k
    return s


def Min(n,m,l):
    '''
    Description: writes the lowest score of the participants in an given interval
    Input: n - the first participant
           m - the last participant
    Output: min - the lowest score    
    '''
    min=l[n]
    for i in range(n+1,m+1,1):
        if l[i]<min:
            min=l[i]
    return min
   
def TenMultiple(n,m,l):
    '''
    Description: writes the scores multiple of 10 of the given participants 
    Input: n - the first participant
           m - the last participant
    Output: c- the list with scores multiple of 10
    '''
    c=[]
    for i in range(n,m+1,1):
        if Multiple(l[i],10)==True:
            c=c+[l[i]]
    return c

def FilterMul(n,l):
    '''
    Description: retains only the participants that have the score multiple of a given value
    Input: n- the given value
            l- the list with the scores
    Output: c- list with filtered participants    '''
    c=[]
    for i in range(0,len(l),1):
        if Multiple(l[i],n)==True:
            c=c+[i]
    return c

def FilterMin(n,l):
    '''
    Description: retains only the participants having scores greater than a given value
    Input: n- a given value
            l- list with the score
    Output: c- the filtered list
    '''
    c=[]
    for i in range(0,len(l),1):
        if l[i]<n:
            c=c+[i]
    return c


def AddPrevious(l,ant):
    '''
    Description: Adds the curent list to the previous
    ant-the list with anterior list
    l-curent list
    '''
    n=len(ant)
    ant.append([])
    ant[n][:]=l[:]
    
def Undo(l,ant):
    '''
    Description: the last operation that has modified the list of scores is cancelled.
    ant-the list with anterior list
    l-curent list
    return Error when there are not previous operations
    '''
    if ant==[]:
        raise ValueError("There do not exist any previous operations")
    else:
        l=ant.pop()
        return l

def Redo(l, ant):
    '''
    Description: Redo the cancelled operation
    ant - the list with anterior list
    l-current list
    '''
    if l == []:
        raise ValueError("There do not exist any previous operations")
    else:
        l.extend(ant[-1])
        return l

