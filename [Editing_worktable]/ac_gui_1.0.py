import tkinter as tk

switch = True
temp = 18
mode = 1
fan = 2
swing = 'continously'
anti_b = 'OFF'
energy_s = 'OFF'

def visual(on_switch):
    global switch
    
    if on_switch == True:
        label['text'] = f'Temp: {temp}   \nFan: {fan}\nMode: {mode}    \nSwing: {swing}\nAnti Bacteria Mode: {anti_b}    \nEnergy Saving Mode: {energy_s}   '
        switch = False

    else:
        label['text'] = ""
        switch = True


def temp_up(on_switch):
    global temp

    if on_switch == False:
        if temp == 30:
            temp = temp

        else:
            temp += 1
        visual(True)

def temp_down(on_switch):
    global temp
    
    if on_switch == False:
        if temp == 18:
            temp = temp

        else:
            temp -= 1
        visual(True)


root = tk.Tk()

canvas = tk.Canvas(root, height= 500, width=300, bg="#F4F4F2")
canvas.pack()


top_frame = tk.Frame(root, bg='#E8E8E8')
top_frame.place(relx= 0.5, rely=0.05, relwidth=0.8, relheight=0.3, anchor="n")


low_frame = tk.Canvas(root, bg='#F4F4F2')
low_frame.place(relx= 0.5, rely=0.35, relwidth=0.8, relheight=0.7, anchor='n')


on_button = tk.Button(low_frame, text="I O", bg="#BBBFCA", command=lambda: visual(switch))
on_button.place(relx= 0.7, rely =0.1, relheight= 0.2, relwidth=0.2)


temp_up_button = tk.Button(low_frame, text="ʌ", command=lambda :temp_up(switch))
temp_up_button.place(relx= 0.2, rely = 0.1, relheight= 0.08, relwidth=0.1)


temp_down_button = tk.Button(low_frame, text="v", command=lambda :temp_down(switch))
temp_down_button.place(relx=0.2, rely = 0.2, relheight = 0.08, relwidth=0.1)


label = tk.Label(top_frame, bg='#E8E8E8')
label.place(relwidth=1, relheight=1)


root.mainloop()
