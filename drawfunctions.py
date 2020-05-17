import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
import math

root = Tk()        
root.geometry('500x275')
root.title('Input Functions')
# Spacer
Label(root, text = '       ').grid(row=0,column=0)

e1 = Entry(root, width=45, borderwidth = 5)
Label(root, text = 'Function 1 :     y =').grid(row=0,column=1)
e1.grid(row=0, column=2, columnspan = 3, padx = 10, pady=20)

e2 = Entry(root, width=45, borderwidth = 5)
Label(root, text = 'Function 2 :    y =').grid(row=1,column=1)
e2.grid(row=1, column=2, columnspan = 3, padx = 10, pady=20)

start = Entry(root, width=5, borderwidth = 5)
Label(root, text = 'Plot from (Default -10 to 10): ').grid(row=3,column=1)
start.insert(0, -10)
start.grid(row=3, column=2,padx = 10)


Label(root, text = 'to').place(relx = 0.65, rely = 0.53, anchor = CENTER)

end = Entry(root, width=5, borderwidth = 5)
#Label(root, text = '                                              To : ').grid(row=3,column=3)
end.insert(0,'10')
end.grid(row=3, column=3,padx = 10)


def plot_func():
    if start.get() == '':
        left = -10
    else:
        left = int(start.get())
    if end.get() == '':
        right = 10
    else:
        right = int(end.get())
    
    x = np.arange(left, right+0.2, 0.2)
    func1 = e1.get()
    func2 = e2.get()
    if 'sqrt' in (func1 or func2):
        func1 = func1.replace('sqrt', 'np.sqrt')
        func2 = func2.replace('sqrt', 'np.sqrt')
    f1 = eval(func1)
    f2 = eval(func2)
    plt.figure(figsize = (6,6))
    # plt.scatter(x, f2, color = 'r', marker = 'x')
    # plt.scatter(x, f1, color = 'b', marker = 'o')
    #Draws line connecting the points
    plt.plot(x, f1, color = 'b', label = f'y = {e1.get()}')    
    plt.plot(x, f2, color = 'r', label = f'y = {e2.get()}')
    #Adds gridlines to the graph
    plt.grid()
    #Sets axes limits
    plt.xticks = (np.arange(min(x), max(x)))
    #Draws the x and y lines of origin
    plt.axhline(0, color = 'black', lw = 1.5)
    plt.axvline(0, color = 'black', lw = 1.5)

    #Add legend to the plot
    plt.legend(bbox_to_anchor=(1, 1.15))
    plt.show()
    
def _quit():
    root.quit()     # stops mainloop
    root.destroy()   
    
enter = Button(root, text = 'Plot', padx = 50, pady = 10, command = plot_func)
enter.grid(row = 4, column = 2, pady = 10)

quit = enter = Button(root, text = 'Quit', padx = 50, pady = 10, command = _quit)
quit.grid(row=4, column = 3, pady = 10)



root.mainloop()