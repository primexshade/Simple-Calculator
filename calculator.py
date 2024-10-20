from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Calculator")

# Create an entry widget for the display
display = Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button click function
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

# Define clear function
def button_clear():
    display.delete(0, END)

# Define equal function
def button_equal():
    try:
        result = str(eval(display.get()))
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

# Define button creation function
def create_button(text, row, column, command):
    button = Button(root, text=text, padx=20, pady=20, command=command)
    button.grid(row=row, column=column)

# Create number buttons
for i in range(1, 10):
    create_button(str(i), (i-1)//3 + 1, (i-1)%3, lambda i=i: button_click(i))

create_button("0", 4, 0, lambda: button_click(0))

# Create operation buttons
create_button("+", 1, 3, lambda: button_click("+"))
create_button("-", 2, 3, lambda: button_click("-"))
create_button("*", 3, 3, lambda: button_click("*"))
create_button("/", 4, 3, lambda: button_click("/"))

# Create special buttons
create_button("=", 4, 2, button_equal)
create_button("C", 4, 1, button_clear)

# Run the main loop
root.mainloop()