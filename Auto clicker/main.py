import pyautogui
import time
import tkinter as tk
from tkinter import *
import keyboard  # Import the stop_script function
from PIL import Image, ImageTk
import keyboard
from tkinter import messagebox
import threading

root = tk.Tk()
root.geometry("300x200")
root.resizable(width=False, height=False)


image = Image.open("background.jpg")  # img path  # open the img from the app
background_image = ImageTk.PhotoImage(image)  # the can me app
# select the  path
background_label = tk.Label(
    root, image=background_image
)  # here to choose the background make it lable in the root
background_label.place(
    x=0, y=0, relheight=1, relwidth=1
)  # potiion of the background to make it 0 and 0 to make it on all the screen


entrydelay = tk.Entry(root)
entrydelay.pack(side="left", pady=12)
entryclicks = tk.Entry(root)
entryclicks.pack(side="right", pady=12)
entryclicksleft = tk.Entry(root, width=20)
entryclicksleft.pack()
entryclicksleft.place(x=220, y=150)
labeledleftclicks = tk.Label(
    root,
    text="Left Clicks :",
)  # Adjust the width as needed
labeledleftclicks.pack()
labeledleftclicks.place(x=220, y=120)
entryclicksleftdelay = tk.Entry(root, width=14)
entryclicksleftdelay.pack()
entryclicksleftdelay.place(x=0, y=150)
labeledelayleft = tk.Label(
    root,
    text="Put Your Left Delay:",
)  # Adjust the width as needed
labeledelayleft.pack()
labeledelayleft.place(x=0, y=120)


def ok():
    def on_key_event(e):
        try:
            if e.name == "esc":
                print('You Pressed "ESC" Program has Closed..')
                root.destroy()
            elif e.name == "s":
                print("Started")
                start_task()
        except e:
            print("SomeThing Is Wrong")
        keyboard.on_press(on_key_event)


def on_key_event(e):
    try:
        if e.name == "esc":
            print('You Pressed "ESC" Program has Closed..')
            root.destroy()
        elif e.name == "s":
            print("Started")
            start_task()
    except e:
        print("SomeThing Is Wrong")


keyboard.on_press(on_key_event)


def simulate_clicks():
    button["state"] = "disable"
    button["fg"] = "red"
    try:
        click_delay = user_input = entrydelay.get()
        num_clicks = user_input = entryclicks.get()
        num_clicksleft = user_input = entryclicksleft.get()
        click_delayleft = user_input = entryclicksleftdelay.get()
        click_delay = int(click_delay) * 100
        num_clicks = int(num_clicks)
        num_clicksleft = int(num_clicksleft)
        click_delayleft = int(click_delayleft) * 100
    except:
        print(
            f"your Numbers is : {click_delay} , {num_clicks} , if this have chrs or float number , the programe accept only int :)"
        )
    else:
        print(
            f"your Numbers is : {click_delay} , {num_clicks} , if this have chrs or float number , the programe accept only int :)"
        )

        def leftClick():
            for _ in range(num_clicks):
                pyautogui.click()
                root.after(click_delay)
                print(f"Left Click {_}")
                time.sleep(0.5)

        def rightclick():
            for c in range(num_clicksleft):
                pyautogui.click(button="right")
                root.after(click_delayleft)
                print(f"Right Click {c}")
                time.sleep(0.5)

    thread1 = threading.Thread(target=leftClick)
    thread2 = threading.Thread(target=rightclick)
    thread3 = threading.Thread(target=ok)

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

    def show_alert():
        messagebox.showinfo(
            "done✅", f"Right: {num_clicks} Left: {num_clicksleft} Clicks Clicked ✔"
        )

    show_alert()
    button["state"] = "normal"
    button["fg"] = "white"


def start_task():
    task_thread = threading.Thread(target=simulate_clicks)
    task_thread.start()


root.title("Mouse Auto Click")
labeledelay = tk.Label(
    root,
    text="Put Your Right Delay:",
)  # Adjust the width as needed
labeledelay.pack()
labeledelay.place(x=0, y=60)


labeledclicks = tk.Label(
    root,
    text="Right Clicks :",
)  # Adjust the width as needed
labeledclicks.pack()
labeledclicks.place(x=200, y=60)


original_image = Image.open("buttom.png")
resized_image = original_image.resize((50, 50))
bg_image = ImageTk.PhotoImage(resized_image)
button = tk.Button(
    root,
    text="Start",
    font=("Arial Black",),
    command=start_task,
    image=bg_image,
    compound="center",
    fg="white",
)

button.pack()
button.place(x=120, y=140)


root.mainloop()
