#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import time

window=tk.Tk()

def update_clock():
  
  date= time.strftime("%d")
  year = time.strftime("%Y")
  week = time.strftime("%a")
  month = time.strftime("%h")
  hours = time.strftime("%I")
  minutes= time.strftime("%M")
  seconds = time.strftime("%S")
  am_or_pm =time.strftime("%p")
  time_text=hours+ ": " +minutes+ " :" +seconds+ " "+am_or_pm+" "+week+" "+date+" "+month+" "+year
  digital_clock_label.config(text=time_text)
  digital_clock_label.after(1000,update_clock)
  
digital_clock_label=tk.Label(window, text="date:year:month:week:00:00:00:",font="Helvetica 36 bold",bg="white",fg="black")

digital_clock_label.pack()

update_clock()
window.mainloop()

