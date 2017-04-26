
#
#  sg_calculator_tkinter.py
#
#
"""
this is an attempt to convert Joe's sample calculator example using simplegui
 into something similar using tkinter, with some additional tkinter widgets
 tossed in.

demonstrates Tkinter widgets Frame, Button, Label, Entry, Text and Scrollbar

This runs in Python 3.2.3 but will require a change from
 tkinter to Tkinter in the first line of code to work with Python 2.7

"""

# calculator with all buttons

#  http://www.codeskulptor.org/#examples-buttons.py  # this is the starting point
#

#  import simplegui

from Tkinter import *  # replaces the simplegui call


# create frame
#  f = simplegui.create_frame("Calculator",300,300)

# create a root window
#
root = Tk()
root.title("Calculator")
root.geometry("450x300")

# create a frame in the window to hold other widgets
#
app = Frame(root)
app.grid()
# intialize variables
#
store = 0
operand = 0
button_width = 12    # used to set width of the buttons


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand in Display box """
    print ("Store = ", store)
    print ("Operand = ", operand)
    print ("")

    entry_box.delete(0,END)     # clears text input box

    t_box.delete(0.0, END)      # clears 'Result' text output box
    t_box.insert(0.0, store)    # writes 'store' value to 'Result' box

    t_disp.insert(0.0, '\n')           # block for 'Display' text box
    t_disp.insert(0.0, "operand = " + str(operand))
    t_disp.insert(0.0, '\n')
    t_disp.insert(0.0, "store = " + str(store))
    t_disp.insert(0.0, '\n')

"""
the above lines insert at the upper-left corner of the text box, which makes
 sense for this example.  But often you want to append the text to the bottom
 of the existing text instead.  The next line shows how do that, switching
 0.0 to END

#    t_disp.insert(END, "operand = " + str(operand))   etc.

"""

def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()

def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()

def enter_num(t):
    """ enter a new operand"""
    global operand
    str = entry_box.get()   # this is new, the .get() method for the Entry widget
    operand = float(str)
    output()


"""
The next block describes the Buttons
"""
#  http://www.tutorialspoint.com/python/tk_button.htm
#  http://effbot.org/tkinterbook/button.htm
#
#  this is probably clear by now, but I'll break down one pair of lines to be sure
#
#  pr_button = Button(app, text = "Print", command = output, width=button_width)
#
# 'pr_button' is the variable name I assigned to this button
# 'Button' is the tkinter keyword for this widget
# 'app' is the name I gave the Frame where we are placing the button
# 'text' is what appears written on the button
# 'command' is the event handler that executes when the button is clicked
# 'width' is the width in characters (not pixels) of the default font
#
# pr_button.grid(column = 0, row = 0, padx = 2, pady = 2)
#
# 'pr_button.grid' signifies we are doing the layout using the grid mode
# 'column' is the column number within app
# 'row' is the row number within app
# 'padx' and 'pady' are optional and separate the buttons by 2 pixels
#
# there are 35 possible Button configurations and we only used six of them!
#
pr_button = Button(app, text = "Print", command = output, width=button_width)
pr_button.grid(column = 0, row = 0, padx = 2, pady = 2)

swap_button = Button(app, text = "Swap", command = swap, width=button_width)
swap_button.grid(column = 0, row = 1, padx = 2, pady = 2)

add_button = Button(app, text = "Add", command = add, width=button_width)
add_button.grid(column = 0, row = 2, padx = 2, pady = 2)

sub_button = Button(app, text = "Subtract", command = sub, width=button_width)
sub_button.grid(column = 0, row = 3, padx = 2, pady = 2)

mult_button = Button(app, text = "Mult", command = mult, width=button_width)
mult_button.grid(column = 0, row = 4, padx = 2, pady = 2)

div_button = Button(app, text = "Div", command = div, width=button_width)
div_button.grid(column = 0, row = 5, padx = 2, pady = 2)

#
#  this is a new widget, of type Label.  This one is a blank to create a space
#
Lblank = Label(app, text="")
Lblank.grid(column = 0, row = 6, padx = 2, pady = 2)

# this is a label for the entry box.  Should be pretty clear by now
#
L1 = Label(app, text="Enter number:")
L1.grid(column = 0, row = 7, padx = 2, pady = 2)

# this is the Entry widget, used to display a single line of input text.
#  believe it or not, this widget has 36 (!) configuration options
#  http://effbot.org/tkinterbook/entry.htm
#
entry_box = Entry(app, width=button_width)
entry_box.grid(column = 0, row = 8, padx = 2, pady = 2)
entry_box.bind('<Return>', enter_num)

L_t_box = Label(app, text="Result:")
L_t_box.grid(column = 1, row = 0, padx = 6, pady = 2)

t_box = Text(app, width = 30, height = 2)
t_box.grid(row = 0, column = 2, rowspan = 2, columnspan = 2, pady = 10, padx = 6, sticky = N)

L_t_disp = Label(app, text="Display:")
L_t_disp.grid(column = 1, row = 3, padx = 6, pady = 2)

t_disp = Text(app, width = 30, height = 6)
t_disp.grid(row = 3, column = 2, rowspan = 4, columnspan = 2,  sticky = 'N')

# this is the Scrollbar widget, used to implement scrolled listboxes, canvases, and text fields.
#  http://effbot.org/tkinterbook/scrollbar.htm (good luck understanding it fully)
#
#  this one is linked to the "t_disp" Text widget above.
#    syncing this correctly (I still don't have it 100%) was the hardest part
#    of building this calculator
#
scrl = Scrollbar(app, command = t_disp.yview)
scrl.grid(row = 3, column = 2, rowspan = 4, columnspan = 2, sticky = 'N,S,E')

#  define both the Text (or Listbox or whatever) and the
#   Scrollbar before doing the .config() below or it won't work
#
t_disp.config(yscrollcommand = scrl.set)
scrl.config(command = t_disp.yview)

# get frame rolling
# f.start()
mainloop()

