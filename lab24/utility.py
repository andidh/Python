
def sum():
    '''
    Description: calculates the sum of all notes and returns the final score
    '''
    s=0
    for i in range(0,10,1):
        n=int(input("Give the note: "))
        while(n>10 or n<0):
            n=int(input("The notes must be between 0 and 100. Give another score: "))
        s=s+n
    return s

def Multiple(mul,nr):
    '''
    Checks if a number is a multiple of another number
    Output - True if the number is a multiple
    		- False if the number is not a multiple
    '''
    if mul%nr==0:
        return True
    else:
        return False