import tkinter as tk
from tkinter import *
app = tk.Tk()
app.geometry("500x500")
app.title("python-calculator")
app.maxsize(500,500)
app.minsize(500,500)
ent = Entry(app, width=32, borderwidth=9, relief=RIDGE)
ent.grid(pady=40,row=0,sticky="w",padx=40)

def delete():
    a = ent.get()
    ent.delete(first=len(a) - 1, last="end")


def fresult():
    if ent.get() == "":
        pass
    elif ent.get()[0] == "0":
        ent.delete(0, "end")
    else:
        c_res = ent.get()
        c_res = eval(c_res)
        clearf()
        ent.insert("end", c_res)


def clearf():
    ent.delete(0, "end")

clean = Button(app,text="C",width=12,command=clearf,bg="green",fg="white",relief=RIDGE)
clean.grid(row=0,sticky="w",padx=320,pady=10)
Char_nine = Button(text="9",width=6,command=lambda : ent.insert("end","9"),borderwidth=9,relief=RIDGE)
Char_nine.grid(row=1,sticky="w",padx=30)
Char_eight = Button(text="8",width=6,command=lambda : ent.insert("end","8"),borderwidth=9,relief=RIDGE)
Char_eight.grid(row=1,sticky="w",padx=90)
Char_seven = Button(app,text="7",width=6,command=lambda : ent.insert("end","7"),borderwidth=9,relief=RIDGE)
Char_seven.grid(row=1,sticky="w",padx=150)
Char_plus = Button(app,text="+",width=12,command=lambda : ent.insert("end","+"),borderwidth=9,relief=RIDGE)
Char_plus.grid(row=1,sticky="e",padx=250)
Char_six = Button(text="6",width=6,command=lambda : ent.insert("end","6"),borderwidth=9,relief=RIDGE)
Char_six.grid(row=2,sticky="w",padx=30,pady=10)
Char_five = Button(text="5",width=6,command=lambda : ent.insert("end","5"),borderwidth=9,relief=RIDGE)
Char_five.grid(row=2,sticky="w",padx=90,pady=10)
Char_four = Button(app,text="4",width=6,command=lambda : ent.insert("end","4"),borderwidth=9,relief=RIDGE)
Char_four.grid(row=2,sticky="w",padx=150,pady=10)
Char_minus = Button(app,text="-",width=12,command=lambda : ent.insert("end","-"),borderwidth=9,relief=RIDGE)
Char_minus.grid(row=2,sticky="e",padx=250,pady=10)
Char_three = Button(text="3",width=6,command=lambda : ent.insert("end","3"),borderwidth=9,relief=RIDGE)
Char_three.grid(row=3,sticky="w",padx=30,pady=10)
Char_two = Button(text="2",width=6,command=lambda : ent.insert("end","2"),borderwidth=9,relief=RIDGE)
Char_two.grid(row=3,sticky="w",padx=90,pady=10)
Char_one = Button(app,text="1",width=6,command=lambda : ent.insert("end","1"),borderwidth=9,relief=RIDGE)
Char_one.grid(row=3,sticky="w",padx=150,pady=10)
Char_multiply = Button(app,text="*",width=12,command=lambda : ent.insert("end","*"),borderwidth=9,relief=RIDGE)
Char_multiply.grid(row=3,sticky="e",padx=250,pady=10)
Char_zero = Button(text="0",width=6,command=lambda : ent.insert("end","0"),borderwidth=9,relief=RIDGE)
Char_zero.grid(row=4,sticky="w",padx=30,pady=10)
Char_double_zero = Button(text="00",width=6,command=lambda : ent.insert("end","00"),borderwidth=9,relief=RIDGE)
Char_double_zero.grid(row=4,sticky="w",padx=90,pady=10)
Char_dot = Button(app,text=".",width=6,command=lambda : ent.insert("end","."),borderwidth=9,relief=RIDGE)
Char_dot.grid(row=4,sticky="w",padx=150,pady=10)
Char_divide = Button(app,text="/",width=12,command=lambda : ent.insert("end","/"),borderwidth=9,relief=RIDGE)
Char_divide.grid(row=4,sticky="e",padx=250,pady=10)
result = Button(app,text="=",width=15,command=fresult,bg="green",fg="white",borderwidth=9,relief=RIDGE)
result.grid(row=5,sticky="w",padx=30,pady=10)
Char_modulus = Button(app,text="%",width=12,command=lambda : ent.insert("end","%"),borderwidth=9,relief=RIDGE)
Char_modulus.grid(row=5,sticky="e",padx=250,pady=10)
delete = Button(app,text="del",width=6,command=delete,borderwidth=9,relief=RIDGE)
delete.grid(row=5,sticky="w",padx=160,pady=10)

app.mainloop()