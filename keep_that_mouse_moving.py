import pyautogui
import time
import continuous_threading
import tkinter as tk

pyautogui.FAILSAFE = False

root = tk.Tk()
root.title('Keep that mouse moving')
root.iconbitmap('/Users/hassenkhouja/Desktop/Keep that mouse going/icon.ico')
root.geometry('300x200')

stop = False

status_text = tk.StringVar()
button_text = tk.StringVar()
status_text.set('Ready')
button_text.set('Start')

def handle_thread():
    global move_mouse_thread
    global stop
    global status_text
    global button_text
    global start_button
    if move_mouse_thread.is_alive():
        status_text.set('Stopping...')
        start_button['state'] = tk.DISABLED
        button_text.set('Stopping')
        stop = True
    else:
        status_text.set('Running...')
        button_text.set('Stop')
        stop = False
        move_mouse_thread = continuous_threading.Thread(target=move_mouse)
        move_mouse_thread.start()
        print(f'Starting Thread: {move_mouse_thread.getName()}')


def move_mouse():
    global status_text
    global button_text
    while True:
        print('Sleeping for 5 seconds...')
        time.sleep(5)
        if stop:
            print(f'Stopping Thread')
            status_text.set('Ready')
            start_button['state'] = tk.NORMAL
            button_text.set('Start')
            break
        current_position = pyautogui.position()
        print('Moving mouse to (0,0)...')
        pyautogui.moveTo(x = 0, y = 0)
        print('Moving mouse to previous position...')
        pyautogui.moveTo(current_position)
        print('Sleeping for 5 seconds...')
        time.sleep(5)
        if stop:
            print(f'Stopping Thread')
            status_text.set('Ready')
            start_button['state'] = tk.NORMAL
            button_text.set('Start')
            break
        



        

move_mouse_thread = continuous_threading.Thread(target=move_mouse)

start_button = tk.Button(root, textvariable = button_text, command = handle_thread)
start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
start_button.pack()

statusbar = tk.Label(root, textvariable = status_text, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

def handle_quit():
    global stop
    if not stop:
        stop = True
    root.destroy()

root.protocol('WM_DELETE_WINDOW', handle_quit)




root.mainloop()
