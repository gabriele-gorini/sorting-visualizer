from tkinter import *
from tkinter import ttk

import random


from colors import *
from algorithms.bubblesort import bubble_sort
from algorithms.insertionsort import insertion_sort
from algorithms.mergesort import merge_sort
from algorithms.quicksort import quick_sort

#Creating the window
window = Tk()
window.title("Sorting Algorithm Visualizer")
window.maxsize(1000, 700)
window.config(bg = WHITE)

#This function will draw the randomly generated data on the canvas as vertical bars
def drawData(data, colorArray):
    canvas.delete('all')
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

    drawData(data, [BLUE for x in range(len(data))])

#This function will return the timeout between the operations
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

#This function will start the sorting process with the selected algorithm
def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)

def is_sorted():
    global data
    print(data)
    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            return False

    return True

#Used from the user to select which algorithm he wants to use
algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort', 'Insertion Sort', 'Quick Sort']

#Used from the user to select the speed of the execution
speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

#The array that is going to be sorted
data = []

#UI generation
UI_Frame = Frame(window, width=900, height=300, bg=WHITE)
UI_Frame.grid(row=0, column=0, padx=10, pady=5)

#Algorithm selection dropdown menu
algo_label = Label(UI_Frame, text="Algorithm: ", bg=WHITE)
algo_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_Frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

#Sorting speed selection dropdown menu
speed_label = Label(UI_Frame, text="Sorting Speed: ", bg=WHITE)
speed_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_Frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

#Sort Button
sort_btn = Button(UI_Frame, text="Sort", command=sort, bg=LIGHT_GRAY)
sort_btn.grid(row=2, column=1, padx=5, pady=5)

#Generate Array Button
generate_btn = Button(UI_Frame, text = "GenerateArray", command=generate, bg=LIGHT_GRAY)
generate_btn.grid(row=2, column=0, padx=5, pady=5)

#Canvas for array drawing
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

#Generate first random array
generate()

window.mainloop()