# insertion sorting

# takes an element & places it in correct order 

def insertion_sorted(arr):
    #start from second element
    for i in range(1,len(arr)):
        j = i 
        # swap backward until current element in right place 
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr 

data = [12,42,67,2,14]
print("unsorted:",data)

sorted_data = insertion_sorted(data)
print("sorted:",sorted_data)

# time complexity:O(N²) worst and avg , O(N) best (if sorted array)
# space complexity: O(1)