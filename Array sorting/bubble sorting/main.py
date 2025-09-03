#bubble sorting

#pushes maximum to the last by adjacent swaps

def bubble_sorted(arr):
    #outerloop reverse\
    count = 0 
    for i in range(len(arr)-1,0,-1):
        count += 1
        #another for loop to check adjacent elements(should not include last index[i-1])
        sorted = True
        for j in range(i):
            #swap between index and the next number 
            if arr[j]>arr[j+1]:
                sorted = False
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if sorted == True:
            print(count)
            return arr
    print(count)
    return arr

data = [1,2,3,4,5]
print("unsorted:",data)
sorted_data = bubble_sorted(data)
print("sorted:",sorted_data)

# time complexity:O(N²) worst and avg , O(N) best (if sorted array)
# space complexity: O(1)