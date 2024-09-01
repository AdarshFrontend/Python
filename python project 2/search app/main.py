from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki

def search(): 
    search_data=ent.get()
    data=wiki.summary(search_data,sentences=200)
    ent.set('')
    text.delete(0.0,END)
    search_lb1['text']="Searching result for :{}".format(search_data)
    text.insert(0.0,data)


def enter_pressed(event):
    search()

root=Tk()
root.title('Search application')
root.geometry('320x480')
root.configure(bg='red')

ent=StringVar()
search_entry=Entry(root,width=30 ,font=('arial',12),bd=2,relief=RIDGE,textvariable=ent)
search_entry.bind('<Return>',enter_pressed )
search_entry.place(x=15,y=20)

search_lb1=Label(root,text=' Searching result for :',font=('arial black',12,'bold'),bg='#c0c0c0')
search_lb1.place(x=15,y=70)

text=ScrolledText(root,font=('times',10),bd=4,relief=SUNKEN,wrap=WORD)
text.place(x=15,y=100,height=300,width=300)


search_btn=Button(root,text="Search",font=('arial',12,'bold'),width=10,command=search)
search_btn.place(x=15,y=420)

clear_btn=Button(root,text="Clear",font=('arial',12,'bold'),width=10,
                 command=lambda: text.delete(0.0,END))
clear_btn.place(x=105,y=420)

exit_btn=Button(root,text="Exit",font=('arial',12,'bold'),width=10,
                command=root.quit)
exit_btn.place(x=200 ,y=420)
root.mainloop()