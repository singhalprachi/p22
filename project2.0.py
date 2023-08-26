from tkinter import*
from tkinter import ttk
y=0
a=ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root = ttk.Frame(a)

def quiz(y):
    a.add(frame1,text="Q1")
    a.add(frame2,text="Q2")
    a.add(frame3,text="Q3")
    a.add(frame4,text="Q4")
    a.add(frame5,text="Q5")


    Label(frame1, text = "Total keywords in Python ?" , font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame1,text="33",font=("Arial",20,"bold"),bg="light blue",command=a1_right).grid(row=3,column=1)
    Button(frame1,text="31",font=("Arial",20,"bold"),bg="light green",command=a1_wrong).grid(row=3,column=2)
    Button(frame1,text="30",font=("Arial",20,"bold"),bg="light pink",command=a1_wrong).grid(row=3,column=3)


    Label(frame2,text="Who is the Father of our Nation ?",font=("Arial",40,"bold")).grid(row=2,column=2)
    Button(frame2,text="S.C Bose",font=("Arial",20,"bold"),bg="light blue",command=a2_wrong).grid(row=3,column=1)
    Button(frame2,text="Chandrashehkar Azad",font=("Arial",20,"bold"),bg="light green",command=a2_wrong).grid(row=3,column=2)
    Button(frame2,text="Mahatma Gandhi",font=("Arial",20,"bold"),bg="light pink",command=a2_right).grid(row=3,column=3)

    Label(frame3,text="What is the currency of India ?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame3,text="Rupee",font=("Arial",20,"bold"),bg="light blue",command=a3_right).grid(row=3,column=1)
    Button(frame3,text="Dollar",font=("Arial",20,"bold"),bg="light green",command=a3_wrong).grid(row=3,column=2)
    Button(frame3,text="Euro",font=("Arial",20,"bold"),bg="light pink",command=a3_wrong).grid(row=3,column=3)
    
    
    Label(frame4,text="What is the capital of India ?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame4,text="Delhi",font=("Arial",20,"bold"),bg="light blue",command=a4_wrong).grid(row=3,column=1)
    Button(frame4,text=" New Delhi",font=("Arial",20,"bold"),bg="light green",command=a4_right).grid(row=3,column=2)
    Button(frame4,text="Lucknow",font=("Arial",20,"bold"),bg="light pink",command=a4_wrong).grid(row=3,column=3)


    Label(frame5,text="Which is the largest river in india?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame5,text="Narmada",font=("Arial",20,"bold"),bg="light blue",command=a5_wrong).grid(row=3,column=1)
    Button(frame5,text="Tapi",font=("Arial",20,"bold"),bg="light green",command=a5_wrong).grid(row=3,column=2)
    Button(frame5,text="Ganges",font=("Arial",20,"bold"),bg="light pink",command=a5_right).grid(row=3,column=3)

def a1_right():
    Label(frame1,text="Correct",font=("Arial",30,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="Marks obtained: 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)

def a1_wrong(): 
    Label(frame1,text="Incorrect",font=("Arial",30,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="Marks obtained: 0",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3) 
def a2_right():
    Label(frame2,text="Correct",font=("Arial",30,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="Marks obtained: 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)
def a2_wrong():
    Label(frame2,text="Incorrect",font=("Arial",30,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="Marks obtained: 0",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)     
def a3_right():
    Label(frame3,text="Correct",font=("Arial",20,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame3,text="Marks obtained: 1",font=("Arial",20,"bold"),background="black",fg="white").grid(row=1,column=3)
    
def a3_wrong():
    Label(frame2,text="Incorrect",font=("Arial",20,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="Marks obtained: 0",font=("Arial",20,"bold"),background="black",fg="white").grid(row=1,column=3)     
def a4_right():
    Label(frame4,text="Correct",font=("Arial",30,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame4,text="Marks obtained: 1",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)
    

def a4_wrong():
    Label(frame4,text="Incorrect",font=("Arial",30,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame4,text="Marks obtained: 0",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3) 

def a5_right():
    Label(frame5,text="Correct",font=("Arial",20,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame5,text="Marks obtained: 1",font=("Arial",20,"bold"),background="black",fg="white").grid(row=1,column=3)
    


def a5_wrong():
    Label(frame5,text="Incorrect",font=("Arial",30,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame5,text="Marks obtained: 0",font=("Arial",30,"bold"),background="black",fg="white").grid(row=1,column=3)                     
quiz(y)
a.pack()

root.mainloop()