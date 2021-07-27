def bubble_sort(arr):
    arr_len=len(arr)
    if arr_len<=1:
        print('sorting cannot be done as there is only one element')
    else:
        for i in range(len(arr)):
            for j in range (0,arr_len-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
bubble_sort(arr) 
print ("Sorted array is:") 
for i in range(n):
    print ("%d" %arr[i]), 
