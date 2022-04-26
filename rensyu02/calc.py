import tkinter as tk
import tkinter.messagebox as tkm

from tblib import Frame



if __name__ == "__main__":

    def button_click(event):
        btn = event.widget
        num = btn["text"]
        #tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
        entry.insert(tk.END, num)
        #button["bg"] = "yellow" 色の変化

    def click_equal(event): 
        eqn = entry.get()
        ans = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)

    def click_all_clear(event):
        entry.delete(0, tk.END)
        entry.insert(tk.END)

    def click_clear(event):
        pass


        
    root = tk.Tk()
    root.geometry("300x450")

    root.grid_rowconfigure(0, weight=1)

    entry=tk.Entry(root,
                    width=10,
                    justify="right",
                    font=("Times New Roman",40))
    entry.place(x=0, y=0)

    r=1
    c=1
    for i in range (9, -1, -1): #数字の表示
        button=tk.Button(root,
                        text=i,
                        font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(column=c, row=r)
        
        if i%3==1:
            r+=1
            c=0
        c+=1
    
    button=tk.Button(root,      #+の表示・押された時の処理
                    text="+",
                    font=("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.grid(column=2, row=4)

    button=tk.Button(root,      #=の表示・押された時の処理
                    text="=",
                    font=("Times New Roman", 30))
    button.bind("<1>",click_equal)
    button.grid(row=4,column=3)


    #追加機能

    button=tk.Button(root,      #acの表示・押された時の処理
                    text="a",
                    font=("Times New Roman", 30))
    button.bind("<1>", click_all_clear)
    button.grid(column=5, row=4)

    button=tk.Button(root,      #cの表示・押された時の処理
                    text="c",
                    font=("Times New Roman", 30))
    button.bind("<1>", click_clear)
    button.grid(column=5, row=3)

    root.mainloop()

