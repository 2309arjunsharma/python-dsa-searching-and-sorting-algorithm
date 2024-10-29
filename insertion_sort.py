def insertion_sort(arr):
    n=len(arr)
    for i in range(1,len(arr)):
        current=arr[i]
        c=i-1
        while c>=0 and current<arr[c]:
            arr[c+1]=arr[c]
            c-=1
        arr[c+1]=current
    return arr

lst=[12,25,65,23,90]
result=insertion_sort(lst)
print(result)
