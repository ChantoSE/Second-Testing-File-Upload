from tkinter import*
from tkinter import ttk

root = Tk()

root.iconbitmap("Image/2.ico")
root.geometry("500x500")
#root.resizable(False, False)
root.title("MyScroller")

mainframe1 = LabelFrame(root) # this's frame 1 that stay upper
mainframe2 = LabelFrame(root)

# Focus to create everything in mainframe1 first
mycanvas = Canvas(mainframe1)
mycanvas.pack(side=LEFT, fill=BOTH) # if don't use fill=BOTH it will see spacing up and down.

yscrollbar = ttk.Scrollbar(mainframe1, orient="vertical", command= mycanvas.yview)
yscrollbar.pack(side= RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure (scrollregion= mycanvas.bbox("all")))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor= "nw")

mainframe1.pack(fill="both", expand="yes", padx=10, pady=10)
mainframe2.pack(fill="both", expand="yes", padx=10, pady=10)

for i in range(50):
    Button(myframe, text="My Button - " + str(i)).pack()

# Focus to create everything in mainframe2 (horizontal)

# Focus to create everything in mainframe2 (horizontal)
mycanvas1 = Canvas(mainframe2)
mycanvas1.pack(side=TOP, fill=BOTH)

xscrollbar = ttk.Scrollbar(mainframe2, orient="horizontal", command= mycanvas1.xview)
xscrollbar.pack(side= BOTTOM, fill="x")
mycanvas1.configure(xscrollcommand=xscrollbar.set)

mycanvas1.bind('<Configure>', lambda e: mycanvas1.configure(scrollregion= mycanvas1.bbox("all")))

myframe1 = Frame(mycanvas1)
mycanvas1.create_window((0,0), window = myframe1, anchor="nw")

controlframe = Frame(root) # prepare framework that we want to set it like range (support with .grid)
controlframe.pack()

for i in range (70):
    #Button(myframe1, text= "The Button1 - " + str(i)).pack()
    Button(myframe1, text= "The Button1 - " + str(i)).grid()

root.mainloop()

#mylabel = Label(controlframe, text="", borderwidth=0, bd=2, relief= SUNKEN, font=("Time Newroman",12))
#mylabel.grid(row=1, column=1, pady=20)