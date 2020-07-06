from tkinter import *
import Operations_functions as OpFu

root = Tk()
root.title('Simple calculator')
root.configure(background='#263238')
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

button_l = Button(root, text = '(', padx = 35, pady = 35, bg = '#004D40', fg = 'white', command = lambda: OpFu.act_()).grid(row = 1, column = 0)
button_r = Button(root, text = ')', padx = 35, pady = 35, bg = '#004D40', fg = 'white', command = lambda: OpFu.act_()).grid(row = 1, column = 1)
button_C = Button(root, text = 'C', padx = 35, pady = 35, bg = '#004D40', fg = 'white', command = lambda: OpFu.clear_(e)).grid(row = 1, column = 2)
button_div = Button(root, text = '/', padx = 34, pady = 35, bg = '#00796B', fg = 'white', command = lambda: OpFu.div_(e, 'Division')).grid(row = 1, column = 3)

button_1 = Button(root, text = '1', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(1, e)).grid(row = 4, column = 0)
button_2 = Button(root, text = '2', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(2, e)).grid(row = 4, column = 1)
button_3 = Button(root, text = '3', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(3, e)).grid(row = 4, column = 2)
button_add = Button(root, text = '+', padx = 34, pady = 35, bg = '#00796B', fg = 'white', command = lambda: OpFu.add_(e, 'Addition')).grid(row = 4, column = 3)

button_4 = Button(root, text = '4', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(4, e)).grid(row = 3, column = 0)
button_5 = Button(root, text = '5', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(5, e)).grid(row = 3, column = 1)
button_6 = Button(root, text = '6', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(6, e)).grid(row = 3, column = 2)
button_sus = Button(root, text = '-', padx = 36.4, pady = 35, bg = '#00796B', fg = 'white', command = lambda: OpFu.sus_(e, 'Substraction')).grid(row = 3, column = 3)

button_7 = Button(root, text = '7', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(7, e)).grid(row = 2, column = 0)
button_8 = Button(root, text = '8', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(8, e)).grid(row = 2, column = 1)
button_9 = Button(root, text = '9', padx = 35, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(9, e)).grid(row = 2, column = 2)
button_mul = Button(root, text = 'x', padx = 35, pady = 35, bg = '#00796B', fg = 'white', command = lambda: OpFu.mul_(e, 'Multiplication')).grid(row = 2, column = 3)

button_0 = Button(root, text = '0', padx = 79, pady = 35, bg = '#263238', fg = 'white', command = lambda: OpFu.num_(0, e)).grid(row = 5, column = 0, columnspan = 2)
butoon_dot = Button(root, text = '.', padx = 37, pady = 35,bg = '#263238', fg = 'white', command = lambda: OpFu.dot_(e)).grid(row = 5, column = 2)
butoon_eq = Button(root, text = '=', padx = 35, pady = 35, bg = '#009688', fg = 'white', command = lambda: OpFu.eq_(e)).grid(row = 5, column = 3)

root.mainloop()