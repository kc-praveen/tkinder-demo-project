import tkinter
from tkinter import *
from tkinter import messagebox
window=tkinter.Tk()
window.title("kc")
window.geometry("900x500")
window.configure(bg="gray")

def login():

    username=e1.get()
    password=e2.get()
    if(username=='kc' and password=='420'):

        window2=tkinter.Tk()
        window2.title("vanakam da mapla")
        window2.geometry("800x500")
        window2.configure(bg="gray")
        #L5=Label(window2, text="Vaa Arunachellam nee varuvanu tharium", font=("Times new roman", 20, "bold"), bg="white", fg="black")

        L1 = Label(window2, text="CONTACT BOOK", font=("Times new roman", 20, "bold"), bg="black", fg="white")
        L1.place(x=400, y=50)
        L2 = Label(window2, text="ENTER NAME", font=("Times new roman", 12, "bold"), bg="white", fg="red")
        L2.place(x=120, y=200)
        L3 = Label(window2, text="ENTER NUMBER", font=("Times new roman", 12, "bold"), bg="white", fg="red")
        L3.place(x=120, y=250)
        e3 = Entry(window2, width=20)
        e3.place(x=300, y=150)
        e4 = Entry(window2, width=20)
        e4.place(x=300, y=200)
        b1 = Button(window2, text="SAVE", command=login, font=("Times new roman", 18, "bold"), bg="white", fg="red")
        b1.place(x=250, y=400)

        #L5.place(x=150,y=200)
        window.destroy()
    else:
        messagebox.showerror("Error","Olunga password podra venna")


L1=Label(window, text="CONTACT BOOK", font=("Times new roman", 20, "bold"), bg="black", fg="white")
L1.place(x=400,y=50)
L2=Label(window, text="USER NAME", font=("Times new roman", 16, "bold"), bg="black", fg="red")
L2.place(x=130,y=200)
L3=Label(window, text="PASSWORD", font=("Times new roman", 16, "bold"), bg="black", fg="red")
L3.place(x=130,y=250)
b1 = Button(window, text="LOGIN", command=login, font=("Times new roman", 18, "bold"), bg="white", fg="red")
b1.place(x=250, y=400)

e1=Entry(window,width=40)
e1.place(x=300,y=200)
e2=Entry(window,width=40)
e2.place(x=300,y=250)





#login()





window.mainloop()