from functions import AddScore, DelPoz, DelFrom, Replace, Minim, Sort, Maxim, Avrg, Min, TenMultiple, FilterMul, FilterMin

def testInit(l):
	l.append(89)
	l.append(73)
	l.append(81)
	return l

def testScore():
	assert AddScore(1, [89, 77, 81], 73) == [89, 73, 77, 81]
	assert AddScore(0, [32, 67, 90], 88) == [88, 32, 67, 90]
	print("True")
testScore()

def testDelPoz():
	assert DelPoz([89, 70, 81], 1) == [89, 81]
	assert DelPoz([83, 45, 90, 61], 2) == [83, 45, 61]
	print("True")
testDelPoz()

def testDelFrom():
	assert DelFrom([30, 78, 90, 67, 82], 0, 2) == [90, 67, 82]
	assert DelFrom([89, 37, 84, 58], 0, 3) == [58]
	print("true")
testDelFrom()

def testReplace():
	
	assert Replace([32, 43, 90, 55], 1, 88) == [32, 88, 90, 55]
	assert Replace([67, 90, 32, 47], 3, 100) == [67, 90, 32, 100]
	print("True")
testReplace()

def testMinim():
    assert Minim(25,[14,78,36])==[0]
    assert Minim(19,[25,64,11,6,5])==[2,3,4]
    assert Minim(60,[78,89,77])==[]
testMinim()

def testSort():
    assert Sort([65,14,98,25,30])==[1,3,4,0,2]
    assert Sort([14,98])==[0,1]
    assert Sort([98,15])==[1,0]
testSort()
    
def testMaxim():
    assert Maxim(64,[70,15,65,20,99])==[2,0,4]
    assert Maxim(15,[78,45,13,64,100])==[2,1,3,0,4]
    assert Maxim(47,[15,64,26])==[1]
    assert Maxim(100,[68,55,14])==[]
testMaxim()
    
def testAvrg():
    assert Avrg(0,2,[50,70,90,14])==70.0
    assert Avrg(0,1,[100,100,100,100])==100.0
    assert Avrg(2,4,[100,58,50,60,70])==60.0
testAvrg()
    
def testMin():
    assert Min(0,2,[100,26,90,45,7])==26
    assert Min(1,2,[52,10,56])==10
    assert Min(0,4,[45,58,47,99,20])==20
testMin()
   
def testMultiple():
    assert TenMultiple(2,[3,6,5,4])==[0,2]
    assert TenMultiple(6,[3,12,19,24,6])==[0,2]
    assert TenMultiple(4,[3,2,6,])==[0,1,2]
testMultiple()

def testFilterMul():
    assert FilterMul(2,[3,6,5,4])==[0,2]
    assert FilterMul(6,[3,12,19,24,6])==[0,2]
    assert FilterMul(4,[3,2,6,])==[0,1,2]
testFilterMul()
   
def testFilterMin():
    assert FilterMin(50,[15,18,14,25])==[]
    assert FilterMin(15,[12,65,47])==[1,2]
    assert FilterMin(5,[14,98,45])==[0,1,2]
testFilterMin()

