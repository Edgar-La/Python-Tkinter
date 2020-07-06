from tkinter import *

root = Tk()
root.title('Simple calculator')
root.configure(background='#263238')
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def num_(number_):
	#e.dele
	e.insert(END, number_) 
def clear_():
	R_ = 0
	e.delete(0, END)

def dot_():
	e.insert(END, '.')

def sum_():
	global R_
	R_ = float(e.get())
	global Operation_
	Operation_ = 'Sum'
	e.delete(0, END)
def sus_():
	global R_
	R_ = float(e.get())
	global Operation_
	Operation_ = 'Substraction'
	e.delete(0, END)
def mul_():
	global R_
	R_ = float(e.get())
	global Operation_
	Operation_ = 'Multiplication'
	e.delete(0, END)
def div_():
	global R_
	R_ = float(e.get())
	global Operation_
	Operation_ = 'Division'
	e.delete(0, END)

def eq_():
	second = e.get()
	e.delete(0, END)
	if 	Operation_ == 'Sum':
		e.insert(0, R_ + float(second))
	elif 	Operation_ == 'Substraction':
		e.insert(0, R_ - float(second))
	elif 	Operation_ == 'Multiplication':
		e.insert(0, R_ * float(second))
	elif 	Operation_ == 'Division':
		e.insert(0, R_ / float(second))

def act_():
	return
