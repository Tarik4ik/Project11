import tkinter as tk

root = tk.Tk()
root.title("+ / -")
root.geometry("500x500")
p1 = 0
p2 = 0
p3 = 0

lbl1 = tk.Label(text=0, background="#17202A", foreground="#F4F6F7", padx="5", pady="10", font="15", height="2",
                width="8")

lbl1.place(x=100, y=50)

lbl2 = tk.Label(text=0, background="#17202A", foreground="#F4F6F7", padx="5", pady="10", font="15", height="2",
                width="8")

lbl2.place(x=300, y=50)

lbl3 = tk.Label(text=0, background="#1C2833", foreground="#E67E22", padx="5", pady="10", font="15", height="2",
                width="15")

lbl3.place(x=175, y=280)


def up1():
    global p1
    p1 += 1
    lbl1.config(text=p1)


def up2():
    global p2
    p2 += 1
    lbl2.config(text=p2)


def down1():
    global p1
    p1 -= 1
    lbl1.config(text=p1)


def down2():
    global p2
    p2 -= 1
    lbl2.config(text=p2)


def plus():
    global p3
    p3 = p1 + p2
    lbl3.config(text=p3)


def minus():
    global p3
    p3 = p1 - p2
    lbl3.config(text=p3)


pl1 = tk.Button(text="up", background="#E67E22", foreground="#ECF0F1", padx="10", pady="5", font="20", height="1",
                width="2", command=up1)

pl1.place(x=120, y=130)

min1 = tk.Button(text="down", background="#E67E22", foreground="#ECF0F1", padx="10", pady="5",  font="5", height="1", width="2",
                 command=down1)

min1.place(x=120, y=180)

pl2 = tk.Button(text="up", background="#E67E22", foreground="#ECF0F1", padx="10", pady="5", font="5", height="1", width="2",
                command=up2)

pl2.place(x=320, y=130)

min2 = tk.Button(text="down", background="#E67E22", foreground="#ECF0F1", padx="10", pady="5",  font="5", height="1", width="2",
                 command=down2)

min2.place(x=320, y=180)

pl3 = tk.Button(text="+", background="#E67E22", foreground="#ECF0F1", padx="15", pady="10", font="14", height="2", width="4",
                command=plus)

pl3.place(x=207, y=100)

min3 = tk.Button(text="-", background="#E67E22", foreground="#ECF0F1", padx="15", pady="10", font="14", height="2", width="4",
                command=minus)

min3.place(x=207, y=180)

root.mainloop()
