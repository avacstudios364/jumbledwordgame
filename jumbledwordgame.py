import tkinter
from tkinter import *
import random
from tkinter import messagebox

root = tkinter.Tk()

answers = ['pass', 'computer', 'head', 'control', 'hat', 'mouse', 'phone']

words = ['saps', 'outercpm', 'daeh', 'trocoln', 'tha', 'ueosm', 'onhpe']

'''
x = random.randrange(3,30,3)

print(x)
'''
#num = tracks the current question
num = random.randrange(0,len(words), 1) #len() gives you total number of items in a list

c = 0 #c = correct answer count
d = 0 #total number of questions attempted by player
s = '' #string for score
l = Label(root)

def reset():
    global num, answers, words
    num = random.randrange(0, len(words), 1)
    label.config(text = words[num])
    e1.delete(0,END)

def default():
    global words
    global answers
    global num
    label.config(text = words[num])


def checkanswer():
    global num, words, answers, c, d, s, l
    d = int(d)+1
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo('Correct!', 'You got it correct!')
        c = c+1
    else:
        messagebox.showinfo('Incorrect!', 'You got it wrong!')
    s = 'Score: '+str(c)+'/'+str(d)
    l.forget()
    l = Label(root, font = ('Verdana',20), text = s, bg = 'black', fg = 'white')
    l.pack(side = LEFT)
    reset()


root.geometry('500x500+450+150')
root.title('Jumbled Word Game')

root.configure(background='black')
Label(root, text = 'Lets play Jumbled Word Game!', fg = 'white', 
        bg = 'black', font = ('Verdana',20)).pack(pady =5)

label = Label(root,font = ('Verdana',17), fg = 'white', bg = 'black', width = 15)
label.pack(pady = 20, ipadx=10, ipady=10)

ans = StringVar()
e1= Entry(root, width = 10, font = ('Verdana',20), 
textvariable = ans, fg = 'black', bg = 'white')
e1.pack(pady = 30,ipadx=10, ipady=10)

b1 = Button(root, text = 'Check', bg = 'green', fg = 'white', bd = 5,
            font = ('Comic sans ms',15), width = 15, command = checkanswer)
b1.pack(pady = 10)

b2 = Button(root, text = 'Change', bg = 'blue', fg = 'white', bd = 5,
            font = ('Comic sans ms',15), width = 15, command = reset)
b2.pack()

default()
root.mainloop()

