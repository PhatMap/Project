def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p + i]) 
    for j in range(n2):
        R.append(A[q + j + 1])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else :
            A[k] = R[j]
            j += 1 

def Merge_Sort(A, p ,r):
    if p < r:
        q = int((p+r)/2)
        Merge_Sort(A, p, q)
        Merge_Sort(A, q + 1, r)
        Merge(A, p , q, r)
        
A = [0,0,0,2,4,5,7,1,2,3,6,0,0,0,7,0,9]
# Merge(A, 3, 6, 10)
Merge_Sort(A, 0, len(A)-1)
print(A)



