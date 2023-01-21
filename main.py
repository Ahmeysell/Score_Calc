from tkinter import *
import math


# Run operation that selected
def select():
    op_selected = selected.get()
    if op_selected == '1':
        selected.destroy()
        op_button.destroy()

        fin = Entry(Window)
        fin.config(bg="burlywood4")
        fin.place(x=48, y=136)

        mid_button = Button(Window)
        mid_button.config(text="Enter",
                          bg="black",
                          fg="white",
                          command=lambda: mid_calc(int(fin.get())))
        mid_button.place(x=178, y=132)

    elif op_selected == '2':
        selected.destroy()
        op_button.destroy()

        mid = Entry(Window)
        mid.config(bg="burlywood4")
        mid.place(x=48, y=136)

        mid_button = Button(Window)
        mid_button.config(text="Enter",
                          bg="black",
                          fg="white",
                          command=lambda: final_calc(int(mid.get())))
        mid_button.place(x=178, y=132)

    elif op_selected == '3':
        selected.destroy()
        op_button.destroy()

        mid = Entry(Window)
        mid.config(bg="burlywood4")
        mid.place(x=48, y=136)

        final = Entry(Window)
        final.config(bg="burlywood4")
        final.place(x=48, y=156)

        mid_button = Button(Window)
        mid_button.config(text="Enter",
                          bg="black",
                          fg="white",
                          command=lambda: average_calc(int(mid.get()), int(final.get())))
        mid_button.place(x=178, y=142)
    else:
        pass


# Function that finds the Average
def average_calc(mid, final):
    if mid < 100 and final < 100:
        result = mid * 0.3 + final * 0.8
        if result >= 60:
            final = Label(Window)
            final.config(text=f"Your final Score : {result}", font=("Ariel", 15), bg="LavenderBlush4")
            final.place(x=32, y=250)
        else:
            sorry = Label(Window)
            sorry.config(text=f"You shall not PASS!!", font=("Ariel", 15), bg= "red", fg="yellow")
            sorry.place(x=42, y=250)
    else:
        error = Label(Window)
        error.config(text=f"You can not take this score", font=("Ariel", 15), bg="red", fg="yellow")
        error.place(x=18, y=250)
    return


# Function that finds the Final score
def final_calc(mid):
    if mid < 100:
        val1 = 60 - (mid * 0.3)
        result = (val1 * 10) / 8
        result = int(math.ceil(result))
        final = Label(Window)
        final.config(text=f"Your final Score : {result}", font=("Ariel", 15), bg="LavenderBlush4")
        final.place(x=42, y=250)
    else:
        error = Label(Window)
        error.config(text=f"You can not take this score", font=("Ariel", 15), bg="red", fg="yellow")
        error.place(x=18, y=250)
    return


# Function that finds the Midterm score
def mid_calc(fin):
    if fin < 100:
        val1 = 60 - (fin * 0.8)
        result = (val1 * 10) / 3
        result = int(math.ceil(result))
        if 100 > result:
            midterm = Label(Window)
            midterm.config(text=f"Your Midterm Score : {result}", font=("Ariel", 15), bg= "LavenderBlush4")
            midterm.place(x=22, y=250)
        else:
            sorry = Label(Window)
            sorry.config(text=f"You shall not PASS!!", font=("Ariel", 15), bg= "red", fg="yellow")
            sorry.place(x=42, y=250)
    else:
        error = Label(Window)
        error.config(text=f"You can not take this score", font=("Ariel", 15), bg="red", fg="yellow")
        error.place(x=18, y=250)
    return


# For calculate start initial position of window
def windowInitial(S_width, S_height, W_width, W_height):
    initial_x = int((S_width - W_width) / 2)
    initial_y = int((S_height - W_height) / 2)
    yield initial_x
    yield initial_y


# Create window
Window = Tk()

Initial_size = windowInitial(1920, 1080, 270, 400)
Initial_x = next(Initial_size)
Initial_y = next(Initial_size)

# Windows Settings
Window.geometry(f"270x400+{Initial_x}+{Initial_y}")
Window.title("Score Calculater")
Window.resizable(False, False)

# Select operation that you want to do
Operations = Label(Window)
Operations.config(text="1) Midterm Calc\n"
                       "2)      Final Calc\n"
                       "3) Average Calc\n"
                       "Select your operation:", font=("Arial", 15))
Operations.place(x=30, y=10)

# Write the operation that you want to do
selected = Entry(Window)
selected.configure(bg="burlywood1")
selected.place(x=48, y=136)

# Action Button
op_button = Button(Window)
op_button.config(text="Select", bg="black", fg="white", command=select)
op_button.place(x=178, y=132)

mainloop()
