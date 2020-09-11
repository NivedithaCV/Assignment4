import utilities as li

#read matrix and partial pivot
A,c_A=li.matrix_r("C")
B,c_B=li.matrix_r("D")
A,B=li.partial_pivot(A,B,c_B)
r=len(A)
# A=0,2,8,6,         B=1,0,0,0
#   0,0,1,2            0,1,0,0
#   0,1,0,1            0,0,1,0
#   3,7,1,0            0,0,0,1
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

def matrix_det_LU(A):
    A=L_Udec(A)
    if len(A)==len(A[0]):
        det=1;
        for i in range(len(A)):
            det=det*A[i][i]
        if det!=0:
            print("inverse exit")
            return True
        else:
            print("inverse doesnot exit")
            return False
    else:
        raise ("given is not a square matrix")
        return False

def forw_backw(A,B,col):
    r=len(A)
    Y=[[0 for x in range(col)] for y in range(r)]
    X=[[0 for t in range(col)] for w in range(r)]
    for g in range(col):
        #forwardd substitution
        for i in range(r):
            sum=0
            for k in range(i):
                sum=sum+A[i][k]*Y[k][g]
            Y[i][g]=B[i][g]-sum

        #backward substitution
        for l in range(r-1,-1,-1):
            sum=0
            for m in range(l+1,r):
                sum=sum+A[l][m]*X[m][g]
            X[l][g]=(Y[l][g]-sum)/A[l][l]
            X[l][g]=round(X[l][g],4)
    print("matrix Y",Y)
    print("inverse matrix is",X)

def inverse(A,B,c_B):
    if matrix_det_LU(A)==True:
        forw_backw(A,B,c_B)

inverse(A,B,c_B)
# output:
# inverse exit
# matrix Y [[0, 0, 0, 1], [0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0], [1.0, -8.0, -2.0, 0.0]]
# inverse matrix is [[-0.2499, 1.6668, -1.8332, 0.3333], [0.0833, -0.6667, 0.8333, 0.0], [0.1666, -0.3334, -0.3334, 0.0], [-0.0833, 0.6667, 0.1667, -0.0]]
