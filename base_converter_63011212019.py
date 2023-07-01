# โปรแกรมแปลงเลขฐาน BY'Arthit Thaweebot 63011212019
from tkinter import *
from tkinter import ttk
import tkinter
# กำหนด GUI
GUI = tkinter.Tk()
GUI.maxsize(320, 380)
GUI.minsize(320, 380)
GUI.geometry('300x380')
GUI.title('โปรแกรมแปลงเลขฐาน')
# ตัวแปร
inputnumber = StringVar()
inputbasenumber = StringVar()
sum_all = StringVar()
result = StringVar()
# เลือกเลขฐาน 1 -16
bases = [str(i) for i in range(1, 17)]
ttk.Style().configure("style1.TCombobox", foreground = "blue", background = "black")
# การคำนวณเลขฐาน
def Cal():
        sum = 0
        input_number = (inputnumber.get())
        base = len(input_number)
        base_number = int(sum_all.get())
        for i in range(base):
                if(input_number[i].upper()=="A"):
                        number = 10
                elif(input_number[i].upper()=="B"):
                        number = 11
                elif(input_number[i].upper()=="C"):
                        number = 12
                elif(input_number[i].upper()=="D"):
                        number = 13
                elif(input_number[i].upper()=="E"):
                        number = 14
                elif(input_number[i].upper()=="F"):
                        number = 15
                else:
                        number = int(input_number[i])
                sum = sum + number*(base_number**(base-1))
                base -= 1
        oct = ""
        num = (sum)
        con = int(inputbasenumber.get())
        while num != 0:
                binary = num % con
                if (binary == 10):
                        binary = 'A'
                if (binary == 11):
                        binary = 'B'
                if (binary == 12):
                        binary = 'C'
                if (binary == 13):
                        binary = 'D'
                if (binary == 14):
                        binary = 'E'
                if (binary == 15):
                        binary = 'F'
                oct += str(binary) 
        num = num//con
        volumn = "ผลลัพธ์ : {:}".format(oct[::-1])
        result.set(volumn)
def clear():
        inputnumber.set('')
        sum_all.set('')
        inputbasenumber.set('')
        result.set('')
def exit():
        GUI.destroy()
# ช่อง ป้อนตัวเลข
text_inputnumber = ttk.Label(GUI, text = 'ป้อนตัวเลข', font = ('Angsana New',15))
text_inputnumber.pack(padx = 10, pady = 5)
channel_1 = ttk.Entry(GUI, textvariable = inputnumber)
channel_1.pack(padx=10,pady=5)
# ช่อง จากเลขฐาน
text_basenumber = ttk.Label(GUI, text = 'จากเลขฐาน', font = ('Angsana New',15))
text_basenumber.pack(padx = 10, pady = 5)
channel_2 = ttk.Combobox(GUI, textvariable = sum_all, values = bases, style = "style1.TCombobox", font = "ms-sans 10")
channel_2.pack(padx = 10, pady = 5)
# ช่อง เป็นเลขฐาน
text_basenumber = ttk.Label(GUI, text = 'เป็นเลขฐาน', font = ('Angsana New',15))
text_basenumber.pack(padx = 10, pady = 5)
channel_3 = ttk.Combobox(GUI, textvariable = inputbasenumber , values = bases, style = "style1.TCombobox", font = "ms-sans 10")
channel_3.pack(padx = 10, pady = 5)
# ปุ่ม OK
button_ok = ttk.Button(GUI, text = 'OK',command = Cal)
button_ok.pack()
result_num = Label(GUI, textvariable = result, bg = "#F5F5F5", fg = "black", pady = 20, font = ('Angsana New',20))
result_num.pack(anchor = "center", fill = X)
# ปุ่ม Clear
button_clear = Button(GUI, text='Clear', font = 'AngsanaNew 10 bold', width = 5, relief = GROOVE, bd = 5, command = clear)
button_clear.pack(padx = 10, pady = 5, side = tkinter.LEFT)
# ปุ่ม Exit
button_exit = Button(GUI, text = 'Exit', font = 'AngsanaNew 10 bold', width = 5, relief = GROOVE, bd = 5, command = exit)
button_exit.pack(padx = 10, pady = 5, side = tkinter.RIGHT)
GUI.mainloop()