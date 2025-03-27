from tkinter import *
import random
import time
root = Tk()
root.geometry("1580x750+0+0")
root.title("ร้านอาหารวิศวกรรมศาสตร์ ศรีราชา")
root.configure(bg="seashell2")

Tops = Frame(root,width = 1500,height = 50,bg = "wheat",relief = SUNKEN)
Tops.pack(side = TOP)



f1 = Frame(root,width = 800,height = 700,bg = "seashell2",relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root,width = 300,height = 700,bg = "seashell2",relief = SUNKEN)
f2.pack(side = RIGHT)

signal_status = StringVar()
  # Default state
signal_color = StringVar()
signal_color.set("light grey")  # Default color


#====================Difine variable and function=======
text_Input = StringVar()
operator = ""

def btnClick(number):
    global operator 
    operator = operator + str(number)
    text_Input.set(operator)
    
def btnClear():
    global operator
    operator = ""
    text_Input.set("")
    

def btnEqual():
    global operator
    Calculate = str(eval(operator))
    text_Input.set(Calculate)
    operator = ""
    
def btnTotalClick():
    CoMeu1 = 0
    try:
        CoMenu1 = int(Menu1.get)
    except:
        Menu1.set(0)
    finally:
        Cost = CoMenu1 * MenuPrice[0]
    

def btnReset():
    Menu1.set("")
    Menu2.set("")
    Menu3.set("")
    Menu4.set("")
    Menu5.set("")
    Menu6.set("")
    
def update_signal(can_pass):
    if can_pass:
        signal_status.set("Pass")
        signal_color.set("green")
    else:
        signal_status.set("Denied")
        signal_color.set("red")
        
def refresh_color():
    signal_label.config(bg=signal_color.get())  # Update background color
    root.after(100, refresh_color) 

def btnExit():
    root.destroy()

#====================Time===============================
localtime = time.asctime(time.localtime(time.time()))

_ = Label(Tops,font = ('TH Saraban New',50,'bold'),text = "ระบบชำระค่าทางด่วน"
               ,fg="Blue",bd = 10,anchor = 'w',bg = "seashell2")

_.grid(row = 0,column = 0)

_ = Label(Tops,font = ('TH Saraban New',20,'bold'),text = localtime
               ,fg="Blue",bd = 10,anchor = 'w',bg = "seashell2")
_.grid(row = 1,column = 0)

#===================Calculaotr Frame=========================

_ = Entry(f2,font=('TH Saraban New',20,'bold'),textvariable = text_Input,
          bd = 30,insertwidth = 4,bg = "powder blue",justify = 'right')

_.grid(columnspan = 4)

#===================Raw 1====================================
_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "7",bg = "powder blue",command = lambda:btnClick(7)).grid(row = 2,column = 0)

_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "8",bg = "powder blue",command = lambda:btnClick(8)).grid(row = 2,column = 1)

_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "9",bg = "powder blue",command = lambda:btnClick(9)).grid(row = 2,column = 2)


#===================Raw 2====================================
_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "4",bg = "powder blue",command = lambda:btnClick(4)).grid(row = 3,column = 0)

_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "5",bg = "powder blue",command = lambda:btnClick(5)).grid(row = 3,column = 1)

_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "6",bg = "powder blue",command = lambda:btnClick(6)).grid(row = 3,column = 2)


#===================Raw 3====================================
_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "1",bg = "powder blue",command = lambda:btnClick(1)).grid(row = 4,column = 0)

_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "2",bg = "powder blue",command = lambda:btnClick(2)).grid(row = 4,column = 1)

_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "3",bg = "powder blue",command = lambda:btnClick(3)).grid(row = 4,column = 2)


#===================Raw 4====================================

_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',20,'bold'),
           text = "0",bg = "powder blue",command = lambda:btnClear()).grid(row = 5,column = 1)


#===================Raw 5====================================

_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',12,'bold'),
           text = "Confirm",bg = "powder blue",command = lambda:btnClear()).grid(row = 2,column = 4)
_ = Button(f2,padx = 22,pady = 8,fg = 'black',font = ('TH Sarabun New',13,'bold'),
           text = "Cancel",bg = "powder blue",command = lambda:btnClear()).grid(row = 3,column = 4)


#====================Menu Info===============================
rand = StringVar()
Menu1 = StringVar()
Menu2 = StringVar()
Menu3 = StringVar()
Menu4 = StringVar()
Menu5 = StringVar()
Menu6 = StringVar()
Cost = StringVar()
Service = StringVar()
TotalCost = StringVar()
Tax = StringVar()
CostPTax = StringVar()


