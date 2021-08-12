import time
def merge(array,arr,lb,mid,ub,speed) :
    sample=[]
    s=arr.copy()
    i=lb
    j=mid+1 
    while i<=mid and j<=ub :
        time.sleep(0.05*speed)
        array(arr,["red" if k==i or k==j else "green" for k in range(len(arr)) ])
        if arr[i]<=arr[j] :
            sample.append(arr[i])
            i+=1
        else :
            sample.append(arr[j])
            j+=1
            
    if i <=mid :
        sample.extend(arr[i:mid+1])
    elif j<=ub :
        sample.extend(arr[j:ub+1])
    i=0
    for k in range(lb,ub+1) :
        arr[k]=sample[i]
        time.sleep(0.001*speed)
        array(arr,["red"if t==k else "green" for t in range(len(arr)) ])
        i+=1
def mergesort(array,arr,lb,ub,speed) :
    if lb < ub :
        mid=(lb+ub)//2
        mergesort(array,arr,lb,mid,speed)
        mergesort(array,arr,mid+1,ub,speed)
        merge(array,arr,lb,mid,ub,speed)
        time.sleep(0.01)
        array(arr,[ "green" for k in range(len(arr))])