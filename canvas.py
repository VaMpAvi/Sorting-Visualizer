from tkinter import *
from tkinter import ttk
import random
from Bsort import Bubble_sort
from Msort import mergesort
from ins import insertionSort,selectionSort
from Qsort import quicksort

root=Tk()
root.title("Sorting visualizer")
root.maxsize(900,600)
root.config(bg="Yellow")
f=Frame(root,width=880,height=160,bg="Yellow")
f.grid(row=0,column=0,padx=10,pady=5)

canvas=Canvas(root,width=880,height=410,bg="black")
canvas.grid(row=1,column=0,padx=10,pady=5)

global no
no=IntVar()
l=Label(f,text="Select Size")
l.grid(row=0,column=5,padx=5,pady=5)
size_=Scale(f,from_=5,to=100,variable=no,orient=HORIZONTAL,length=140)
size_.grid(row=0,column=6,padx=5,pady=5,sticky=W)

Label(f,text="Select Speed").grid(row=0,column=2)
speed_=Scale(f,from_=0.1,to=2,resolution=0.1,length=130,orient=HORIZONTAL)
speed_.grid(row=0,column=3,columnspan=2,padx=5,pady=5,sticky=E)

Label(f,text="Algorithms").grid(row=0,column=0,padx=5,pady=5,sticky=W)
global var
var=StringVar()
algo=ttk.Combobox(f,textvariable=var)
algo.grid(row=0,column=1,padx=5,pady=5,sticky=E)
algo["value"]=("Bubble sort","Merge sort","Quick sort","Insertion sort","Selection sort")
algo.current(0)

def genArray() :
    global data
    data=[ random.randrange(5,250,2) for i in range(no.get())]
    #print(data)
    array(data,['green']*no.get())


def array(data,color) :
    canvas.delete(ALL)
    if no.get() <=50 :
        x1=200-no.get()-5
    elif no.get() >=90:
        x1=100-no.get()+5
    else :
        x1=100-no.get()+10
    y1=0
    for i in range(no.get()) :
        if no.get() <=90:
            x=x1+5
        else :
            x=x1+4.6
        y=20+(data[i]*1.5)
        x1=x+400/no.get()
        y1=0
        rect=canvas.create_rectangle(x,y,x1,y1,fill=color[i])
    root.update_idletasks()

def algo_() :
    global data,color,var,gen,root
    gen.config(state=DISABLED)
    sort.config(state=DISABLED)
    algo.config(state=DISABLED)
    speed_.config(state=DISABLED)
    size_.config(state=DISABLED)
    root.config(cursor='NONE')
    if var.get()=="Bubble sort" :
        Bubble_sort(array,data,['green']*(no.get()),speed_.get())
    elif var.get() =="Merge sort":
        mergesort(array,data,0,len(data)-1,speed_.get())
    elif var.get()=="Insertion sort":
        insertionSort(array,data,len(data))
    elif var.get()=="Selection sort":
        selectionSort(array,data,len(data),['green']*(no.get()))
    else :
        quicksort(array,data,0,len(data)-1,['green']*(no.get()))
    gen.config(state=ACTIVE)
    sort.config(state=ACTIVE)
    algo.config(state=ACTIVE)
    speed_.config(state=ACTIVE)
    size_.config(state=ACTIVE)
    root.config(cursor="")
    print(data)

gen=Button(f,text="Generate Array",padx=5,pady=5,command=genArray,width=14)
gen.grid(row=1,column=6,sticky=NE)

sort=Button(f,text="Sort!",padx=5,pady=5,command=algo_,width=14,fg="Blue",bg="Black")
sort.grid(row=2,column=6,sticky=SE)

#rect=canvas.create_rectangle(5,100,10,0,fill="red")
root.mainloop()