_ = Label(f1,font=('TH sarabun New',18,'bold'),text = "Card ID :",bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 0,column= 0)
_ = Label(f1,font = ('TH Sarabun New',18,'bold'),textvariable = rand,
          bd = 10,width = 16,bg = "powder blue",
          justify = 'right').grid(row = 0,column = 1)

_ = Label(f1,font=('TH sarabun New',18,'bold'),text  = "Entry point :",bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 1,column= 0)
_ = Label(f1,font=('Th Sarabun New',18,'bold'),textvariable=Menu1,
          bd = 10,width=16,bg="powder blue",justify='right').grid(row = 1,column=1)

_ = Label(f1,font=('TH sarabun New',18,'bold'),text  = "Exit point :",bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 2,column= 0)
_ = Label(f1,font=('Th Sarabun New',18,'bold'),textvariable=Menu2,
          bd = 10,width=16,bg="powder blue",justify='right').grid(row = 2,column=1)

_ = Label(f1,font=('TH sarabun New',18,'bold'),text  = "Status :",bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 3,column= 0)
_ = Label(f1,font=('Th Sarabun New',18,'bold'),textvariable=Menu2,
          bd = 10,width=16,bg="powder blue",justify='right').grid(row = 3,column=1)

_ = Label(f1,font=('TH sarabun New',18,'bold'),text  = "Email :",bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 4,column= 0)
_ = Entry(f1,font=('Th Sarabun New',18,'bold'),textvariable=Menu2,
          bd = 10,insertwidth=4,bg="powder blue",justify='right').grid(row = 4,column=1)

_ = Button(f1,padx = 10,pady = 8,fg = 'black',font = ('TH Sarabun New',12,'bold'),
           text = "Send",bg = "light gray",command = lambda:btnClear()).grid(row = 4,column = 2)

_ = Label(f1,font=('TH sarabun New',18,'bold'),text  = "OTP :",bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 5,column= 0)
_ = Entry(f1,font=('Th Sarabun New',18,'bold'),textvariable=Menu2,
          bd = 10,insertwidth=4,bg="powder blue",justify='right').grid(row = 5,column=1)

_ = Button(f1,padx = 10,pady = 8,fg = 'black',font = ('TH Sarabun New',12,'bold'),
           text = "Enter",bg = "light gray",command = lambda:btnClear()).grid(row = 5,column = 2)

_ = Label(f1,font=('TH sarabun New',18,'bold'),text  = "Balance :" ,bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 0,column= 2)
_ = Label(f1,font=('Th Sarabun New',18,'bold'),textvariable=Menu6,
          bd = 10,width=16,bg="powder blue",justify='right').grid(row = 0,column=3)

_ = Label(f1,font=('TH sarabun New',18,'bold'),text  = "Cost :",bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 1,column= 2)
_ = Label(f1,font=('Th Sarabun New',18,'bold'),textvariable=Cost,
          bd = 10,width=16,bg="powder blue",justify='right').grid(row = 1,column=3)



_ = Label(f1,font=('TH sarabun New',18,'bold'),text  = "Signal :" ,bd = 16,
          anchor = 'w',bg = "seashell2").grid(row = 2,column= 2)

signal_label = Label(f1, font=('TH Sarabun New', 18, 'bold'), textvariable=signal_status, 
                     bd=10, anchor='w', fg="white", bg=signal_color.get(), width=16)
signal_label.grid(row=2, column=3)

# Entry for Cost (Just a placeholder)
Cost = StringVar()




refresh_color()

root.mainloop()

#========================Button==========================
_ = Button(f1,padx=16,pady=8,bd=16,fg="black",font= ('Th Sarabun New',18,'bold'),
           width = 10,text = "Total",bg = "powder blue",command=btnTotalClick)
_.grid(row = 7,column= 1)

_ = Button(f1,padx=16,pady=8,bd=16,fg="black",font= ('Th Sarabun New',18,'bold'),
           width = 10,text = "Reset",bg = "powder blue",command=btnReset)
_.grid(row = 7,column= 2)

_ = Button(f1,padx=16,pady=8,bd=16,fg="black",font= ('Th Sarabun New',18,'bold'),
           width = 10,text = "Exit",bg = "powder blue",command=btnExit)
_.grid(row = 7,column= 3)

root.mainloop()