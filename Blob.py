

from Tkinter import *
from PIL.Image import *

board=Tk()
board.geometry("775x775")
photo=PhotoImage(file="white.png")
wallcovered=[]

def putWall(b,c,n):
    if [c,n] in wallcovered:
        b.config(bg='white')
        wallcovered.remove([c,n])
    else:
        b.config(bg='black')
        wallcovered.append([c,n])
    print c,n
    
def mur1(c,n):
    b=Button(board,image=photo,borderwidth=0,bg="white",height=20,width=10, command= lambda :putWall(b,c,n))
    b.grid(row=c,column=n)

def mur2(c,n):
    b=Button(board,image=photo,borderwidth=0,bg="white",height=10,width=20, command= lambda :putWall(b,c,n))
    b.grid(row=c,column=n)

def floor(c,n):
    b=Button(board,image=photo,borderwidth=0,bg="white",height=20,width=20)
    b.grid(row=c,column=n)

def pillier(c,n):
    b=Button(board,borderwidth=0, state='disabled',image=photo,bg="black",width=10,height=10)
    b.grid(row=c,column=n)

def randomwall1():
    c=random.choice(list(1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39)
    n=random.choice(list(
        
for c in range (41):
    for n in range (41):
        if n%2==0 and c%2==0:
            pillier(c,n)
        if n%2==0 and c%2!=0:
            mur1(c,n)
        if c%2==0 and n%2!=0:
            mur2(c,n)
        if c%2!=0 and n%2!=0:
            floor(c,n)




board.mainloop()
"""b = Button(master, text=longtext, anchor=W, justify=LEFT, padx=2)
b.config(relief=SUNKEN)"""

