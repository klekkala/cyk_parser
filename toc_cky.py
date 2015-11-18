#############Author: Kiran Kumar Lekkala#############


##input_list = [i.strip().split() for i in open("input_cyk.txt").readlines()]


import numpy as np

#a is an array consisting of non-terminal symbols
a = ['#','a','b','a','a','b']
#a = ['#','b','a','a','b','a']
#a =  ['#','b','a','b','b','b']
#a = ['#','a','a','a','a']

input_file= open('string_cyk.txt','r');
input_string = input_file.read()
a = input_string.split()
#n is the number of characters
n = len(a)

input_list = [i.strip().split() for i in open("input_cyk.txt").readlines()]

D = ['#']
B = []
S = ['#',1]
Q = []
Q.append(D)

for i in range(0,len(input_list)):

	B.append('#')
	B = input_list[i][::2]
	Q.append(B)
	B = []

R = [item[0] for item in Q]


def find(a,b):
	for i in range(1,len(R)):
		if a == R[i]:
			tup1 = i
		if b == R[i]:
			tup2 = i
	return (tup1,tup2)
	

for j in range(1,len(Q)):
	for k in range(1,len(Q[j])):
		if len(Q[j][k])==2:
			Q[j][k] = find(Q[j][k][0],Q[j][k][1])

print Q
#r is the number of non-terminal symbols
r = len(Q)
#P is a 3D dimetional array. Initialized to zeroes.
P=np.zeros((n,n,r))

#function to find the index of the non-terminal symbol
def find_ind(l,m):
	Z=[]
	for i in range(1,len(Q)):
		for j in range(1,len(Q[i])):
			#print i,j
			if Q[i][j][0]==l and Q[i][j][1]==m:
				Z.append(i)
	
	return Z
	

##for loop for setting the terminals
for i in range(1,len(a)):
	for j in range(1,len(Q)):
		for k in range(1,len(Q[j])):
		
			if Q[j][k]==a[i]:
				P[1,i,j]=j


F = []
counter=0
##for loop for substring of length greater than 1
for i in range(2,n):
	for j in range(1,n-i+1):
		for k in range(1,i):
			for l in range(1,r):
				for m in range(1,r):
					if P[k,j,l]!=0 and P[i-k,j+k,m]!=0:

						Z = find_ind(l,m)
						for a in range(0,len(Z)):
							P[i,j,Z[a]] = Z[0]
							if a == 0 and counter==0:
								F.append(Z[a])
								counter=1
	counter=0
						
					

print P
print F
for i in range(1,len(S)):
	if P[n-1][1][S[i]] != 0:
		print "yes"
	else:
		print "no"
