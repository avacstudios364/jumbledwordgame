from tkinter import *
import random
from tkinter import messagebox

root = Tk()

answers = ['pass', 'computer', 'head', 'control', 'hat', 'mouse']

words = ['saps', 'outercpm', 'daeh', 'trocoln', 'tha', 'ueosm']

'''
x = random.randrange(3,30,3)

print(x)
'''

num = random.randrange(0,len(words), 1) #len() gives you total number of items in a list

c = 0 #c = correct answer count
d = 0 #total number of questions attempted by player
s = '' #string for score
l = Label(root)

def reset():
    pass

def default():
    global words
    global answers
    global num
    label.config(text = words[num])


def checkanswer():
    pass


root.geometry('500x500+450+150')
root.title('Jumbled Word Game')

root.configure(background='black')
Label(root, text = 'Lets play Jumbled Word Game!', fg = 'white', 
        bg = 'black', font = ('Verdana',20)).pack(pady =5)

label = Label (root, fg = 'white', bg = 'black', font = ('Verdana',17))
label.pack(pady = 20, ipadx=10, ipady=10)

ans = StringVar()
e1= Entry(root, width = 10, font = ('Verdana',20), fg = 'white', bg = 'black')
e1.pack(pady = 30,ipadx=10, ipady=10)

b1 = Button(root, text = 'Check', bg = 'green', fg = 'white', bd = 5,
            font = ('Comic sans ms',15), width = 15, command = None)
b1.pack(pady = 10)

b2 = Button(root, text = 'Change', bg = 'blue', fg = 'white', bd = 5,
            font = ('Comic sans ms',15), width = 15, command = None)
b2.pack()

#default()
root.mainloop()

