import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.geometry('500x500')

questions = ["Who developed Python Programming Language?",
             "What will be the value of the following Python expression:4 + 3 % 5",
             "What is the method inside the class in python language?",
             "Which of the following declarations is incorrect?",
             "Which of the following data types is shown :L = [2, 54, 'javatpoint', 5] ",
             "What happens when '2' == 2 is executed?",
             "List in Python is ................in nature.",
             "What is the correct syntax for defining a function in Python?",
             "Which of the following is NOT a comparison operator in Python?"             ]



options = [['Wick van Rossum','Rasmus Lerdorf','Guido van Rossum','Niene Stom','Guido van Rossum']
           ,['2','7','4','1','7'],
           ['Object','Function','Attribute','Argument','Function'],
           ['_x = 2','__x = 3','__xyz__ = 5','None of these','None of these'],
           ['Dictionary','Tuple','List','Stack',' List'],
           ['False','True','ValueError occurs','TypeError occurs',' False'],
            ['functionable','mutable','immutable','None of these',' mutable'],
            ['define function(x)','function x()','def x():','None of these',' def x():'],
             ['==','++','!=:','<=','++']]


frame = tk.Frame(root, padx=10, pady=10,bg='#fff')
question_label = tk.Label(frame,height=5, width=28,bg='#567800',fg="blue", 
                          font=('Verdana', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame) 

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))
button_next = tk.Button(frame, text='Next',bg='Orange', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)
button_next.grid(row=6, column=0)


index = 0
correct = 0
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

def checkAnswer(radio):
    global correct, index

    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')

def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'

    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
       
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])
    

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'

displayNextQuestion()

root.mainloop()