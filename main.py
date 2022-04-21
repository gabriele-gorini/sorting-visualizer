from tkinter import *
from tkinter import ttk

import random

from colors import BLACK

#Creating the window
window = Tk()
window.title("Sorting Algorithm Visualizer")
window.geometry("%sx%s" % (window.winfo_screenwidth(), window.winfo_screenheight()))
window.maxsize(window.winfo_screenwidth(), window.winfo_screenheight())
window.config(bg = 'WHITE')

#This function will generate the array with random values
def generate():
    pass

#This function will start the sorting process with the selected algorithm
def sort():
    pass

#Used from the user to select which algorithm he wants to use
algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'MergeSort', 'Insertion Sort', 'Quick Sort']

#Used from the user to select the speed of the execution
speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

#The array that is going to be sorted
data = []

#UI generation
UI_Frame = Frame(window, width=window.winfo_width(), height=300, bg='black')
UI_Frame.grid(row=0, column=0, padx=10, pady=5)

#Algorithm selection dropdown menu
algo_label = Label(UI_Frame, text="Algorithm: ", bg='white')
algo_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_Frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

#Sorting speed selection dropdown menu
speed_label = Label(UI_Frame, text="Sorting Speed: ", bg='white')
speed_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_Frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

#Sort Button
sort_btn = Button(UI_Frame, text="Sort", command=sort, bg='grey')
sort_btn.grid(row=2, column=1, padx=5, pady=5)

#Generate Array Button
generate_btn = Button(UI_Frame, text = "GenerateArray", command=generate, bg='grey')
generate_btn.grid(row=2, column=0, padx=5, pady=5)

#Canvas for array drawing
canvas = Canvas(window, width=800, height=400, bg='black')
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()