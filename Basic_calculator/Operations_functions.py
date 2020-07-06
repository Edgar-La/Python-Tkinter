from tkinter import END

def num_(number_, e_):
	e_.insert(END, number_)

def clear_(e_):
	R_ = 0; e_.delete(0, END)

def dot_(e_):
	e_.insert(END, '.')

def add_(e_, Op_):
	global R_; R_ = float(e_.get())
	global Operation_; Operation_ = Op_
	e_.delete(0, END)
def sus_(e_, Op_):
	global R_; R_ = float(e_.get())
	global Operation_; Operation_ = Op_
	e_.delete(0, END)
def mul_(e_, Op_):
	global R_; R_ = float(e_.get())
	global Operation_; Operation_ = Op_
	e_.delete(0, END)
def div_(e_, Op_):
	global R_; R_ = float(e_.get())
	global Operation_; Operation_ = Op_
	e_.delete(0, END)

def eq_(e_):
	second = e_.get()
	e_.delete(0, END)
	if 	(Operation_ == 'Addition'): e_.insert(0, R_ + float(second))
	elif 	(Operation_ == 'Substraction'): e_.insert(0, R_ - float(second))
	elif 	(Operation_ == 'Multiplication'): e_.insert(0, R_ * float(second))
	elif 	Operation_ == 'Division':
		if (float(second) != 0): e_.insert(0, R_ / float(second))
		elif (float(second) == 0.0): e_.insert(0, 'SYNTAX_ERROR')


def act_(e_):
	return
