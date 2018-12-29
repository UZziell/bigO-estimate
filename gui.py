from tkinter import *
from tkinter import messagebox
import functions as fn


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.title("BigO estimation")
root.geometry('1049x750')
root.resizable(False, False)
f1 = Frame(root)
f2 = Frame(root)

f3 = Frame(root)

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')

###########
# FRAME 1 #
###########
photo = PhotoImage(file="res/espresso2.png")
Label(f1, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
Button(f1, text=' Single', bg="black", fg="white", command=lambda: raise_frame(f2)).place(x=20, y=40)
Button(f1, text='Double', bg="black", fg="white", command=lambda: raise_frame(f3)).place(x=20, y=80)
Label(f1, text="Hint\n"
               "Single: Estimates an algorithm complexity\n"
               "Double: Compares two algorithms complexities", fg="white", bg="black").place(x=20, y=680)

###########
# FRAME 2 #
###########
# Label(f2, text='FRAME 2').pack()
# lbl = Label(f2, text="")
# lbl.grid(column=0, row=0)
photo_earth = PhotoImage(file="res/sss.png")
Label(f2, image=photo_earth).place(x=0, y=0, relwidth=1, relheight=1)

hint_lbl = Label(f2, text="Hint: Paste code in the box", bg="black", fg="white")
hint_lbl.grid(column=3, row=0)

f2entry = Text(f2, bg="black", fg="white", height=40, width=100)
f2entry.grid(column=1, row=1)

f2entry.insert(END, "# USE Python programming lang, provide functions with variable named N as iterator"
                    "\n#sample:"
                    """\n\ni = 0
while i < N:
    print("*", end='')
    i += 1""")


def calc_handle():
    user_input = f2entry.get("1.0", "end-1c")
    complexity = fn.equation_finder(user_input)
    messagebox.showwarning("TADDDDDAAAAAAAAAAAAA",
                           f"Estimated Algorithm Complexity(BIG O notation): {complexity[0]}")
    fn.plot(complexity[1])
    # api1 = compiler_api.Api(single_input)
    # print(api1.response.status_code, api1.finalstring)
    # messagebox.showinfo("Operation Successful", "Estimated: {}".format(api1.finalstring["cpuTime"]))
    # print("Status code: {}\n".format(api1.response.status_code))
    # print(" memory used was: {}\n".format(api1.finalstring['memory']),
    #       "cputime was {}\n".format(api1.finalstring["cpuTime"]))
    # print("\noutput: \n\n", api1.finalstring['output'])


calc_btn = Button(f2, text="Calculate", bg="black", fg="white", command=calc_handle)
calc_btn.grid(column=1, row=3)
Button(f2, text='Back', bg="black", fg="white", command=lambda: raise_frame(f1)).grid(row=3, column=4)
Label(f2, text="", bg="black", fg="white").grid(row=10, column=10)

###########
# FRAME 3 #
###########
Label(f3, image=photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
f3entry = Text(f3, bg="black", fg="white", height=40, width=50)
f3entry.grid(column=1, row=1)

f3entry.insert(END, "# USE Python programming lang, provide functions with variable named N as iterator"
                    "\n#sample:"
                    """\n\ni = 0
while i < N:
    print("*", end='')
    i += 1""")

lbl = Label(f3, bg="black", fg="white", text="")
lbl.grid(column=2, row=1)

f3entry2 = Text(f3, bg="black", fg="white", height=40, width=50)
f3entry2.grid(column=3, row=1)


def compare_handle():
    src1 = f3entry.get("1.0", "end-1c")
    src2 = f3entry2.get("1.0", "end-1c")
    left_complex = fn.equation_finder(src1)
    right_complex = fn.equation_finder(src2)

    if left_complex > right_complex:
        better = "Second"
    elif left_complex < right_complex:
        better = "First"
    else:
        better = "No idea which"
    messagebox.showinfo("Compare Successful", "{} algorithm is better.".format(better))
    # api1 = apis.Compiler(f3entry.get("1.0", "end-1c"))
    # api2 = apis.Compiler(f3entry2.get("1.0", "end-1c"))
    # fcpu = float(api1.finalstring['cpuTime'])
    # scpu = float(api2.finalstring['cpuTime'])
    # print("first Status code: {} and second Status code: {}\n".format(api1.response.status_code,
    #                                                                   api2.response.status_code))
    #
    # print(" first memory: {} and second memory: {}\n".format(api1.finalstring['memory'],
    #                                                          api2.finalstring['memory']),
    #
    #       "first cputime: {} and second cputime: {}\n".format(fcpu, scpu))
    # print("\nfirst output: \n\n", api1.finalstring['output'])
    # print("\nsecond output: \n\n", api2.finalstring['output'])
    #
    # if fcpu > scpu:
    #     better = "Second"
    # elif fcpu < scpu:
    #     better = "First"
    # else:
    #     better = "No idea which"
    # messagebox.showinfo("Compare Successful", "{} algorithm is better.".format(better))
    #
    # # print(f3entry.get("1.0", "end-1c"))
    # # print("\n")
    # # print(f3entry2.get("1.0", "end-1c"))


compare_btn = Button(f3, text="Compare", bg="black", fg="white", command=compare_handle)
compare_btn.grid(row=3, columnspan=4)

Button(f3, text='back', bg="black", fg="white", command=lambda: raise_frame(f1)).place(x=970, y=690)

raise_frame(f1)
root.mainloop()
