import time

from colors import *

def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size):
        swapped = False
        for j in range(0, size-i-1):
            if data[j] > data[j+1]:   
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))])
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                time.sleep(timeTick)
        
        if swapped == False:
            break
    
    drawData(data, [BLUE for x in range(len(data))])