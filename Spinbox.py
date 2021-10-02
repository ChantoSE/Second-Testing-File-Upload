from tkinter import *

root = Tk()


root.iconbitmap("Image/2.ico")
root.geometry("500x500")
root.title("MySpinbox")

#myspinbox = Spinbox(root, from_=0, to= 15, increment=2, font=("Arial",18)) # បង្កើតពីតំលៃចាប់ផ្តើមដល់តំលៃបញ្ចប់ (increment=2 គឺចុចម្តងកើន២លេខ)
myspinbox = Spinbox(root, value=("Tp", "Tpb", "T", "TOP"), font=("Arial",18))
myspinbox.pack(pady=20)


def getdata():
    mylabel.config(text=myspinbox.get())
mybutton = Button(root, text="Submit", command=getdata) # use to call function to use
mybutton.pack(pady=20,)  

mylabel = Label(root, text="Click Output Show Here", bd=5,relief= SUNKEN, anchor=S) # Label ប្រើសម្រាប់បង្តើតទីតាំង១ដែល កំណត់បានឲ្យវាចេញជាពាក្យអ្វីមួយដែលយើងបានកំណត់។​ 
mylabel.pack(pady=20, side= "left") # define where actual location that we need to point out.



root.mainloop()