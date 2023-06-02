import tkinter as tk
root= tk.Tk()
canvas=tk.Canvas(root,width=400,height=400)
canvas.pack()
canvas.create_rectangle(10,10,100,100,fill='red')
canvas.create_oval(175,100,100,175,width=5)
root.mainloop()
