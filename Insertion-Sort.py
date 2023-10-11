def NonDecreasing(A):
    for j, value in enumerate(A[1:], start=1):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i-=1
        A[i+1] = key

def NonIncreasing(A):
    for j, value in enumerate(A[1:], start=1):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i-=1
        A[i+1] = key
    
def BinaryPlus(A , B, C):
    n = len(A)
    carry = 0
    for i in range(n-1):
        bit_sum = A[i] + B[i] + carry
        
        C.append(int(bit_sum%2))
        carry = int(bit_sum/2)
    C.insert(0, carry)

A = [1,0,0,1,1]
B = [0,1,1,1,0]
C = []  

NonDecreasing(A)
print(A)