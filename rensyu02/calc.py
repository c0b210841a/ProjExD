import tkinter as tk
import tkinter.messagebox as tkm



if __name__ == "__main__":

    def button_click(event):
        btn = event.widget
        num = btn["text"]
        #tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
        entry.insert(tk.END, num)

    def click_equal(event):
        eqn = entry.get()
        ans = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)
        
    root = tk.Tk()
    root.geometry("300x450")

    entry=tk.Entry(root,
                    width=10,
                    justify="right",
                    font=("Times New Roman",40))
    entry.grid(row=0, column=0, columnspan=4)

    r=1
    c=1
    for i in range (9, -1, -1):
        button=tk.Button(root,
                        text=i,
                        font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(column=c, row=r, padx=10, pady=10)
        
        if i%3==1:
            r+=1
            c=0
        c+=1
    
    button=tk.Button(root,
                    text="+",
                    font=("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.grid(column=2, row=4, padx=10, pady=10)

    button=tk.Button(root,
                    text="=",
                    font=("Times New Roman", 30))
    button.bind("<1>",click_equal)
    button.grid(row=4,column=3,padx=10,pady=10)

    
    root.mainloop()

