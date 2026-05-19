import tkinter as tk


class myapp:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("text")
        self.root.configure(background="black")
        self.txt= tk.Text(background="black",foreground="white")
        self.txt.pack(padx=10,pady=10)
        self.bt=tk.Button(background="black",foreground="white",text="press me",command=self.hello)
        self.bt.pack(padx=10,pady=10)
        
    def hello(self):
       
        print (self.txt.get("1.00","end"))



root=tk.Tk()
apps=myapp(root)
root.mainloop()