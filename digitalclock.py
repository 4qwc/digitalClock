# progame  clock
# by hs4qwc 
# date 12/1/2020


from tkinter import *
import datetime
import time as tm
import winsound
################ MAIN LABEL #####################
guiClock = Tk()
guiClock.title("Alarm Clock")
guiClock.iconbitmap(r"Clock1.ico")
guiClock.geometry("600x100")



frame = Frame(guiClock)
frame.pack()

#######################################
def NOW_TIME():

	now = tm.strftime("%H:%M:%S")  # เวลาปัจจุบัน
	CLOCK_DISTPLAY["text"] = now
	print('เวลา:', now)

	date = tm.strftime("%d/%m/%Y") 
	print("วันที่:",date)
	DATE_DISTPLAY["text"] = date
	frame.after(1000, NOW_TIME)     # กำหนดให้ฟังก์ชั่นทำงานซ้ำ 1 วิ
			
CLOCK_DISTPLAY = Label(frame, fg="red", font=("Arial", 45, 'bold'),bg='blue')
CLOCK_DISTPLAY.grid(row=1, column=1)

DATE_DISTPLAY = Label(frame, fg="white", font=("Arial", 45, 'bold'),bg='gray')
DATE_DISTPLAY.grid(row=1, column=0)

NOW_TIME() # เรียกฟังชั่นมาใช้งาน


guiClock.mainloop()
