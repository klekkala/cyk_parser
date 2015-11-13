##input_list = [i.strip().split() for i in open("input_cyk.txt").readlines()]


import numpy as np

#a is an array consisting of non-terminal symbols
a = ['#','a','b','a','a','b']
#a = ['#','b','a','a','b','a']
#a = ['#','b','a','b','b','b']
#n is the number of characters
n = len(a)


#Dummy list
D = ['#']


#terminals list
Q1 = ['#']
A1 = ['#','a']
B1 = ['#','b']
C1 = ['#','a']
R1 = [D,Q1,A1,B1,C1]


#non terminals list
#R is a list consisting of n characters
Q = ['#',(2,3),(3,4)]
A = ['#',(3,2)]
B = ['#',(4,4)]
C = ['#',(2,3)]
R = [D,Q,A,B,C]
S = [D,Q]



#r is the number of non-terminal symbols
r = len(R)
r1 = len(R1)
#P is a 3D dimetional array. Initialized to zeroes.
P=np.zeros((n,n,r))

#function to find the index of the non-terminal symbol
def find_ind(l,m):
	Z=[]
	for i in range(1,len(R)):
		for j in range(1,len(R[i])):
			#print i,j
			if R[i][j][0]==l and R[i][j][1]==m:
				Z.append(i)
	
	return Z
	

##for loop for setting the terminals
for i in range(1,len(a)):
	for j in range(1,len(R1)):
		for k in range(1,len(R1[j])):
		
			if R1[j][k]==a[i]:
				P[1,i,j]=1




##for loop for substring of length greater than 1
for i in range(2,n):
	for j in range(1,n-i+1):
		for k in range(1,i):
			for l in range(1,r):
				for m in range(1,r):
					if P[k,j,l]==1 and P[i-k,j+k,m]==1:

						Z = find_ind(l,m)
						for a in range(0,len(Z)):
							P[i,j,Z[a]] = 1

print P
for i in range(1,len(S)):
	if P[n-1][1][i] == 1:
		print "yes"
	else:
		print "no"
