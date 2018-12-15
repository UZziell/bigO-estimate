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
#
#
# Frame 1
photo = PhotoImage(file="espresso2.png")
Label(f1, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
Button(f1, text=' Single', bg="black", fg="white", command=lambda: raise_frame(f2)).place(x=20, y=40)
Button(f1, text='Double', bg="black", fg="white", command=lambda: raise_frame(f3)).place(x=20, y=80)
Label(f1, text="Hint\n"
               "Single: estimates an algorithm runtime\n"
               "Double: compares two algorithms runtimes", fg="white", bg="black").place(x=20, y=680)
#
#
#

# FRAME 2 #
# Label(f2, text='FRAME 2').pack()
# lbl = Label(f2, text="")
# lbl.grid(column=0, row=0)
Label(f2, image=photo).place(x=0, y=0, relwidth=1, relheight=1)

hintlbl = Label(f2, text="Hint: Paste code in the box", bg="black", fg="white")
hintlbl.grid(column=3, row=0)

f2entry = Text(f2, bg="black", fg="white", height=40, width=100)
# txt.insert(END, "paste your code here")
f2entry.grid(column=1, row=1)


def calchandle():
    print(f2entry.get("1.0", "end-1c"))


btn = Button(f2, text="Calculate", bg="black", fg="white", command=calchandle)
btn.grid(column=1, row=3)
Button(f2, text='Back', bg="black", fg="white", command=lambda: raise_frame(f1)).grid(row=3, column=4)
Label(f2, text="", bg="black", fg="white").grid(row=10, column=10)
#
#
#
#
# Frame 3 #
Label(f3, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
f3entry = Text(f3, bg="black", fg="white", height=40, width=50)
# entry.insert(END, "paste your code here")
f3entry.grid(column=1, row=1)

lbl = Label(f3, bg="black", fg="white", text="")
lbl.grid(column=2, row=1)

f3entry2 = Text(f3, bg="black", fg="white", height=40, width=50)
f3entry2.grid(column=3, row=1)


def comparehandle():
    print(f3entry.get("1.0", "end-1c"))
    print("\n")
    print(f3entry2.get("1.0", "end-1c"))


btn = Button(f3, text="Compare", bg="black", fg="white", command=comparehandle)
btn.grid(row=3, columnspan=4)
Button(f3, text='back',bg="black", fg="white", command=lambda: raise_frame(f1)).place(x=970, y=690)

raise_frame(f1)
root.mainloop()
