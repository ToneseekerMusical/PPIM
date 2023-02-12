import tkinter as tk
import random

class DynamicGrid(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.text = tk.Text(self, wrap="char", borderwidth=0, highlightthickness=0,
                            state="disabled")
        self.text.pack(fill="both", expand=True)
        self.boxes = []

    def add_box(self, color=None):
        bg = color if color else random.choice(("red", "orange", "green", "blue", "violet"))
        box = tk.Frame(self.text, bd=1, relief="sunken", background=bg,
                       width=100, height=100)
        self.boxes.append(box)
        self.text.configure(state="normal")
        self.text.window_create("end", window=box)
        self.text.configure(state="disabled")

class Example(object):
    def __init__(self):
        self.root = tk.Tk()
        self.dg = DynamicGrid(self.root, width=500, height=200)
        add_button  = tk.Button(self.root, text="Add", command=self.dg.add_box)

        add_button.pack()
        self.dg.pack(side="top", fill="both", expand=True)

        # add a few boxes to start
        for i in range(10):
            self.dg.add_box()

    def start(self):
        self.root.mainloop()

Example().start()