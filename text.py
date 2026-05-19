import tkinter as tk
from tkinter import filedialog


class myapp:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("text")
        self.root.configure(background="black")
        self.txt= tk.Text(background="black",foreground="white")
        self.txt.pack(padx=10,pady=10)
        self.bt=tk.Button(background="black",foreground="white",text="save",command=self.saves)
        self.bt.pack(padx=10,pady=10)
        self.btl=tk.Button(background="black",foreground="white",text="load",command=self.loads)
        self.btl.pack(padx=10,pady=10)
        self.btc=tk.Button(background="black",foreground="white",text="clear",command=self.clears)
        self.btc.pack(padx=10,pady=10)

    def saves(self):
        f1=filedialog.asksaveasfile(defaultextension="*.*",confirmoverwrite=True,mode="w")
        f1.write(self.txt.get("1.0","end-1c"))
        f1.close()

    def loads(self):
        f1=filedialog.askopenfile(mode="r", defaultextension="*.txt")
        a=f1.read()
        f1.close()
        self.txt.delete("1.0","end-1c")
        self.txt.selection_clear()

        self.txt.insert("1.0",a)
    def clears(self):
        self.txt.delete("1.0","end-1c")
        self.txt.selection_clear()



root=tk.Tk()
apps=myapp(root)
root.mainloop()