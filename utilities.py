#read matrixes
def matrix_r(A):
    with open(A,"r") as fhand:
        M=[]
        N=[]
        for line in fhand:
          line=line.rstrip()
          li=list(line.split(","))
          c=len(li)
          M.append(li)
        r=len(M)
        c=len(M[0])
        A=[[0 for y in range(c)]for x in range(r)]

        for i in range(r):
          for j in range(c):
              A[i][j]=int(M[i][j])
        return(A,c)

#partial pivoting
def partial_pivot(a,b,col):
    """This function does partial pivoting of passed matrices"""
    r=len(a)
    for i in range(r):
        if a[i][i]==0:
            for k in range(i,col):
                if k==i or a[i][i]!=0:
                    continue
                else:
                    if abs(a[k][i])>abs(a[i][i]):
                        # c=b[i][col-1]
                        # b[i][col-1]=b[k][col-1]
                        # b[k][col-1]=c
                        for j in range(r):
                            pivot=a[i][j]
                            a[i][j]=a[k][j]
                            a[k][j]=pivot
                        for z in range(col):
                            c=b[i][z]
                            b[i][z]=b[k][z]
                            b[k][z]=c
    return a,b

#Gauss_Jordan elemination
def Gauss_Jordan(a,b,col):
    """Gauss Jordan method of decomposition"""
    for q in range(r):
        pivot=a[q][q]
        for l in range(q,r):
            a[q][l]= a[q][l]/pivot
            b[q][col]=b[q][col]/pivot
        for w in range(r):
            if a[w][q]==0 or q==w:
                continue
            else:
                factor=a[w][q]
                b[w][col]=b[w][col]-factor*b[q][col]
                for c in range(q,r):
                    a[w][c]=a[w][c]-factor*a[q][c]

    return a,b

#multiplication of matrice
def mult(M,N,col_N):
    r=len(M)
    E=[[0 for y in range(col_N)]for x in range(r)]
    I=[[1,0,0],[0,1,0],[0,0,1]]
    for i in range(r):
        for j in range(col_M):
            for k in range(r):
                E[i][j]+=M[i][k]*N[k][j]
    if E==I:
        print("result is identity matrix")
    for r in E:
        print(r)
