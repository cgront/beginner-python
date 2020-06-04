import tkinter as tk 
root = tk.Tk()

def key(event):
  args = event.keysym, event.keycode, event.char 
  print("Symbol: {}, Code: {}, Char: {}".format(*args)) 

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = tk.Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()