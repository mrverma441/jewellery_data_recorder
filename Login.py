from tkinter import*
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S Login System")
        self.root.geometry("1355x705+0+0")

        F1 = Frame(self.root, bd=10, relief=GROOVE,bg="blue")
        F1.place(x=463, y=150, height=350)

        self.user = StringVar()
        self.password = StringVar()

        title = Label(F1, text="Login System", font=("times new roman", 30, 'bold'),fg="red").grid(row=0, columnspan=2, pady=20)

        lblUser = Label(F1, text="Username", font=("times new roman", 25, "bold"),fg="green").grid(row=1, column=0, pady=10,
                                                                                        padx=20)

        txtuser = Entry(F1, bd=7, relief=GROOVE, textvariable=self.user, width=25, font="arial 15 bold",fg="blue").grid(row=1,
                                                                                                              column=1,
                                                                                                              pady=10,
                                                                                                              padx=10)

        lblpassword = Label(F1, text="Password", font=("times new roman", 25, "bold"),fg="orange").grid(row=2, column=0, pady=10,
                                                                                            padx=20)

        txtpassword = Entry(F1, bd=7, relief=GROOVE, show="*", textvariable=self.password, width=25,
                            font="arial 15 bold",fg="orange").grid(row=2, column=1, pady=10, padx=10)

        btnexit = Button(F1, text="Exit", font="arial 15 bold", bd=7, width=10, command=self.exitfun,fg="brown").place(x=10, y=250)
        btnreset = Button(F1, text="Reset", font="arial 15 bold", bd=7, width=10, command=self.resetfun,fg="violet").place(x=180,
                                                                                                               y=250)
        btnlogin = Button(F1, text="Login", font="arial 15 bold", bd=7, width=10, command=self.logfun,fg="red").place(x=350,
                                                                                                             y=250)

    def exitfun(self):
        option = messagebox.askyesno("Exit", "Do you really want to exit")
        if option > 0:
            self.root.destroy()

        else:
            return

    def resetfun(self):
        self.user.set("")
        self.password.set("")

    def logfun(self):
        if self.user.get() == "mrverma" and self.password.get() == "7534050774":
            messagebox.showinfo("Welcome", "Hello MR VERMA")
            root.destroy()
            import Student_Data_Recorder
            Student_Data_Recorder.File_App()
        else:
            messagebox.showerror("Error","Invailed username or password")
            self.root.destroy()
            
            

root=Tk()
root.configure(background="orange")
ob=Login(root)
root.mainloop()
