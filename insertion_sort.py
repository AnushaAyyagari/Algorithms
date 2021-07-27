def insertion_sort(arr):
    arr_len=len(arr)
    i=0
    for i in range(1,arr_len):
        print('the ith element is',arr[i])
        for j in range(0,i):
            print('the jth element is',arr[j])
            if arr[j]>=arr[i]:
                print('the jth element {} is greater than {}'.format(arr[j],arr[i]))
                arr[j],arr[i]=arr[i],arr[j]
                #j=j+1

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
insertion_sort(arr) 
print ("Sorted array is:") 
for i in range(n):
    print ("%d" %arr[i]), 
