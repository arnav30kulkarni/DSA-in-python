#Selection sorting

def selection_sorted(arr):
    #Step 1:- traversing the array
    for i in range(len(arr)):
        min_inx = i
    #step 2:- second for loop to traverse and find minimum 
        for j in range(i+1,len(arr)):
          if arr[j]<arr[min_inx]:
             min_inx = j
    #step 3:-swapping the index and min_inx(minimun index should take i'th index place)
        arr[i],arr[min_inx] = arr[min_inx],arr[i]
    return arr

data = [64,23,55,6,3,23,5]
print("unsorted", data)
sorted_data = selection_sorted(data)
print("sorted", sorted_data)

#Time complexity:- O(n²) (best,avg,worst-same case)
#Space complexity:-O(1)