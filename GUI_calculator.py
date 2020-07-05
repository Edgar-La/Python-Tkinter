from tkinter import *

root = Tk()
root.title('Simple calculator')
root.configure(background='#263238')
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)


def num_(number_):
	#e.delete(0, END)
	e.insert(END, number_)
	#e.get() 
def clear_():
	R_ = 0
	e.delete(0, END)

def dot_():
	e.insert(END, '.')

def sum_():
	return
def dot_():
	return
def eq_():
	return
def act_():
	return

button_l = Button(root, text = '(', padx = 35, pady = 35, bg = '#004D40', fg = 'white', command = lambda: act_()).grid(row = 1, column = 0)
button_r = Button(root, text = ')', padx = 35, pady = 35, bg = '#004D40', fg = 'white', command = lambda: act_()).grid(row = 1, column = 1)
button_C = Button(root, text = 'C', padx = 35, pady = 35, bg = '#004D40', fg = 'white', command = clear_).grid(row = 1, column = 2)
button_div = Button(root, text = '%', padx = 34, pady = 35, bg = '#00796B', fg = 'white', command = lambda: act_()).grid(row = 1, column = 3)

button_1 = Button(root, text = '1', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(1)).grid(row = 4, column = 0)
button_2 = Button(root, text = '2', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(2)).grid(row = 4, column = 1)
button_3 = Button(root, text = '3', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(3)).grid(row = 4, column = 2)
button_sum = Button(root, text = '+', padx = 34, pady = 35, bg = '#00796B', fg = 'white', command = sum_).grid(row = 4, column = 3)

button_4 = Button(root, text = '4', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(4)).grid(row = 3, column = 0)
button_5 = Button(root, text = '5', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(5)).grid(row = 3, column = 1)
button_6 = Button(root, text = '6', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(6)).grid(row = 3, column = 2)
button_sus = Button(root, text = '-', padx = 36.4, pady = 35, bg = '#00796B', fg = 'white', command = lambda: act_()).grid(row = 3, column = 3)

button_7 = Button(root, text = '7', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(7)).grid(row = 2, column = 0)
button_8 = Button(root, text = '8', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(8)).grid(row = 2, column = 1)
button_9 = Button(root, text = '9', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(9)).grid(row = 2, column = 2)
button_mul = Button(root, text = 'x', padx = 35, pady = 35, bg = '#00796B', fg = 'white', command = lambda: act_()).grid(row = 2, column = 3)

button_0 = Button(root, text = '0', padx = 79, pady = 35, bg = '#263238', fg = 'white', command = lambda: num_(0)).grid(row = 5, column = 0, columnspan = 2)
butoon_dot = Button(root, text = '.', padx = 37, pady = 35,bg = '#263238', fg = 'white', command = dot_).grid(row = 5, column = 2)
butoon_eq = Button(root, text = '=', padx = 35, pady = 35, bg = '#009688', fg = 'white', command = eq_).grid(row = 5, column = 3)


root.mainloop()