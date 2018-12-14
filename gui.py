from tkinter import *

window = Tk()
window.title("BigO estimation")
window.geometry('1080x750')

lbl = Label(window, text="  ")
lbl.grid(column=0, row=0)

hintlbl = Label(window, text="Hint: Use python syntax")
hintlbl.grid(column=3, row=1)

txt = Text(window, height=40, width=100)
txt.grid(column=1, row=1)



def clicked():
    print(txt.get("1.0", "end-1c"))


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=2)
window.mainloop()
