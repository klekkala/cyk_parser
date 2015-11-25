######################Author: Kiran Kumar Lekkala#######################
#####Description: processing the input from the grammer file############
def input_process():
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

    return Q
    

