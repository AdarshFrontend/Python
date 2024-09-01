from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkinter.ttk import Treeview,Combobox
class Admin:
    def __init__(self):
        self.root1=Tk()
        self.root1.geometry(f'{self.root1.winfo_screenwidth()}x{self.root1.winfo_screenheight()}')
        self.view()
        self.root1.mainloop()
        
    def getcourses(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute('''select * from courses''')
        data1=cr.fetchall()
        for i in data1:
            self.tree.insert('','end',values=i)
            self.courses.append(i[1])
    
    def getteachers(self):
        for j in self.tree2.get_children():
            self.tree2.delete(j)
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute('''select * from teacher''')
        data2=cr.fetchall()
        for j in data2:
            self.tree2.insert('','end',values=j)
    
    # def getstudents(self):
    #     for k in self.tree3.get_children():
    #         self.tree3.delete(k)
    #     db=sqlite3.connect("attendancesystem.db")
    #     cr=db.cursor()
    #     cr.execute('''select * from student''')
    #     data3=cr.fetchall()
    #     for k in data3:
    #         self.tree3.insert('','end',values=k)
            
    def addcourse(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from courses where courseid={self.courseid.get()} or
                   coursename='{self.coursename.get()}' ''')
        data=cr.fetchone()
        if data:
            messagebox.showerror("Error",' name or id already exist')
        else:
            cr.execute(f'''insert into courses values({self.courseid.get()},'{self.coursename.get()}') ''')
            db.commit()
            messagebox.showinfo("Success","course added")
            self.getcourses()
            
    def addteacher(self):
        db=sqlite3.connect("attendancesystem.db")
        cr=db.cursor()
        cr.execute(f'''select * from teacher where Tid={self.teacherid.get()} or
                   email='{self.teacheremail.get()}' or
                   courseassigned='{self.combo.get()}' ''')
        data=cr.fetchone()
        if data:
            messagebox.showerror("Error",' Employee or course already exist')
        else:
            cr.execute(f'''insert into teacher values({self.teacherid.get()},'{self.teachername.get()}','{self.teacheremail.get()}','{self.teacherpass.get()}','{self.gender.get()}','{self.combo.get()}') ''')
            db.commit()
            messagebox.showinfo("Success","teacher added")
            
            self.getteachers()
    
    # def addstudents(self):
    #     db=sqlite3.connect("attendancesystem.db")
    #     cr=db.cursor()
    #     cr.execute(f'''select * from student where rollno={self.studentroll.get()} or
    #                email='{self.studentemail.get()}'  ''')
    #     data=cr.fetchone()
    #     if data:
    #         messagebox.showerror("Error",' Student already exist')
    #     else:
    #         cr.execute(f'''insert into student values({self.studentroll.get()},'{self.studentname.get()}','{self.studentemail.get()}','{self.studentpass.get()}','{self.gender1.get()}','{self.scombo.get()}') ''')
    #         db.commit()
    #         messagebox.showinfo("Success","student added")
            
    #         self.getstudents()
    
    
            
    
    
    def view(self):
        self.courses=[]
        nb=Notebook()
        nb.pack(expand=True,fill="both")
        
        #courses
        F1=Frame(bg='#467890')
        F1.pack(expand=True,fill="both")
        f11=Frame(F1,bg='#D1D0CE')
        f11.place(relx=0.5,rely=0.5,anchor='center')
        L1=Label(f11,text="course id" ,font=("Elephant", 14),bg='#E5E4E2' ,bd=3,  highlightthickness=2, highlightbackground='#467890')
        L1.grid(row=0,column=0,padx=10,pady=10)
        self.courseid=Entry(f11)
        self.courseid.grid(row=0,column=1,padx=10,pady=10)
        
        L2=Label(f11,text="course Name",font=("Elephant", 14),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='#467890')
        L2.grid(row=1,column=0,padx=10,pady=10)
        self.coursename=Entry(f11)
        self.coursename.grid(row=1,column=1,padx=10,pady=10)
        btn=Button(f11,text="Add course" ,font=("Arial bold", 12),command=self.addcourse)
        btn.grid(row=2,column=1,padx=10,pady=10)
        
        self.tree=Treeview(f11,columns=('column1','column2'),show='headings' )
        self.tree.heading('column1',text="course id")
        self.tree.heading('column2',text="course name")
        self.tree.grid(row=3,column=1)
        self.getcourses()
        nb.add(F1,text='Add course')
        
        #teachers
        F2=Frame(bg='red')
        F2.pack(expand=True,fill="both")
        f22=Frame(F2,bg='#D1D0CE')
        f22.place(relx=0.5,rely=0.5,anchor='center')
        L1=Label(f22,text="T_id" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L1.grid(row=0,column=0,padx=10,pady=10)
        self.teacherid=Entry(f22)
        self.teacherid.grid(row=0,column=1,padx=10,pady=10)
        
        L2=Label(f22,text="T_name" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L2.grid(row=1,column=0  ,padx=10,pady=10)
        self.teachername=Entry(f22)
        self.teachername.grid(row=1,column=1,padx=10,pady=10)
        
        
        L3=Label(f22,text="T_email" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L3.grid(row=2,column=0,padx=10,pady=10)
        self.teacheremail=Entry(f22)
        self.teacheremail.grid(row=2,column=1,padx=10,pady=10)
        
        L4=Label(f22,text="T_pass" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L4.grid(row=3,column=0,padx=10,pady=10)
        self.teacherpass=Entry(f22)
        self.teacherpass.grid(row=3,column=1,padx=10,pady=10)
        
        self.gender=StringVar(value="male")
        L5=Label(f22,text="T_gender" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L5.grid(row=4,column=0,padx=10,pady=10)
        self.teachergender=Radiobutton(f22,text="male" ,value="male",variable=self.gender)
        self.teachergender.grid(row=4,column=1,padx=10,pady=10)
        self.teachergender1=Radiobutton(f22,text="Female" ,value="Female",variable=self.gender)
        self.teachergender1.grid(row=5,column=1,padx=10,pady=10)
        
        L6=Label(f22,text="T_course" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        L6.grid(row=6,column=0,pady=10)
        self.combo=Combobox(f22,values=self.courses)
        self.combo.grid(row=6,column=1,padx=10,pady=10)
        
        addteacher=Button(f22,text="Add techers",command=self.addteacher,font=("Arial bold", 10))
        addteacher.grid(row=7,column=1,padx=10,pady=10)
        
        self.tree2=Treeview(f22,columns=('column1','column2','column3','column4','column5','column6'),show='headings' )
        self.tree2.heading('column1',text="Teacher id")
        self.tree2.heading('column2',text="Teacher name")
        self.tree2.heading('column3',text="Teacher email")
        self.tree2.heading('column4',text="Teacher pass")
        self.tree2.heading('column5',text="Teacher gender")
        self.tree2.heading('column6',text="Teacher course")
        self.tree2.grid(row=8,column=1)
        self.getteachers()
        
        nb.add(F2,text=' Add Teachers ')
         
        
        
        # #student
        # F3=Frame(bg='red')
        # F3.pack(expand=True,fill="both")
        # f33=Frame(F3,bg='#D1D0CE')
        # f33.place(relx=0.5,rely=0.5,anchor='center')
        # L1=Label(f33,text="S_rollno" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        # L1.grid(row=0,column=0,padx=10,pady=10)
        # self.studentroll=Entry(f33)
        # self.studentroll.grid(row=0,column=1,padx=10,pady=10)
        
        # L2=Label(f33,text="S_name" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        # L2.grid(row=1,column=0  ,padx=10,pady=10)
        # self.studentname=Entry(f33)
        # self.studentname.grid(row=1,column=1,padx=10,pady=10)
        
        
        # L3=Label(f33,text="S_email" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        # L3.grid(row=2,column=0,padx=10,pady=10)
        # self.studentemail=Entry(f33)
        # self.studentemail.grid(row=2,column=1,padx=10,pady=10)
        
        # L4=Label(f33,text="S_pass" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        # L4.grid(row=3,column=0,padx=10,pady=10)
        # self.studentpass=Entry(f33)
        # self.studentpass.grid(row=3,column=1,padx=10,pady=10)
        
        # self.gender1=StringVar(value="male")
        # L5=Label(f33,text="S_gender" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        # L5.grid(row=4,column=0,padx=10,pady=10)
        # self.studentgender=Radiobutton(f33,text="male" ,value="male",variable=self.gender1)
        # self.studentgender.grid(row=4,column=1,padx=10,pady=10)
        # self.studentgender1=Radiobutton(f33,text="Female" ,value="Female",variable=self.gender1)
        # self.studentgender1.grid(row=5,column=1,padx=10,pady=10)
        
        # L6=Label(f33,text="S_course" ,font=("Elephant", 11),bg='#E5E4E2',bd=3,  highlightthickness=2, highlightbackground='red')
        # L6.grid(row=6,column=0,pady=10)
        # self.scombo=Combobox(f33,values=self.courses)
        # self.scombo.grid(row=6,column=1,padx=10,pady=10)
        
        # addstudent=Button(f33,text="Add students",command=self.addstudents,font=("Arial bold", 10))
        # addstudent.grid(row=7,column=1,padx=10,pady=10)
        
        # self.tree3=Treeview(f33,columns=('column1','column2','column3','column4','column5','column6'),show='headings' )
        # self.tree3.heading('column1',text="student roll")
        # self.tree3.heading('column2',text="student name")
        # self.tree3.heading('column3',text="student email")
        # self.tree3.heading('column4',text="student pass")
        # self.tree3.heading('column5',text="student gender")
        # self.tree3.heading('column6',text="student course")
        # self.tree3.grid(row=8,column=1)
        # self.getstudents()
        
        # nb.add(F3,text=' Add Students ')

