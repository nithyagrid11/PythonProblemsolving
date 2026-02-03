def Swap(a,b):
    temp = a
    a = b
    b = temp
    return (a,b)
print(Swap(3,4))

def Swap1(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]
arr = [1,2,3,4,5,6]
Swap1(arr,1,3)
print(arr)