import time

from colors import *

def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]

        j=i-1
        while j>=0 and key < data[j]:
            drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))])
            #The swap operation is not actually part of the algorithm, it has been added for animation purpose
            data[j], data[j+1]= data[j+1], data[j]
            j -= 1
        data[j+1] = key
    
    drawData(data, [BLUE for x in range(len(data))])