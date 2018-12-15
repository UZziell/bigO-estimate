from tkinter import *


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.title("BigO estimation")
root.geometry('1020x750')
root.resizable(False, False)
f1 = Frame(root)
f2 = Frame(root)

f3 = Frame(root)

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')

photo = PhotoImage(file="espresso2.png")

Label(f1, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
Button(f1, text=' Single', bg="black", fg="white", command=lambda: raise_frame(f2)).place(x=20, y=40)
Button(f1, text='Double', bg="black", fg="white", command=lambda: raise_frame(f3)).place(x=20, y=80)
Label(f1, text="Hint\n"
               "Single: estimates an algorithm runtime\n"
               "Double: compares two algorithms runtimes", fg="white", bg="black").place(x=20, y=680)

# FRAME 2 #
# Label(f2, text='FRAME 2').pack()
Label(f2, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
lbl = Label(f2, text=" ")
lbl.grid(column=0, row=0)

hintlbl = Label(f2, text="Hint: Use python syntax")
hintlbl.grid(column=3, row=0)

txt = Text(f2, height=40, width=100)
txt.grid(column=1, row=1)


def clicked():
    print(txt.get("1.0", "end-1c"))


btn = Button(f2, text="Calculate", command=clicked)
btn.grid(column=1, row=2)
Button(f2, text='back', command=lambda: raise_frame(f1)).grid(row=10, column=10)

# Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='back', command=lambda: raise_frame(f1)).pack(side='left')

raise_frame(f1)
root.mainloop()
