import tkinter as tk
window=tk.Tk()
#window.geometry("1000x1000")
window.title('cns encryption algorism')
label=tk.Label(window,font=('Arial',18),text='encryption algorism')
label.grid(row=1,column=1)
label1=tk.Label(window,text="write the plan text to be encrypted",font=('Arial',12))
label1.grid(row=2,column=1)
textbox=tk.Text(window,height=10,)
textbox.grid(row=3,column=1)
label2=tk.Label(window,text="themessage to be decrypted",font=('Arial',12))
label2.grid(row=2,column=4)
button1=tk.Button(window,text='clickToencrpt',bg="red")
button1.grid(row=6,column=1)
button2=tk.Button(window,text='clicktoDecrypt',bg="green")
button2.grid(row=6,column=4)
textbox1=tk.Text(window,height=10,)
textbox1.grid(row=3,column=4)
lable3=tk.Label(window,text="chooseThe ALgorithm:",bg="blue")
lable3.grid(row=8,column=1)
lable4=tk.Label(window,text="message after decrpyt:",bg="white")
lable4.grid(row=9,column=1)
textbox2=tk.Text(window,height=10)
textbox2.grid(row=12,column=1)


window.mainloop()