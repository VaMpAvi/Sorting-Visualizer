import time 
def partition(array,arr,lb,ub,color) :
    pivot=arr[lb]
    start=lb
    end=ub
    while start < end :
        time.sleep(0.001)
        color=["violet" if k==lb else "red" if k==start or k==end else "green" for k in range(len(arr))]
        array(arr,color)
        while start <=end and arr[start]<=pivot :
            start+=1 
        while start<=end and arr[end]>pivot :
            end-=1 
        if start < end :
            arr[start],arr[end]=arr[end],arr[start]
    arr[end],arr[lb]=arr[lb],arr[end]
    return end

def quicksort(array,arr,lb,ub,color) :
    if lb < ub :
        loc=partition(array,arr,lb,ub,color)
        quicksort(array,arr,lb,loc-1,color)
        quicksort(array,arr,loc+1,ub,color)
    if lb==0 and ub==len(arr)-1 :
        array(arr,["blue" for k in range(len(arr))])