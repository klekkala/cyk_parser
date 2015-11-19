##take the gramer as input from input_cyk.txt
input_list = [i.strip().split() for i in open("input_cyk.txt").readlines()]
import numpy as np

#a is an array consisting of non-terminal symbols
input_file= open('string_cyk.txt','r');
input_string = input_file.read()
a = input_string.split()



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
