from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Treeview,Notebook

class Student:
    def __init__(self,name,email):
        self.name = name
        self.email = email 
        self.root4=Tk()
        self.root4.geometry(f'{self.root4.winfo_screenwidth()}x{self.root4.winfo_screenheight()}')
        self.view()
        self.root4.mainloop()

    def getattendance(self):
        db = sqlite3.connect("attendancesystem.db")
        cr = db.cursor()
        
        cr.execute(f'''select * from student where email='{self.email}' ''')
        self.data = cr.fetchone()
        self.rollno = self.data[0]
        cr.execute(f'''select date,attendance from attendance where rollno='{self.rollno}' ''')
        data1 = cr.fetchall()
        
        for i in data1:
            self.tree.insert('','end',values=i)

    def updateprofile(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''update student set name='{self.studentname.get()}',Password='{self.studentpass.get()}' where email='{self.email}' ''') 
        db.commit()
        messagebox.showinfo("Success","Profile Updated Succcessfully")   


    def logout(self):
        self.root4.destroy()
        import MainPanel

    def view(self):
        nb = Notebook(self.root4)
        nb.pack(expand=True, fill='both')

        # Attendance Tab
        
        F1 = Frame(nb, bg='#dee2ff')
        F1.pack(expand=True, fill='both')
        
        f11 = Frame(F1, bg='#dee2ff')
        f11.place(relx=0.5, rely=0.5, anchor='center')
        
        self.tree = Treeview(f11, columns=("column1", "column2"), show='headings')
        self.tree.heading("column1", text="Date")
        self.tree.heading("column2", text="Attendance")
        self.tree.pack(expand=True, fill='both')

        nb.add(F1, text='View Students')
        
        self.getattendance()


# STUDENT UPDATE PROFILE

        F2= Frame(nb,bg='#dee2ff')
        F2.pack(expand=True, fill='both')

        self.f22=Frame(F2,bg='#c0c0c0')
        self.f22.place(relx=0.5,rely=0.5,anchor='center')
        
        list_data=[StringVar(value=self.data[i]) for i in range(len(self.data))]

        l1 = Label(self.f22, text="Roll no.",font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='blue')
        l1.grid(row=0, column=0, padx=10, pady=10)
        self.studentid = Entry(self.f22,textvariable=list_data[0],state='disabled')
        self.studentid.grid(row=0, column=1, padx=10, pady=10)

        l2 = Label(self.f22, text="Name",font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='blue')
        l2.grid(row=1, column=0, padx=10, pady=10)
        self.studentname = Entry(self.f22,textvariable=list_data[1])
        self.studentname.grid(row=1, column=1, padx=10, pady=10)

        l3 = Label(self.f22, text="Email",font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='blue')
        l3.grid(row=2, column=0, padx=10, pady=10)
        self.studentemail = Entry(self.f22,textvariable=list_data[2],state='disabled')
        self.studentemail.grid(row=2, column=1, padx=10, pady=10)

        l4 = Label(self.f22, text="Password",font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='blue')
        l4.grid(row=3, column=0, padx=10, pady=10)
        self.studentpass = Entry(self.f22,show="*",textvariable=list_data[3])
        self.studentpass.grid(row=3, column=1, padx=10, pady=10)


        l6 = Label(self.f22, text="Course",font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='blue')
        l6.grid(row=4, column=0, padx=10, pady=10)
        self.combo = Entry(self.f22,textvariable=list_data[5],state='disabled')
        self.combo.grid(row=4, column=1, padx=10, pady=10)

        addstudent = Button(self.f22, text="Update Profile",command=self.updateprofile)
        addstudent.grid(row=5, column=1, padx=10, pady=10)

        logbtn = Button(self.f22, text="Logout",command=self.logout)
        logbtn.grid(row=6, column=1, padx=10, pady=10)
        nb.add(F2, text="Update Profile")


  