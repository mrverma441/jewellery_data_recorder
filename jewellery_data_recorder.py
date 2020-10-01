from tkinter import*
from tkinter import ttk, messagebox
import time, os
class File_App:
    def __init__(self):
        self.root=Tk()
        self.root.title("Student Data Recorder")
        self.root.geometry("1350x700+0+0")
        

        title=Label(self.root,text="Jewellry Data Recorder",bd=10,relief=GROOVE,pady=10, font=("Harlow Solid Italic",40,"bold"),bg="yellow").pack(fill=X,)
        Student_Frame=Frame(self.root,bd=10, relief=GROOVE,bg="red")
        Student_Frame.place(x=20,y=100,height=450)

        stitle=Label(Student_Frame,text="Jewellery Details",font=("times new roman",40,"bold")).grid(row=0,columnspan=4,pady=20)

        #====All Variables=====
        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()


        lblsid=Label(Student_Frame,text="C.ID",font=("times new roman",20,"bold")).grid(row=1,column=0,pady=10,padx=20)
        txtsid=Entry(Student_Frame,textvariable=self.s_id, bd=7, relief=GROOVE,width=22,font=("arial 15 bold")).grid(row=1, column=1, padx=10, pady=10)

        lblcontact=Label(Student_Frame,text="Contact No.",font=("times new roman",20,"bold")).grid(row=1,column=2,pady=10,padx=20)
        txtcontact=Entry(Student_Frame, bd=7,textvariable=self.contact, relief=GROOVE,width=22,font=("arial 15 bold")).grid(row=1, column=3, padx=10, pady=10)

        lblname=Label(Student_Frame,text="C.Name",font=("times new roman",20,"bold")).grid(row=2,column=0,pady=10,padx=20)
        txtname=Entry(Student_Frame, bd=7,textvariable=self.name, relief=GROOVE,width=22,font=("arial 15 bold")).grid(row=2, column=1, padx=10, pady=10)

        lbldate=Label(Student_Frame,text="Date(dd/mm/yyyy)",font=("times new roman",20,"bold")).grid(row=2,column=2,pady=10,padx=20)
        txtdate=Entry(Student_Frame, bd=7,textvariable=self.date, relief=GROOVE,width=22,font=("arial 15 bold")).grid(row=2, column=3, padx=10, pady=10)

        lblcourse=Label(Student_Frame,text="weight&Int",font=("times new roman",20,"bold")).grid(row=3,column=0,pady=10,padx=20)
        txtcourse=Entry(Student_Frame, bd=7,textvariable=self.course, relief=GROOVE,width=22,font=("arial 15 bold")).grid(row=3, column=1, padx=10, pady=10)

        lbladdress=Label(Student_Frame,text="Address",font=("times new roman",20,"bold")).grid(row=4,column=0,pady=10,padx=20)
        txtaddress=Entry(Student_Frame, bd=7,textvariable=self.address, relief=GROOVE,width=22,font=("arial 15 bold")).grid(row=4, column=1, padx=10, pady=10)

        lblcity=Label(Student_Frame,text="Cash AMt.",font=("times new roman",20,"bold")).grid(row=5,column=0,pady=10,padx=20)
        txtcity=Entry(Student_Frame, bd=7,textvariable=self.city, relief=GROOVE,width=22,font=("arial 15 bold")).grid(row=5, column=1, padx=10, pady=10)

        lbldegree=Label(Student_Frame,text="Select Item",font=("times new roman",20,"bold")).grid(row=3,column=2,pady=10,padx=20)
        lblproof=Label(Student_Frame,text="Id Proof",font=("times new roman",20,"bold")).grid(row=4,column=2,pady=10,padx=20)
        lbldegree=Label(Student_Frame,text="Payment Mode",font=("times new roman",20,"bold")).grid(row=5,column=2,pady=10,padx=20)
        degreecombo=ttk.Combobox(Student_Frame, width=20,textvariable=self.degree,state="readonly", font="arial 15 bold")
        degreecombo['values']=("Gold","Silver")
        degreecombo.grid(row=3,column=3, padx=10, pady=10)

        idcombo=ttk.Combobox(Student_Frame, width=20,textvariable=self.proof,state="readonly", font="arial 15 bold")
        idcombo['values']=("PAN Card", "Driving Licence", "Adhaar Card","Voter Id Card", "Student ID Card")
        idcombo.grid(row=4,column=3, padx=10, pady=10)

        paymentcombo=ttk.Combobox(Student_Frame, width=20,textvariable=self.payment,state="readonly", font="arial 15 bold")
        paymentcombo['values']=("Cash", "NEFT", "Credit Card","Paytm", "Google Pay")
        paymentcombo.grid(row=5,column=3, padx=10, pady=10)

        btnFrame=Frame(self.root, bd=10, relief=GROOVE,bg="orange")
        btnFrame.place(x=10, y=580)
        
        btnsave=Button(btnFrame, text="Save", font="arial 15 bold", bd=7,width=18,command=self.save_data).grid(row=0, column=0, padx=12, pady=10)
        btndelete=Button(btnFrame, text="Delete", font="arial 15 bold", bd=7,width=18,command=self.delete).grid(row=0, column=1, padx=12, pady=10)
        btnclear=Button(btnFrame, text="Clear",command=self.clear, font="arial 15 bold", bd=7,width=18).grid(row=0, column=2, padx=12, pady=10)
        btnlog=Button(btnFrame, text="Logout", font="arial 15 bold", bd=7,width=18, command=self.logout).grid(row=0, column=3, padx=12, pady=10)
        btnexit=Button(btnFrame, text="Exit", font="arial 15 bold", bd=7,width=18, command=self.exit_fun).grid(row=0, column=4, padx=12, pady=10)

        File_Frame=Frame(self.root, bd=10, relief=GROOVE,bg="brown")
        File_Frame.place(x=1030, y=100, width=320, height=450)
        
        ftitle=Label(File_Frame, text="All Files", font='arial 15 bold', bd=5, relief=GROOVE,bg="violet").pack(side=TOP, fill=X, )

        scroll_y=Scrollbar(File_Frame, orient=VERTICAL)
        self.file_list=Listbox(File_Frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>", self.get_data)
        self.show_files()
        self.root.mainloop()

    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error", "Student ID Must Be There")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"

                if present =="yes":
                    ask=messagebox.askyesno("Update", "File already present.\nDo you want to update the file?")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update", "Record Has Updated Successfully")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Saved", "Record Has Saved Successfully")
                    self.show_files()

            else:
                self.save_file()
                messagebox.showinfo("Saved", "Record Has Saved Successfully")
                self.show_files()

        
    def save_file(self):
        f=open("files/"+str(self.s_id.get())+".txt","w")
        f.write(
                str(self.s_id.get())+","+
                str(self.name.get())+","+
                str(self.course.get())+","+
                str(self.address.get())+","+
                str(self.city.get())+","+
                str(self.course.get())+","+
                str(self.date.get())+","+
                str(self.degree.get())+","+
                str(self.proof.get())+","+
                str(self.payment.get())
                )
        f.close

    def show_files(self):
        files=os.listdir("files/")
        self.file_list.delete(0,END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)

    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        # print(self.file_list.get(get_cursor))
        f1=open("files/"+self.file_list.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")
        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])

    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")

    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error", "Student ID Must Be There")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"

                if present =="yes":
                    ask=messagebox.askyesno("Delete", "Do you really want to delete?")
                    if ask>0:
                        os.remove("files/"+self.s_id.get()+".txt")
                        messagebox.showinfo("Sucess", "Delete succesfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error", "File Not Found ???")

    def exit_fun(self):
        ask=messagebox.askyesno("Exit", "Do you really want to exit??")
        if ask>0:
            self.root.destroy()
        else:
            return

    def logout(self):
        self.root.destroy()
        import Login
