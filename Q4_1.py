import utilities as li

#read matrix and partial pivot
A,c_A=li.matrix_r("A")
B,c_B=li.matrix_r("B")
A,B=li.partial_pivot(A,B,c_B)
# A=1,0,1,2         B=6
#   0,1,-2,0         -3
#   1,2,-1,0         -2
#   2,1,3,-2         0


def L_Udec(A):
    for j in range(c_A):
        for i in range(len(A)):

            #diagonal
            if i==j:
                sum=0
                for u in range(i):
                    sum=sum+A[i][u]*A[u][i]
                A[i][i]=A[i][i]-sum

                #elements of upper triangle
            if i<j:
                sum=0
                for k in range(i):
                    sum=sum+A[i][k]*A[k][j]
                A[i][j]=A[i][j]-sum

                #elements of lower triangle
            if i>j:
                sum=0
                for z in range(j):
                    sum=sum+A[i][z]*A[z][j]
                A[i][j]=(A[i][j]-sum)/A[j][j]
    return(A)

def forw_backw(A,B,col):
    for k in range(col):
        r=len(A)

        #forward substitution
        Y=[[0] for y in range(r)]
        for i in range(r):
            sum=0
            for k in range(i):
                sum=sum+A[i][k]*Y[k][0]
            Y[i][0]=B[i][0]-sum
        print("matrix Y",Y)

        #backward substitution
        X=[[0] for w in range(r)]
        for l in range(r-1,-1,-1):
            sum=0
            for m in range(l+1,r):
                sum=sum+A[l][m]*X[m][0]
            X[l][0]=(Y[l][0]-sum)/A[l][l]
    print("solution matrix is",X)

L_Udec(A)
forw_backw(A,B,c_B)
#output:
# matrix Y [[6], [-3.0], [-2.0], [-6.0]]
# solution matrix is [[1.0], [-1.0], [1.0], [2.0]]
