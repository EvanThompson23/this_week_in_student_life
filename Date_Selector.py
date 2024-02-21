import tkinter as tk
from tkcalendar import DateEntry

class Date_Selector :
   def __init__(self, date_start, date_end):
      self.date_start = date_start
      self.date_end = date_end
      
   def get_date_start (self):
      return self.date_start
   
   def set_date_start (self, date):
      self.date_start = date
      
   def get_date_end (self):
      return self.date_end
   
   def set_date_end (self, date):
      self.date_end = date
   
   def cal_selector(dates):
      my_w = tk.Tk()
      my_w.geometry("400x100") # width and height of window   
      font1=['Times',56,'normal'] # font style to display output 

      cal1=DateEntry(my_w,selectmode='day')
      cal1.grid(row=1,column=0,padx=20,pady=30)
      cal2=DateEntry(my_w,selectmode='day')
      cal2.grid(row=1,column=1,padx=20,pady=30)

      b1=tk.Button(my_w,text='Get Events', bg='lightgreen',
            font=20,command=lambda:my_upd())
      b1.grid(row=1,column=2)
      
      def my_upd(): # triggered on Button Click
         dates.set_date_start(cal1.get_date())
         dates.set_date_end(cal2.get_date())
         my_w.destroy()
      
      my_w.mainloop()
