from tkinter import *
from tkinter import ttk

import random

from colors import BLACK

#Creating the window
window = Tk()
window.title("Sorting Algorithm Visualizer")
window.maxsize(1000, 700)
window.config(bg = 'white')

#This function will draw the randomly generated data on the canvas as vertical bars
def drawdata(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

#This function will generate the array with random values
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawdata(data, ['BLUE' for x in range(len(data))])

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
UI_Frame = Frame(window, width=900, height=300, bg='white')
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
canvas = Canvas(window, width=800, height=400, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()