from tkinter import *
root = Tk()

def __one__(event):
    global a
    a = 1

def __two__(event):
    global a
    a = 2

def __tree__(event):
    global a
    a = 3

def __four__(event):
    global a
    a = 4

def __five__(event):
    global a
    a = 5

def hello(event):
    print('Yet another Hello World, Motherfucker')
    print(a)

bnt = Button(root,
             text="click me!",
             width=30, height=15,
             bg="white", fg="black")
bnt.bind('<Button-1>', hello)
bnt.pack()

one = Button(root, text = '1')
one.bind('<Button-1>', __one__)
one.grid(row = 1, column = 1)

two = Button(root, text = '2')
two.bind('<Button-1>', __two__)
two.grid(row = 1, column = 2)

tree = Button(root, text = '3')
tree.bind('<Button-1>', __tree__)
tree.grid(row = 1, column = 3)

four = Button(root, text = '4')
four.bind('<Button-1>', __four__)
four.grid(row = 2, column = 1)

five = Button(root, text = '5')
five.bind('<Button-1>', __five__)
five.grid(row = 2, column = 2)

six = Button(root, text = '6')
six.bind('<Button-1>', __six__)
six.grid(row = 2, column = 3)

seven = Button(root, text = '7')
seven.bind('<Button-1>', __seven__)
seven.grid(row = 3, column = 1)

osem = Button(root, text = '8')
osem.bind('<Button-1>', __osem__)
osem.grid(row = 3, column = 2)

nine = Button(root, text = '9')
nine.bind('<Button-1>', __nine__)
nine.grid(row = 3, column = 3)

zero = Button(root, text = '0')
zero.bind('<Button-1>', __zero__)
zero.grid(row = 4, column = 1, columnspam = 3)

root.mainloop()
