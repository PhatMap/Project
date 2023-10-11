def SmallestSelect(A, count):
    key = A[count]
    index_key = count
    for index, i in enumerate(A[count+1:], count+1):
        if key > A[index]:
            key = A[index]
            index_key = index
    return key, index_key

def SmallestSort(A):
    count = 0
    for i in range(len(A)-1):
        initV, initI = SmallestSelect(A, count)
        count+=1
        A[i], A[initI] = initV, A[i]
    return A
        


A = [-1,2,1,3]
print(SmallestSort(A))
