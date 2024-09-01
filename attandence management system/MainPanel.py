from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Notebook
from adminpannel import *
from teacherpannel import *
from studentpannel import*
class Main:
    def __init__(self):
        self.root=Tk()
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        self.view()
        self.root.mainloop()
        
    def getcourses(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute('''select * from courses''')
        data1=cr.fetchall()
        for i in data1:
            self.courses.append(i[1])
            
    def addstudents(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from student where rollno={self.studentroll.get()} or
                   email='{self.studentemail.get()}'  ''')
        data=cr.fetchone()
        if data:
            messagebox.showerror("Error",' Student already exist')
        else:
            cr.execute(f'''insert into student values({self.studentroll.get()},'{self.studentname.get()}','{self.studentemail.get()}','{self.studentpass.get()}','{self.gender1.get()}','{self.scombo.get()}') ''')
            db.commit()
            messagebox.showinfo("Success","Account created")
            self.root7.destroy()

    def adminlogin(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from Admin where Email='{self.adminemail.get()}' and Password='{self.adminpass.get()}' ''')
        data=cr.fetchone()
        print(data)
        if data:
            messagebox.showinfo("Success",'welcome')
            self.root.destroy()
            obj=Admin()
        else:
            messagebox.showerror("Error","wrong info")
            
            
            
    def teacherlog(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from teacher where email='{self.teacheremail.get()}' and Password='{self.teacherpass.get()}' ''')
        data=cr.fetchone()
        print(data)
        if data:
            messagebox.showinfo("Success",'welcome')
            self.root.destroy()
            obj=Teacher(data[1],data[2])
        else:
            messagebox.showerror("Error","wrong info")
            
    def studentlog(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from student where email='{self.studentemail.get()}' and Password='{self.studentpass.get()}' ''')
        data=cr.fetchone()
        print(data)
        if data:
            messagebox.showinfo("Success",'welcome student')
            self.root.destroy()
            obj=Student(data[1],data[2])
        else:
            messagebox.showerror("Error","wrong info")
            
    def studentregister(self):
        self.courses=[]
        self.getcourses()
        self.root7=Tk()
        self.root7.geometry(f'{self.root7.winfo_screenwidth()}x{self.root7.winfo_screenheight()}')
        self.root7.config(bg="#456788")
        F3=Frame(self.root7,bg='red')
        F3.pack(expand=True,fill="both")
        f33=Frame(F3,bg='#D1D0CE')
        f33.place(relx=0.5,rely=0.5,anchor='center')
        L1=Label(f33,text="S_rollno" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L1.grid(row=0,column=0,padx=10,pady=10)
        self.studentroll=Entry(f33)
        self.studentroll.grid(row=0,column=1,padx=10,pady=10)
        
        L2=Label(f33,text="S_name" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L2.grid(row=1,column=0  ,padx=10,pady=10)
        self.studentname=Entry(f33)
        self.studentname.grid(row=1,column=1,padx=10,pady=10)
        
        
        L3=Label(f33,text="S_email" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L3.grid(row=2,column=0,padx=10,pady=10)
        self.studentemail=Entry(f33)
        self.studentemail.grid(row=2,column=1,padx=10,pady=10)
        
        L4=Label(f33,text="S_pass" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L4.grid(row=3,column=0,padx=10,pady=10)
        self.studentpass=Entry(f33)
        self.studentpass.grid(row=3,column=1,padx=10,pady=10)
        
        self.gender1=StringVar(value="male")
        L5=Label(f33,text="S_gender" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L5.grid(row=4,column=0,padx=10,pady=10)
        self.studentgender=Radiobutton(f33,text="male" ,value="male",variable=self.gender1)
        self.studentgender.grid(row=4,column=1,padx=10,pady=10)
        self.studentgender1=Radiobutton(f33,text="Female" ,value="Female",variable=self.gender1)
        self.studentgender1.grid(row=5,column=1,padx=10,pady=10)
        
        L6=Label(f33,text="S_course" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L6.grid(row=6,column=0,pady=10)
        self.scombo=Combobox(f33,values=self.courses)
        self.scombo.grid(row=6,column=1,padx=10,pady=10)
        
        addstudent=Button(f33,text="Add students",command=self.addstudents,font=("Arial bold", 10))
        addstudent.grid(row=7,column=1,padx=10,pady=10)
        
        
    def view(self):
        nb=Notebook()
        nb.pack(expand=True,fill="both")
        
 # STUDENT PANEL
        F1 = Frame(nb,background="lIGHTBLUE")
        # bg = PhotoImage(file = "a.png") 
        # label1 = Label( self.root, image = bg,width=1200, height=500) 
        # label1.place(relx=0.6, rely=0.5, anchor='e') 
        F1.pack(expand=True,fill="both")
        f11 = Frame(F1,bg='#f3f5f6') 
        f11.place(relx=0.5, rely=0.5, anchor='center')
        l1 = Label(f11, text='Email', font=("Elephant", 14))
        l1.grid(row=0, column=0)
        self.studentemail = Entry(f11)
        self.studentemail.grid(row=0, column=1, padx=10, pady=10)

        l2 = Label(f11, text='Password', font=("Elephant", 14))
        l2.grid(row=1, column=0)
        self.studentpass = Entry(f11, show="*")
        self.studentpass.grid(row=1, column=1, padx=10, pady=10)

        btn = Button(f11, text='S-Login', font=("Arial", 10),command=self.studentlog)
        btn.grid(row=2, column=1, padx=10, pady=10)
        btnn=Button(f11,text="Register",command=self.studentregister,font=("Arial", 10))
        btnn.grid(row=3,column=1,padx=10,pady=10)
        nb.add(F1, text="Student Login")

# TEACHER PANEL
        F2 = Frame(nb,bg='#ffec94')
        F2.pack(expand=True,fill="both")
        f22 = Frame(F2,bg='#f3f5f6')
        f22.place(relx=0.5, rely=0.5, anchor='center')

        l1 = Label(f22, text='Email', font=("Elephant", 14))
        l1.grid(row=0, column=0)
        self.teacheremail = Entry(f22)
        self.teacheremail.grid(row=0, column=1, padx=10, pady=10)

        l2 = Label(f22, text='Password', font=("Elephant", 14))
        l2.grid(row=1, column=0)
        self.teacherpass = Entry(f22, show="*")
        self.teacherpass.grid(row=1, column=1, padx=10, pady=10)

        btn = Button(f22, text=' T-Login', font=("Arial", 10),command=self.teacherlog)
        btn.grid(row=2, column=1, padx=10, pady=10)

        nb.add(F2, text="Teacher Login")

#Admin Panel
        F3 = Frame(nb,bg='#e52e71')
        # bg = PhotoImage(file = "c.png") 
        # label1 = Label( self.root, image = bg,width=1200, height=500) 
        # label1.place(relx=0.6, rely=0.5, anchor='e')
        F3.pack(expand=True,fill="both") 
        f33 = Frame(F3,bg='#f3f5f6')
        f33.place(relx=0.5, rely=0.5, anchor='center')

        l1 = Label(f33, text='Email', font=("Elephant", 14))
        l1.grid(row=0, column=0)
        self.adminemail = Entry(f33)
        self.adminemail.grid(row=0, column=1, padx=10, pady=10)

        l2 = Label(f33, text='Password', font=("Elephant", 14))
        l2.grid(row=1, column=0)
        self.adminpass = Entry(f33, show="*")
        self.adminpass.grid(row=1, column=1, padx=10, pady=10)

        btn = Button(f33, text=' A-Login', font=("Arial", 10),command=self.adminlogin)
        btn.grid(row=2, column=1, padx=10, pady=10)

        nb.add(F3, text="Admin Login" )



obj = Main()