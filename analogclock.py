#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import time

import math

window = tk.Tk()
window.geometry("400x400")


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))
    
    seconds_x = seconds_hand_len *math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)
    
    
    minutes_x = minutes_hand_len *math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)
    
    
    
    hours_x = hours_hand_len *math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 *hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)
    window.after(1000,update_clock)
    
    
    
canvas = tk.Canvas(window,width=400, height=400,)
canvas.pack(expand=True, fill="both")
bg=tk.PhotoImage(file='C:\\Users\\Nagesh\\Downloads\\pngkit_clock-png_4197187.png')
canvas.create_image(200,200,image=bg)


center_x = 200
center_y = 200
seconds_hand_len = 95
minutes_hand_len = 80
hours_hand_len = 60


seconds_hand = canvas.create_line(200,200,
                                 200 + seconds_hand_len, 200 + seconds_hand_len,width=1.5, fill='red')
minutes_hand = canvas.create_line(200,200,
                                  200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='black')

hours_hand = canvas.create_line(200,200,
                                200+hours_hand_len,200+hours_hand_len,width=4, fill='blue')


update_clock()
window.mainloop()
                                 
                        

