import random
import math

def genDiskAccesses(num,lower,upper): #Generates random disk accesses
	accessList = []
	for i in range(num):
		randomval = random.randint(lower,upper)
		accessList.append(randomval)
		return accessList

def FCFS(accessList,startPos):
	currentPos=startPos
	tracksTraversed=0
	for value in accessList:
		diff = math.fabs(currentPos-value)
		tracksTraversed+=diff
		currentPos=value
	return tracksTraversed

def closestSeek(accessList,currentPos): #Returns closest guy in list given current pos
	minimum = 99999999
	nextPos=0
	for value in accessList:
		if(math.fabs(currentPos-value)<minimum):
			nextPos=value
			minimum = math.fabs(currentPos-value)
	return nextPos

def closestSeekFirst(p_accessList,startPos):
	
	accessList=[]
	for value in p_accessList:
		accessList.append(value);

	currentPos=startPos
	tracksTraversed=0
	while(len(accessList)>0):
		nextSeek = closestSeek(accessList,currentPos)
		#print("Next Seek  : ",nextSeek)
		tracksTraversed+=math.fabs(currentPos-nextSeek)
		accessList.remove(nextSeek)
		currentPos=nextSeek
	return tracksTraversed

def scan(p_accessList,startPos,maxEndPos): #Head always moves from lower to higher first
	
	accessList=list(p_accessList)
	accessList.sort()
	currentPos=startPos
	tracksTraversed=0
	
	for value in accessList:
		if(value>=currentPos):
			tracksTraversed+=value-currentPos
			currentPos=value

	if(accessList[0]>=startPos):
		pass
	else:
		tracksTraversed+=maxEndPos-currentPos
		accessList.reverse()
		currentPos=maxEndPos
		for value in accessList:
			if(value<currentPos):
				tracksTraversed+=currentPos-value
				currentPos=value;


	return tracksTraversed
	


	return tracksTraversed
	
def cscan(p_accessList,startPos,maxPos,lowerMaxPos): #Assuming head always reads going from lower to higher
	
	accessList = list(p_accessList)
	accessList.sort();
	currentPos=startPos;
	tracksTraversed=0;

	for value in accessList:
		if(value>=currentPos):
			tracksTraversed+=value-currentPos;
			#print(tracksTraversed)
			currentPos=value;

	if(accessList[0]>=startPos):
		pass;
	else:
		tracksTraversed+=maxPos-currentPos
		#print(tracksTraversed)
		currentPos=lowerMaxPos
		tracksTraversed+=maxPos-lowerMaxPos
		#print(tracksTraversed)
		for value in accessList:
			if(value<startPos):
				tracksTraversed+=value-currentPos
				currentPos=value;

	return tracksTraversed


tempAccessList = [10,50,30,20,40]
print("FCFS : ",FCFS(tempAccessList,10))
print("Shortest Seek First : ",closestSeekFirst(tempAccessList,10))
print("SCAN : ",scan(tempAccessList,50,100))
print("CSCAN : ",cscan(tempAccessList,50,100,0))