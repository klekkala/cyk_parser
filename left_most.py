
def get_left(P,Q,n,r,cur,F,char):
	
	F.append(char)
	for i in range(n-1,0):
		for j in range(1,n):
			for k in range(1,r):
				if P[i,j,k]!=0:
					get_left(P,Q,n,r,cur-1,k) 
















    F.append(1)
    for i in range(2,n):
        for j in range(2,r):
            if P[n-i,1,j]!=0:
                F.append(j)
                break

    mark = ['#',1,1,1,1]
    G.append('')
    for i in range(0,len(F)):
        G.append(Q[F[i]][mark[F[i]]][1])
        if mark[i] == len():
            mark[i] = len()

        else:
            mark[i]+=1




    print F,G

