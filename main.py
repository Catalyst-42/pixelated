from tkinter import *
import time

root=Tk()
root.overrideredirect(True)
root.geometry('316x221+400+400')
# root.attributes("-topmost",True)
# root.attributes('-type', 'dock')
# root.resizable(height=1, width=1)
root.title('Log in')

# region main canvas
canvas = Canvas(root, height=221, width=316, highlightthickness=0, bd=0)
canvas.place(x=0, y=0)
img = PhotoImage(file='main.png')
canvas.create_image(316//2, 221//2, image=img)
# endregion

# region label with just text
label = Label(root, text='Name:', font='Ase 16', bg='#212124', fg='#b3b3b3')
label.place(x=6, y=44)
# endregion

# region bar
xwin = root.winfo_x()
ywin = root.winfo_y()

def get_pos(event):
    global xwin, ywin
    xwin = root.winfo_x() - event.x_root
    ywin = root.winfo_y() - event.y_root

def move_window(event):
    root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

bar = Canvas(root, width=316, height=31, highlightthickness=0, bd=0)
bar.place(x=0, y=0)
img_bar = PhotoImage(file="bar.png")
bar.create_image(316//2, 31//2, image=img_bar)

bar.bind('<B1-Motion>', move_window)
bar.bind('<Button-1>', get_pos)
# endregion

# region close X button in bar
current_image = PhotoImage(file='close.png')
other_image = PhotoImage(file='close_press.png')
def swap_close(event):
    global current_image, other_image, img_close
    btn_close.delete(img_close)
    img_close = btn_close.create_image(9, 11, image=other_image)
    current_image, other_image = other_image, current_image

def destroy(event):
    swap_close(0)
    if 0 <= event.x <= 18 and 0 <= event.y <= 22: root.quit()

btn_close = Canvas(root, width=18, height=22, highlightthickness=0, bd=0)
btn_close.place(x=293, y=5)
img_close = PhotoImage(file="close.png")
btn_close.create_image(9, 11, image=img_close)

btn_close.bind('<ButtonPress>', swap_close)
btn_close.bind('<ButtonRelease>', destroy)
# endregion

# region OK button
current_img_ok = PhotoImage(file='ok.png')
other_img_ok = PhotoImage(file='ok_press.png')
img_ok_enter = PhotoImage(file='ok_enter.png')
img_ok_stable = PhotoImage(file='ok.png')
ok_enter = 0
ok_press = 0
def swap_ok(event):
    global current_img_ok, other_img_ok, img_ok, img_ok_enter, ok_enter, img_ok_stable, ok_press

    if event.type == '4' or event.type == '5':
        if event.type == '4': ok_press = 1
        else: ok_press = 0
        btn_ok.delete(img_ok)
        img_ok = btn_ok.create_image(120//2, 34//2, image=other_img_ok)
        current_img_ok, other_img_ok = other_img_ok, current_img_ok
    
    if event.type == '7' or (ok_enter == 1 and event.type == '5'):
        ok_enter = 1
        btn_ok.delete(img_ok)
        img_ok = btn_ok.create_image(120//2, 34//2, image=img_ok_enter)

    if event.type == '8':
        ok_enter = 0
        if ok_press == 0:
            btn_ok.delete(img_ok)
            img_ok = btn_ok.create_image(120//2, 34//2, image=img_ok_stable)
    
    if event.type == '5' and ok_enter: 
        print(f'ok button function, checkbox: {checkbox_toggled}')
        

btn_ok = Canvas(root, width=120, height=34, highlightthickness=0, bd=0)
btn_ok.place(x=97, y=179)
img_ok = PhotoImage(file="ok.png")
btn_ok.create_image(120//2, 34//2, image=img_ok)
btn_ok.bind('<Enter>', swap_ok)
btn_ok.bind('<ButtonPress>', swap_ok)
btn_ok.bind('<ButtonRelease-1>', swap_ok)
btn_ok.bind('<Leave>', swap_ok)
# endregion

# region text input
def enter_focus(event):
    global text_label
    text_label.delete(img_text)
    text_label.create_image(192//2, 30//2, image=text_label_enter)

def enter_leave_focus(event):
    global text_label
    text_label.delete(text_label_enter)
    text_label.create_image(192//2, 30//2, image=img_text)

text_label = Canvas(root, width=192, height=30, highlightthickness=0, bd=0)
img_text = PhotoImage(file='field.png')
text_label_enter = PhotoImage(file='field_enter.png')
text_label.create_image(192//2, 30//2, image=img_text)
text_label.place(x=115, y=41)
text = Entry(root, font='Ase 16', bd=0, highlightthickness=0, bg='#1e2024', fg='#b3b3b3',
             insertwidth=2, width=17, insertbackground='#b3b3b3')
text.place(x=115+10, y=41+6)

text.bind('<FocusIn>', enter_focus)
text.bind('<FocusOut>', enter_leave_focus)
# endregion

# region time
# def update_time():
#     lbl_time.config(text=f'Time: {time.strftime("%H:%M:%S")}')
#     lbl_time.after(1000, update_time)

# lbl_time = Label(root, font='Ase 16', text=f'Time: {time.strftime("%H:%M:%S")}', bd=0, highlightthickness=0, bg='#1e2024', fg='#b3b3b3')
# lbl_time.place(x=6, y=153+39)
# lbl_time.after(1000, update_time)
# endregion

# region enter 2 label
label = Label(root, text='Password:', font='Ase 16', bg='#212124', fg='#b3b3b3')
label.place(x=6, y=83)
# endregion

# region text input 2
def enter_focus2(event):
    global text_labelM, text_label_enter2, img_text2
    text_labelM.delete(img_text2)
    text_labelM.create_image(192//2, 30//2, image=text_label_enter2)

def enter_leave_focus2(event):
    global text_labelM, text_label_enter2, img_text2
    text_labelM.delete(text_label_enter2)
    text_labelM.create_image(192//2, 30//2, image=img_text2)

img_text2 = PhotoImage(file='field.png')
text_label_enter2 = PhotoImage(file='field_enter.png')

text_labelM = Canvas(root, width=192, height=30, highlightthickness=0, bd=0)
text_labelM.place(x=115, y=79)
text_labelM.create_image(192//2, 30//2, image=img_text2)

text2 = Entry(root, font='Ase 16', bd=0, highlightthickness=0, bg='#1e2024', fg='#b3b3b3', insertwidth=2, width=17, insertbackground='#b3b3b3', show='*')
text2.place(x=115+10, y=79+6)
text2.bind('<FocusIn>', enter_focus2)
text2.bind('<FocusOut>', enter_leave_focus2)
# endregion

# region checkbox
checkbox = Canvas(root, height=24, width=298, highlightthickness=0, bd=0)
checkbox_toggled = 0
checkbox_entered = 0
img_checkbox = PhotoImage(file='checkbox.png')
img_checkbox_entered = PhotoImage(file='checkbox_enter.png')
img_checkbox_toggled = PhotoImage(file='checkbox_toggled.png')
img_checkbox_toggled_enter = PhotoImage(file='checkbox_toggled_enter.png')

def swap_checkbox(event):
    global checkbox_toggled, checkbox_entered
    global img_checkbox, img_checkbox_toggled_enter
    global img_checkbox_toggled, img_checkbox_toggled_enter

    if event.type == '5' and checkbox_entered: checkbox_toggled = 1 if checkbox_toggled == 0 else 0
    if event.type == '7': checkbox_entered = 1
    if event.type == '8': checkbox_entered = 0

    if checkbox_entered and checkbox_toggled:
        checkbox.delete('all')
        checkbox.create_image(298//2, 24//2, image=img_checkbox_toggled_enter)

    if checkbox_entered and not checkbox_toggled:
        checkbox.delete('all')
        checkbox.create_image(298//2, 24//2, image=img_checkbox_entered)

    if not checkbox_entered and checkbox_toggled:
        checkbox.delete('all')
        checkbox.create_image(298//2, 24//2, image=img_checkbox_toggled)

    if not checkbox_entered and not checkbox_toggled:
        checkbox.delete('all')
        checkbox.create_image(298//2, 24//2, image=img_checkbox)

checkbox.place(x=9, y=131)
checkbox.create_image(298//2, 24//2, image=img_checkbox)

checkbox.bind('<Enter>', swap_checkbox)
checkbox.bind('<ButtonRelease-1>', swap_checkbox)
checkbox.bind('<Leave>', swap_checkbox)
# endregion

root.mainloop()
