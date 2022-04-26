from struct import pack
import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x450")
    root.grid()

    for num in range (9, -1, -1):
        button = tk.Button(root, text=num, font= ("Times New Roman", 30))
        
        c=(9-num)%3
        r=(int)((9-num)/3)
        button.grid(column=c, row=r, padx=10, pady=10)
    
    root.mainloop()

