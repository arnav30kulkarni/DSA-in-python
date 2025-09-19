A = [-3,-1,0,1,4,7]

# traditional binary search - lookup in array
#Time complexity - O(log n)
#Space complexity - O(1)

def binary_search(arr,target):
    n = len(arr)
    L = 0 
    R = n-1

    while L<=R:
        M = L + (R-L)//2  #or (L+R)//2
        if arr[M] == target:
            return arr[M]
        elif arr[M]>target:
            R = M - 1 
        else:
            L = M + 1
    return None

result = (binary_search(A,7))
if result is not None:
    print("Found:",result)
else:
    print("not found")


# Based on a condition 
B = [False,False,False,True,True,True]

def binary_search_condition(arr):
    n = len(arr)
    L = 0 
    R = n - 1 
    while L < R: 
        M = L + (R-L)//2
        if arr[M]:
            R = M 
        else:
            L = M + 1 

    return L 

print(binary_search_condition(B))