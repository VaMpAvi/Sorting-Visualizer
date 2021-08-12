import time
def Bubble_sort (array,a,color,speed) :
    s=len(a)
    for i in range(s-1) :
        flag =0
        for j in range(s-1-i) :
            color=["blue" if (j==s-2-i or color[k]=="blue") and k>=len(a)-1-i  else "red" if k==j or k==j+1  else "green" for k in range(len(a))]
            array(a,color)
            if len(a)<=10 :
                time.sleep(1*speed)
            elif len(a)>=70 :
                time.sleep(0.001*speed)
            else :
                time.sleep(0.01*speed)
            if a[j+1]<a[j] :
                a[j+1],a[j]=a[j],a[j+1]
                flag=1    
        if flag==0 :
            break
    array(a,["blue" for i in range(len(a))])

